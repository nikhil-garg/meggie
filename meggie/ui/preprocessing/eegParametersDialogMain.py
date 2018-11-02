"""
"""
import logging

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from meggie.ui.preprocessing.eegParametersDialogUi import Ui_Dialog

import numpy as np

from meggie.ui.utils.messaging import exc_messagebox
from meggie.ui.utils.messaging import messagebox

from meggie.code_meggie.preprocessing.projections import find_eog_events
from meggie.code_meggie.preprocessing.projections import plot_average_epochs
from meggie.code_meggie.preprocessing.projections import call_eeg_ssp

class EegParametersDialog(QtWidgets.QDialog):
    
    def __init__(self, parent):
        QtWidgets.QDialog.__init__(self)
        self.parent = parent
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        raw = self.parent.experiment.active_subject.get_working_file()
        self.ui.comboBoxChannelSelect.addItems(raw.ch_names)
        
        self.ui.tableWidgetEvents.currentItemChanged.connect(
            self.on_currentChanged
        )
        self.ui.tableWidgetEvents.setSortingEnabled(False)
        self.ui.tableWidgetEvents.setSelectionBehavior(1)        
        self.ui.tableWidgetEvents.setColumnCount(2)
        self.set_event_table_headers()
        
        
    def on_pushButtonAdd_clicked(self, checked=None):
        """
        Finds EOG-events from the raw data.
        Called when find eog events -button is clicked.
        """
        raw = self.parent.experiment.active_subject.get_working_file()
        if checked is None or not raw: return
        
        params = dict()
        params['ch_name'] = str(self.ui.comboBoxChannelSelect.currentText())
        params['l_freq'] = float(self.ui.doubleSpinBoxLowPass.value())
        params['h_freq'] = float(self.ui.doubleSpinBoxHighPass.value())
        params['filter_length'] = str(self.ui.spinBoxFilterLength.value())+'s'
        params['tstart'] = float(self.ui.doubleSpinBoxStart.value())

        invert = self.ui.checkBoxInvertPolarity.isChecked()

        # monkey patch peak finder temporarily in the eog module
        # to allow inverting polarity
        import mne

        original_peak_finder = mne.preprocessing.eog.peak_finder

        def new_peak_finder(x0, thresh=None, extrema=1, verbose=None):
            if invert:
                return original_peak_finder(x0, thresh, -extrema, 
                                            verbose)
            return original_peak_finder(x0, thresh, extrema, verbose)

        mne.preprocessing.eog.peak_finder = new_peak_finder

        try:
            eog_events = find_eog_events(self.parent.experiment, params)
            self.ui.tableWidgetEvents.clear()
            self.ui.tableWidgetEvents.setRowCount(0)
            for i in range(0, len(eog_events)):
                self.ui.tableWidgetEvents.insertRow(i)
                self.ui.tableWidgetEvents.setItem(
                    i,0,QtWidgets.QTableWidgetItem(
                        str(raw.times[eog_events[i][0] - raw.first_samp])
                    )
                )
                self.ui.tableWidgetEvents.setItem(i,1,QtWidgets.
                    QTableWidgetItem(str(int(eog_events[i][0])))
                )
        except Exception as e:
            exc_messagebox(self, e)

        mne.preprocessing.eog.peak_finder = original_peak_finder

        self.set_event_table_headers()
            
    def get_events(self):
        """
        A convenience function for fetching all the events from
        the tableWidgetEvents as a numpy array.
        returns:
        eog_events as numpy array
        """
        events = list()
        rowCount = self.ui.tableWidgetEvents.rowCount()
        
        for i in range(0, rowCount):
            time = int(self.ui.tableWidgetEvents.item(i, 1).text())
            events.append([time, 0, 1])

        return np.array(events)

    def on_pushButtonRemove_clicked(self, checked=None):
        if checked is None: 
            return
        index = self.ui.tableWidgetEvents.currentRow()
        self.ui.tableWidgetEvents.removeRow(index)

    @QtCore.pyqtSlot()
    def on_currentChanged(self):
        """
        Called when tableWidgetEvent row selection is changed.
        """
        index = self.ui.tableWidgetEvents.currentIndex().row()
        if index < 0:
            self.ui.pushButtonRemove.setEnabled(False)
        else:
            self.ui.pushButtonRemove.setEnabled(True)

    def on_pushButtonPlotEpochs_clicked(self, checked=None):
        """
        Plots the averaged epochs.
        """
        if checked is None: 
            return
        events = self.get_events()
        tmin = self.ui.doubleSpinBoxTmin.value()
        tmax = self.ui.doubleSpinBoxTmax.value()
        plot_average_epochs(self.parent.experiment, events, tmin, tmax)
        
    def on_pushButtonShowEvents_clicked(self, checked=None):
        """
        Plots the events on mne_browse_raw.
        """
        if checked is None: 
            return
        events = self.get_events()

        raw = self.parent.experiment.active_subject.get_working_file()
        logging.getLogger('ui_logger').info('Plotting events..')

        raw.plot(events=events, scalings=dict(eeg=40e-6))

    def set_event_table_headers(self):
        self.ui.tableWidgetEvents.setHorizontalHeaderLabels([
            "Time (s)",
            "Sample"
        ])
    
    def collect_parameter_values(self):
        """Collects parameter values from dialog.
        """
        dictionary = dict()
        dictionary['tmin'] = self.ui.doubleSpinBoxTmin.value()
        dictionary['tmax'] = self.ui.doubleSpinBoxTmax.value()
        dictionary['events'] = self.get_events()
        dictionary['n_eeg'] = self.ui.spinBoxVectors.value()
        return dictionary

    def accept(self):
        """
        """
        parameter_values = self.collect_parameter_values()
        if len(parameter_values['events']) == 0:
            messagebox(self.parent, 'Add events before computing projects.')
            return
        try:
            self.calculate_eeg(self.parent.experiment.active_subject, parameter_values)    
        except Exception as e:
            pass
        self.parent.initialize_ui()
        self.close()

    def calculate_eeg(self, subject, params):
        update_ui = self.parent.update_ui
        call_eeg_ssp(params, subject, update_ui=update_ui)

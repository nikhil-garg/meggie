# coding: latin1
'''
Created on Mar 19, 2013

@author: Jaakko Lepp�kangas, Atte Rautio
'''
from PyQt4 import QtCore,QtGui
from parameterDialog_ui import Ui_ParameterDialog
from epochDialog_main import EpochDialog

from tkFileDialog import askopenfilename
from Tkinter import Tk
#from enaml.components.push_button import PushButton

from epochs import Epochs
from events import Events
import brainRegions

import numpy as np

class ParameterDialog(QtGui.QDialog):
    """
    Class containing the logic for ParameterDialog
    """
    index = 1

    def __init__(self, parent):
        """
        Initializes the event selection dialog.
        """
        QtGui.QDialog.__init__(self)
        self.parent = parent
        self.ui = Ui_ParameterDialog()
        self.ui.setupUi(self)
        keys = map(str, parent.experiment.event_set.keys())
        self.ui.comboBoxEventID.addItems(keys)
        self.ui.lineEditName.setText('Event' + str(self.__class__.index))
        
        """        
    def on_browseButton_clicked(self, checked=None):
        if checked is None: return # Standard workaround for file dialog opening twice
        self.fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/usr/local/bin/ParkkosenPurettu/meg/jn')
        self.fileEdit.setText(self.fname)
        """
        
    def create_eventlist(self):
        self.event_id = int(self.ui.comboBoxEventID.currentText())
        event_name = self.ui.lineEditName.text()
        print self.parent.experiment.stim_channel
        e = Events(self.parent.experiment.raw_data, 'STI 014')
        e.pick(self.event_id)
        return e.events
        """
        self.tmin = float(self.ui.doubleSpinBoxTmin.value())
        self.tmax = float(self.ui.doubleSpinBoxTmax.value())
        epoch_name = self.ui.lineEditName.text()
        mag = self.ui.checkBoxMag.checkState() == QtCore.Qt.Checked
        grad = self.ui.checkBoxGrad.checkState() == QtCore.Qt.Checked
        eeg = self.ui.checkBoxEeg.checkState() == QtCore.Qt.Checked
        stim = self.ui.checkBoxStim.checkState() == QtCore.Qt.Checked
        eog = self.ui.checkBoxEog.checkState() == QtCore.Qt.Checked
        channels = self.check_channels()
        reject = dict(grad = 1e-12 * self.ui.doubleSpinBoxGradReject_3.value(),
                      mag = 1e-12 * self.ui.doubleSpinBoxMagReject_3.value(),
                      eeg = 1e-6 * self.ui.doubleSpinBoxEEGReject_3.value(),
                      eog = 1e-6 * self.ui.doubleSpinBoxEOGReject_3.value())
        print channels
        try:
            epochs = Epochs(self.parent.experiment.raw_data, stim_channel, mag,
                            grad, eeg, stim, eog, reject, epoch_name, float(self.tmin),
                            float(self.tmax), int(self.event_id), channels)
        except:
            return #TODO error handling
        return epochs
        """
        
    def on_pushButtonAdd_clicked(self, checked=None):
        if checked is None: return # Standard workaround
        events = self.create_eventlist()
        print events
        self.__class__.index += 1
        
        """
        Adds the events to the list.
        """
        if isinstance(events, np.ndarray):
            for event in events:
                item = QtGui.QListWidgetItem(self.ui.lineEditName.text() +
                                             ' ' + str(event[0]) + ', ' +
                                             str(event[2]))
                item.setData(32, event)
                item.setData(33, self.ui.lineEditName.text())
                self.ui.listWidgetEvents.addItem(item)
            self.ui.listWidgetEvents.setCurrentItem(item)
            """
            event_set = '(ID:' + str(self.event_id) + ', ' + \
                str(self.parent.experiment.event_set.get(self.event_id)) + \
                ' events, start: ' + str(self.tmin) + ', end: ' + \
                str(self.tmax) + ')'
            item = QtGui.QListWidgetItem(self.ui.lineEditName.text() + ' ' + event_set)
            item.setData(1, epochs)
            self.ui.listWidgetEvents.addItem(item)
            self.ui.lineEditName.setText('Event' + str(self.__class__.index))
            self.ui.listWidgetEvents.setCurrentItem(item) #select the last item
            """
            self.ui.lineEditName.setText('Event' + str(self.__class__.index))
            self.ui.pushButtonRemove.setEnabled(True)
        
    def on_pushButtonRemove_clicked(self, checked=None):
        """
        Method for removing events from the list
        """
        if checked is None: return # Standard workaround
        row = self.ui.listWidgetEvents.currentRow()
        self.ui.listWidgetEvents.takeItem(row)
        if self.ui.listWidgetEvents.currentRow() < 0:
            self.ui.pushButtonRemove.setEnabled(False)
        
        
    def accept(self):
        """
        Called when the OK button is pressed.
        """
        self.close()
        self.epochDialog = EpochDialog(self)
        epochs = self.epochDialog.exec_()
        """
        for index in xrange(self.ui.listWidgetEvents.count()):
            item = QtGui.QListWidgetItem(self.ui.listWidgetEvents.item(index).text())
            item.setData(1, self.ui.listWidgetEvents.item(index).data(1).toPyObject())
            self.parent.widget.ui.listWidgetEpochs.addItem(item)
        """            
        #self.parent.ui.tabWidget.setCurrentIndex(1)
        #for index in xrange(self.ui.listWidgetEvents.count()):
        #    item = QtGui.QListWidgetItem(self.ui.listWidgetEvents.item(index).text())
        #    item.setData(1, self.ui.listWidgetEvents.item(index).data(1).toPyObject())
        #    self.parent.ui.listWidgetEventsPre.addItem(item)
            
        #self.parent.ui.tabWidget.setCurrentIndex(2)
        
        #print self.ui.listWidgetEvents.currentItem().data(1).toPyObject()
        
    def check_channels(self):
        if self.ui.comboBoxChannelGroup.currentText() == 'Vertex':
            return ['MEG ' + str(x) for x in brainRegions.vertex]
        elif self.ui.comboBoxChannelGroup.currentText() == 'Left-temporal':
            return ['MEG ' + str(x) for x in brainRegions.left_temporal]
        elif self.ui.comboBoxChannelGroup.currentText() == 'Right-temporal':
            return ['MEG ' + str(x) for x in brainRegions.right_temporal]
        elif self.ui.comboBoxChannelGroup.currentText() == 'Left-parietal':
            return ['MEG ' + str(x) for x in brainRegions.left_parietal]
        elif self.ui.comboBoxChannelGroup.currentText() == 'Right-parietal':
            return ['MEG ' + str(x) for x in brainRegions.right_parietal]
        elif self.ui.comboBoxChannelGroup.currentText() == 'Left-occipital':
            return ['MEG ' + str(x) for x in brainRegions.left_occipital]
        elif self.ui.comboBoxChannelGroup.currentText() == 'Right-occipital':
            return ['MEG ' + str(x) for x in brainRegions.right_occipital]
        elif self.ui.comboBoxChannelGroup.currentText() == 'Left-frontal':
            return ['MEG ' + str(x) for x in brainRegions.left_frontal]
        elif self.ui.comboBoxChannelGroup.currentText() == 'Right-frontal':
            return ['MEG ' + str(x) for x in brainRegions.right_frontal]
        
        """
        self.fname = self.fileEdit.text()
        stim_channel = str(self.ui.comboBoxStimulus.currentText())
        event_id = self.ui.lineEditEventID.text()
        tmin = self.ui.lineEditTmin.text()
        tmax = self.ui.lineEditTmax.text()
        reject = self.ui.lineEditReject.text()
        meg = self.ui.checkBoxMeg.checkState() == QtCore.Qt.Checked
        eeg = self.ui.checkBoxEeg.checkState() == QtCore.Qt.Checked
        stim = self.ui.checkBoxStim.checkState() == QtCore.Qt.Checked
        eog = self.ui.checkBoxEog.checkState() == QtCore.Qt.Checked
        self.close()
        self.parent.epochs = CreateEpochs(self.parent.raw, event_id,
                                          stim_channel, tmin, tmax, reject,
                                          meg, eeg, stim, eog)
        
        """
        
    def on_pushButtonSaveEvents_clicked(self, checked=None):
        if checked is None: return # Standard workaround
        events = np.ndarray((self.ui.listWidgetEvents.count(),4), dtype=object)
        for index in xrange(self.ui.listWidgetEvents.count()):
            category = (self.ui.listWidgetEvents.item(index).
                        data(33).toPyObject())
            events[index,0] = str(category)
            event = self.ui.listWidgetEvents.item(index).data(32).toPyObject()
            events[index,1:] = event
        #events = self.create_eventlist()'
        if len(events) > 0:
            print 'Writing events...'
            self.parent.caller.write_events(events)
            print 'Done.'
    
    def on_pushButtonReadEvents_clicked(self, checked=None):
        if checked is None: return # Standard workaround
        filename = str(QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                                    self.parent.experiment.subject_directory))
        if filename == '':
            return
        self.ui.listWidgetEvents.clear()
        sheet = self.parent.caller.read_events(filename)

        for row_index in range(sheet.nrows):
            #Check that there are no empty cells in a row
            if not (any([x == '' for x in sheet.row_values(row_index)])):
                item = QtGui.QListWidgetItem(str(sheet.cell(row_index,0).value)
                                             + ' ' + str(int(sheet.cell
                                                             (row_index,1).
                                                             value))
                                             + ', ' + str(int(sheet.cell
                                                              (row_index,3)
                                                              .value)))
                event = map(int, sheet.row_values(row_index)[1:4])
                item.setData(32, event)
                item.setData(33, str(sheet.cell(row_index,0).value))
                self.ui.listWidgetEvents.addItem(item)
            
        self.ui.listWidgetEvents.setCurrentItem(item)
        
"""
"""
import logging

from PyQt5 import QtWidgets
from PyQt5 import QtCore

from meggie.utilities.dialogs.groupAverageDialogUi import Ui_groupAverageDialog
from meggie.utilities.messaging import exc_messagebox
from meggie.utilities.validators import validate_name


class GroupAverageDialog(QtWidgets.QDialog):

    def __init__(self, experiment, parent, handler, default_name):
        """
        """
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_groupAverageDialog()
        self.ui.setupUi(self)

        self.handler = handler

        subjects = experiment.subjects.keys()
        subject_count = len(subjects)

        # fill the dialog with subjects
        for idx, subject_name in enumerate(subjects):
            self.add_item(idx, subject_name)

        self.subjects = subjects

        self.ui.lineEditName.setText(default_name)

    def add_item(self, idx, name):
        """ creates label-spinbox item and adds it to screen """
        setattr(self.ui, 'horizontalLayoutGroup_' +
                str(idx), QtWidgets.QHBoxLayout())
        getattr(self.ui, 'horizontalLayoutGroup_' + str(idx)).setObjectName(
            'horizontalLayoutGroup_' + str(idx))

        setattr(self.ui, 'checkBoxGroup_' + str(idx),
                QtWidgets.QCheckBox(self.ui.groupBoxAverageGroups))
        getattr(self.ui, 'checkBoxGroup_' + str(idx)
                ).setObjectName('checkBoxGroup_' + str(idx))
        getattr(self.ui, 'checkBoxGroup_' + str(idx)).setText('')
        getattr(self.ui, 'checkBoxGroup_' + str(idx)).setMaximumSize(20, 20)
        getattr(self.ui, 'checkBoxGroup_' + str(idx)
                ).setCheckState(QtCore.Qt.Checked)
        getattr(self.ui, 'horizontalLayoutGroup_' + str(idx)).addWidget(
            getattr(self.ui, 'checkBoxGroup_' + str(idx)))

        setattr(self.ui, 'labelGroup_' + str(idx),
                QtWidgets.QLabel(self.ui.groupBoxAverageGroups))
        getattr(self.ui, 'labelGroup_' + str(idx)
                ).setObjectName('labelGroup_' + str(idx))
        getattr(self.ui, 'labelGroup_' + str(idx)).setText(name)
        getattr(self.ui, 'horizontalLayoutGroup_' + str(idx)).addWidget(
            getattr(self.ui, 'labelGroup_' + str(idx)))

        setattr(self.ui, 'spinBoxGroup_' + str(idx),
                QtWidgets.QSpinBox(self.ui.groupBoxAverageGroups))
        getattr(self.ui, 'spinBoxGroup_' + str(idx)).setMinimum(1)
        getattr(self.ui, 'spinBoxGroup_' + str(idx)).setMaximumSize(40, 1000)
        getattr(self.ui, 'spinBoxGroup_' + str(idx)
                ).setObjectName('spinBoxGroup_' + str(idx))
        getattr(self.ui, 'horizontalLayoutGroup_' + str(idx)).addWidget(
            getattr(self.ui, 'spinBoxGroup_' + str(idx)))

        self.ui.gridLayout.addLayout(getattr(self.ui, 'horizontalLayoutGroup_' + str(idx)),
                                     idx, 2, 1, 1)

    def accept(self):
        groups = {}
        for idx, subject in enumerate(self.subjects):
            selected = getattr(self.ui, 'checkBoxGroup_' +
                               str(idx)).checkState()
            if selected != QtCore.Qt.Checked:
                continue
            group_id = getattr(self.ui, 'spinBoxGroup_' + str(idx)).value()
            if group_id in groups:
                groups[group_id].append(subject)
            else:
                groups[group_id] = [subject]

        try:
            name = validate_name(self.ui.lineEditName.text())
        except Exception as exc:
            exc_messagebox(self, exc)
            return

        self.handler(name, groups)

        self.close()

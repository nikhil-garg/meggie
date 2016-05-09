# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'covarianceEpochDialogUi.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_covarianceEpochDialog(object):
    def setupUi(self, covarianceEpochDialog):
        covarianceEpochDialog.setObjectName(_fromUtf8("covarianceEpochDialog"))
        covarianceEpochDialog.resize(515, 571)
        self.gridLayout = QtGui.QGridLayout(covarianceEpochDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(covarianceEpochDialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 495, 514))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(474, 492))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBoxEpochs = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxEpochs.setObjectName(_fromUtf8("groupBoxEpochs"))
        self.listWidgetEpochs = QtGui.QListWidget(self.groupBoxEpochs)
        self.listWidgetEpochs.setGeometry(QtCore.QRect(10, 30, 441, 191))
        self.listWidgetEpochs.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidgetEpochs.setObjectName(_fromUtf8("listWidgetEpochs"))
        self.verticalLayout.addWidget(self.groupBoxEpochs)
        self.groupBoxParams = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxParams.setObjectName(_fromUtf8("groupBoxParams"))
        self.verticalLayoutWidget = QtGui.QWidget(self.groupBoxParams)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 470, 188))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelTmin = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelTmin.setObjectName(_fromUtf8("labelTmin"))
        self.horizontalLayout.addWidget(self.labelTmin)
        self.doubleSpinBoxTmin = QtGui.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBoxTmin.setMinimum(-1000000000.0)
        self.doubleSpinBoxTmin.setMaximum(1000000000.0)
        self.doubleSpinBoxTmin.setSingleStep(0.1)
        self.doubleSpinBoxTmin.setObjectName(_fromUtf8("doubleSpinBoxTmin"))
        self.horizontalLayout.addWidget(self.doubleSpinBoxTmin)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelTmax = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelTmax.setObjectName(_fromUtf8("labelTmax"))
        self.horizontalLayout_2.addWidget(self.labelTmax)
        self.doubleSpinBoxTmax = QtGui.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBoxTmax.setMinimum(-1000000000.0)
        self.doubleSpinBoxTmax.setMaximum(1000000000.0)
        self.doubleSpinBoxTmax.setSingleStep(0.1)
        self.doubleSpinBoxTmax.setObjectName(_fromUtf8("doubleSpinBoxTmax"))
        self.horizontalLayout_2.addWidget(self.doubleSpinBoxTmax)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.labelMethod = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelMethod.setObjectName(_fromUtf8("labelMethod"))
        self.horizontalLayout_3.addWidget(self.labelMethod)
        self.comboBoxMethod = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBoxMethod.setObjectName(_fromUtf8("comboBoxMethod"))
        self.horizontalLayout_3.addWidget(self.comboBoxMethod)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.labelNjobs = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelNjobs.setObjectName(_fromUtf8("labelNjobs"))
        self.horizontalLayout_4.addWidget(self.labelNjobs)
        self.spinBoxNjobs = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.spinBoxNjobs.setEnabled(True)
        self.spinBoxNjobs.setMinimum(1)
        self.spinBoxNjobs.setMaximum(99)
        self.spinBoxNjobs.setProperty("value", 3)
        self.spinBoxNjobs.setObjectName(_fromUtf8("spinBoxNjobs"))
        self.horizontalLayout_4.addWidget(self.spinBoxNjobs)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.checkBoxKeepSampleMean = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxKeepSampleMean.setEnabled(False)
        self.checkBoxKeepSampleMean.setChecked(True)
        self.checkBoxKeepSampleMean.setObjectName(_fromUtf8("checkBoxKeepSampleMean"))
        self.verticalLayout_2.addWidget(self.checkBoxKeepSampleMean)
        self.verticalLayout.addWidget(self.groupBoxParams)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(covarianceEpochDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(covarianceEpochDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), covarianceEpochDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), covarianceEpochDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(covarianceEpochDialog)

    def retranslateUi(self, covarianceEpochDialog):
        covarianceEpochDialog.setWindowTitle(_translate("covarianceEpochDialog", "Compute covariance from epoch file", None))
        self.groupBoxEpochs.setTitle(_translate("covarianceEpochDialog", "Select epochs for computation:", None))
        self.groupBoxParams.setTitle(_translate("covarianceEpochDialog", "Set parameters:", None))
        self.labelTmin.setText(_translate("covarianceEpochDialog", "Start time:", None))
        self.doubleSpinBoxTmin.setSuffix(_translate("covarianceEpochDialog", " s", None))
        self.labelTmax.setText(_translate("covarianceEpochDialog", "End time:", None))
        self.doubleSpinBoxTmax.setSuffix(_translate("covarianceEpochDialog", " s", None))
        self.labelMethod.setText(_translate("covarianceEpochDialog", "Method:", None))
        self.labelNjobs.setText(_translate("covarianceEpochDialog", "Number of jobs:", None))
        self.checkBoxKeepSampleMean.setText(_translate("covarianceEpochDialog", "Keep sample mean (not checked enabled for empirical method)", None))

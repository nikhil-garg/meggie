# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TFRfromEpochs.ui'
#
# Created: Mon Sep 16 14:07:04 2013
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_DialogEpochsTFR(object):
    def setupUi(self, DialogEpochsTFR):
        DialogEpochsTFR.setObjectName(_fromUtf8("DialogEpochsTFR"))
        DialogEpochsTFR.resize(292, 346)
        self.verticalLayout_2 = QtGui.QVBoxLayout(DialogEpochsTFR)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scrollArea = QtGui.QScrollArea(DialogEpochsTFR)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 274, 289))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(197, 134))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.groupBoxFrequencies = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxFrequencies.setGeometry(QtCore.QRect(0, 0, 271, 281))
        self.groupBoxFrequencies.setObjectName(_fromUtf8("groupBoxFrequencies"))
        self.layoutWidget = QtGui.QWidget(self.groupBoxFrequencies)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 251, 241))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.comboBoxChannels = QtGui.QComboBox(self.layoutWidget)
        self.comboBoxChannels.setObjectName(_fromUtf8("comboBoxChannels"))
        self.verticalLayout_6.addWidget(self.comboBoxChannels)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.labelMinFreq = QtGui.QLabel(self.layoutWidget)
        self.labelMinFreq.setObjectName(_fromUtf8("labelMinFreq"))
        self.horizontalLayout_13.addWidget(self.labelMinFreq)
        self.doubleSpinBoxMinFreq = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxMinFreq.setMinimum(0.1)
        self.doubleSpinBoxMinFreq.setMaximum(200.0)
        self.doubleSpinBoxMinFreq.setProperty("value", 7.0)
        self.doubleSpinBoxMinFreq.setObjectName(_fromUtf8("doubleSpinBoxMinFreq"))
        self.horizontalLayout_13.addWidget(self.doubleSpinBoxMinFreq)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.labelMaxFreq = QtGui.QLabel(self.layoutWidget)
        self.labelMaxFreq.setObjectName(_fromUtf8("labelMaxFreq"))
        self.horizontalLayout_12.addWidget(self.labelMaxFreq)
        self.doubleSpinBoxMaxFreq = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxMaxFreq.setMinimum(7.0)
        self.doubleSpinBoxMaxFreq.setMaximum(600.0)
        self.doubleSpinBoxMaxFreq.setProperty("value", 30.0)
        self.doubleSpinBoxMaxFreq.setObjectName(_fromUtf8("doubleSpinBoxMaxFreq"))
        self.horizontalLayout_12.addWidget(self.doubleSpinBoxMaxFreq)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelFrequencyInterval = QtGui.QLabel(self.layoutWidget)
        self.labelFrequencyInterval.setObjectName(_fromUtf8("labelFrequencyInterval"))
        self.horizontalLayout.addWidget(self.labelFrequencyInterval)
        self.doubleSpinBoxFreqInterval = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxFreqInterval.setMinimum(0.1)
        self.doubleSpinBoxFreqInterval.setMaximum(99.99)
        self.doubleSpinBoxFreqInterval.setProperty("value", 3.0)
        self.doubleSpinBoxFreqInterval.setObjectName(_fromUtf8("doubleSpinBoxFreqInterval"))
        self.horizontalLayout.addWidget(self.doubleSpinBoxFreqInterval)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelNcycles = QtGui.QLabel(self.layoutWidget)
        self.labelNcycles.setObjectName(_fromUtf8("labelNcycles"))
        self.horizontalLayout_2.addWidget(self.labelNcycles)
        self.spinBoxNcycles = QtGui.QSpinBox(self.layoutWidget)
        self.spinBoxNcycles.setMinimum(1)
        self.spinBoxNcycles.setProperty("value", 7)
        self.spinBoxNcycles.setObjectName(_fromUtf8("spinBoxNcycles"))
        self.horizontalLayout_2.addWidget(self.spinBoxNcycles)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_8.addWidget(self.label_2)
        self.spinBoxDecim = QtGui.QSpinBox(self.layoutWidget)
        self.spinBoxDecim.setProperty("value", 3)
        self.spinBoxDecim.setObjectName(_fromUtf8("spinBoxDecim"))
        self.horizontalLayout_8.addWidget(self.spinBoxDecim)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(DialogEpochsTFR)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(DialogEpochsTFR)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogEpochsTFR.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogEpochsTFR.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogEpochsTFR)
        DialogEpochsTFR.setTabOrder(self.scrollArea, self.comboBoxChannels)
        DialogEpochsTFR.setTabOrder(self.comboBoxChannels, self.doubleSpinBoxMinFreq)
        DialogEpochsTFR.setTabOrder(self.doubleSpinBoxMinFreq, self.doubleSpinBoxMaxFreq)
        DialogEpochsTFR.setTabOrder(self.doubleSpinBoxMaxFreq, self.doubleSpinBoxFreqInterval)
        DialogEpochsTFR.setTabOrder(self.doubleSpinBoxFreqInterval, self.spinBoxNcycles)
        DialogEpochsTFR.setTabOrder(self.spinBoxNcycles, self.spinBoxDecim)
        DialogEpochsTFR.setTabOrder(self.spinBoxDecim, self.buttonBox)

    def retranslateUi(self, DialogEpochsTFR):
        DialogEpochsTFR.setWindowTitle(_translate("DialogEpochsTFR", "Meggie - TFR from epochs", None))
        self.groupBoxFrequencies.setTitle(_translate("DialogEpochsTFR", "Frequency window", None))
        self.labelMinFreq.setText(_translate("DialogEpochsTFR", "Minimum frequency:", None))
        self.doubleSpinBoxMinFreq.setSuffix(_translate("DialogEpochsTFR", " Hz", None))
        self.labelMaxFreq.setText(_translate("DialogEpochsTFR", "Maximum frequency:", None))
        self.doubleSpinBoxMaxFreq.setSuffix(_translate("DialogEpochsTFR", " Hz", None))
        self.labelFrequencyInterval.setText(_translate("DialogEpochsTFR", "Frequency interval:", None))
        self.doubleSpinBoxFreqInterval.setSuffix(_translate("DialogEpochsTFR", " Hz", None))
        self.labelNcycles.setText(_translate("DialogEpochsTFR", "Number of cycles:", None))
        self.label_2.setText(_translate("DialogEpochsTFR", "Temporal decim factor:", None))

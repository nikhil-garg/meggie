# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kari/Opinnot/gradu/lahdekoodit/lahdekoodit/meggie_batch/ui/qt4Designer_ui_files/covarianceRawDialog.ui'
#
# Created: Tue Jan 20 19:21:23 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_covarianceRawDialog(object):
    def setupUi(self, covarianceRawDialog):
        covarianceRawDialog.setObjectName(_fromUtf8("covarianceRawDialog"))
        covarianceRawDialog.resize(496, 831)
        self.gridLayout_7 = QtGui.QGridLayout(covarianceRawDialog)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.groupBox = QtGui.QGroupBox(covarianceRawDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.radioButtonSubjectList = QtGui.QRadioButton(self.groupBox)
        self.radioButtonSubjectList.setChecked(True)
        self.radioButtonSubjectList.setObjectName(_fromUtf8("radioButtonSubjectList"))
        self.buttonGroupRawFile = QtGui.QButtonGroup(covarianceRawDialog)
        self.buttonGroupRawFile.setObjectName(_fromUtf8("buttonGroupRawFile"))
        self.buttonGroupRawFile.addButton(self.radioButtonSubjectList)
        self.horizontalLayout_5.addWidget(self.radioButtonSubjectList)
        self.listViewSubjects = QtGui.QListView(self.groupBox)
        self.listViewSubjects.setObjectName(_fromUtf8("listViewSubjects"))
        self.horizontalLayout_5.addWidget(self.listViewSubjects)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.radioButtonElseWhere = QtGui.QRadioButton(self.groupBox)
        self.radioButtonElseWhere.setObjectName(_fromUtf8("radioButtonElseWhere"))
        self.buttonGroupRawFile.addButton(self.radioButtonElseWhere)
        self.horizontalLayout.addWidget(self.radioButtonElseWhere)
        self.lineEditRawFile = QtGui.QLineEdit(self.groupBox)
        self.lineEditRawFile.setEnabled(False)
        self.lineEditRawFile.setObjectName(_fromUtf8("lineEditRawFile"))
        self.horizontalLayout.addWidget(self.lineEditRawFile)
        self.pushButtonBrowse = QtGui.QPushButton(self.groupBox)
        self.pushButtonBrowse.setEnabled(False)
        self.pushButtonBrowse.setObjectName(_fromUtf8("pushButtonBrowse"))
        self.horizontalLayout.addWidget(self.pushButtonBrowse)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout_6.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.pushButtonShowInfo = QtGui.QPushButton(self.groupBox)
        self.pushButtonShowInfo.setObjectName(_fromUtf8("pushButtonShowInfo"))
        self.gridLayout_6.addWidget(self.pushButtonShowInfo, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBoxRejection = QtGui.QGroupBox(covarianceRawDialog)
        self.groupBoxRejection.setObjectName(_fromUtf8("groupBoxRejection"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxRejection)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.frameRejectionPeakToPeak = QtGui.QFrame(self.groupBoxRejection)
        self.frameRejectionPeakToPeak.setEnabled(False)
        self.frameRejectionPeakToPeak.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameRejectionPeakToPeak.setFrameShadow(QtGui.QFrame.Raised)
        self.frameRejectionPeakToPeak.setLineWidth(1)
        self.frameRejectionPeakToPeak.setObjectName(_fromUtf8("frameRejectionPeakToPeak"))
        self.gridLayout = QtGui.QGridLayout(self.frameRejectionPeakToPeak)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelRejections = QtGui.QLabel(self.frameRejectionPeakToPeak)
        self.labelRejections.setObjectName(_fromUtf8("labelRejections"))
        self.gridLayout.addWidget(self.labelRejections, 0, 0, 1, 1)
        self.horizontalLayout_30 = QtGui.QHBoxLayout()
        self.horizontalLayout_30.setObjectName(_fromUtf8("horizontalLayout_30"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_31 = QtGui.QHBoxLayout()
        self.horizontalLayout_31.setObjectName(_fromUtf8("horizontalLayout_31"))
        self.checkBoxGradReject = QtGui.QCheckBox(self.frameRejectionPeakToPeak)
        self.checkBoxGradReject.setObjectName(_fromUtf8("checkBoxGradReject"))
        self.horizontalLayout_31.addWidget(self.checkBoxGradReject)
        self.doubleSpinBoxGradReject = QtGui.QDoubleSpinBox(self.frameRejectionPeakToPeak)
        self.doubleSpinBoxGradReject.setPrefix(_fromUtf8(""))
        self.doubleSpinBoxGradReject.setMaximum(1000000000.0)
        self.doubleSpinBoxGradReject.setProperty("value", 4000.0)
        self.doubleSpinBoxGradReject.setObjectName(_fromUtf8("doubleSpinBoxGradReject"))
        self.horizontalLayout_31.addWidget(self.doubleSpinBoxGradReject)
        self.verticalLayout_7.addLayout(self.horizontalLayout_31)
        self.horizontalLayout_32 = QtGui.QHBoxLayout()
        self.horizontalLayout_32.setObjectName(_fromUtf8("horizontalLayout_32"))
        self.checkBoxEEGReject = QtGui.QCheckBox(self.frameRejectionPeakToPeak)
        self.checkBoxEEGReject.setObjectName(_fromUtf8("checkBoxEEGReject"))
        self.horizontalLayout_32.addWidget(self.checkBoxEEGReject)
        self.doubleSpinBoxEEGReject = QtGui.QDoubleSpinBox(self.frameRejectionPeakToPeak)
        self.doubleSpinBoxEEGReject.setMaximum(1000000000.0)
        self.doubleSpinBoxEEGReject.setProperty("value", 40.0)
        self.doubleSpinBoxEEGReject.setObjectName(_fromUtf8("doubleSpinBoxEEGReject"))
        self.horizontalLayout_32.addWidget(self.doubleSpinBoxEEGReject)
        self.verticalLayout_7.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_30.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_33 = QtGui.QHBoxLayout()
        self.horizontalLayout_33.setObjectName(_fromUtf8("horizontalLayout_33"))
        self.checkBoxMagReject = QtGui.QCheckBox(self.frameRejectionPeakToPeak)
        self.checkBoxMagReject.setObjectName(_fromUtf8("checkBoxMagReject"))
        self.horizontalLayout_33.addWidget(self.checkBoxMagReject)
        self.doubleSpinBoxMagReject = QtGui.QDoubleSpinBox(self.frameRejectionPeakToPeak)
        self.doubleSpinBoxMagReject.setMaximum(1000000000.0)
        self.doubleSpinBoxMagReject.setProperty("value", 4000.0)
        self.doubleSpinBoxMagReject.setObjectName(_fromUtf8("doubleSpinBoxMagReject"))
        self.horizontalLayout_33.addWidget(self.doubleSpinBoxMagReject)
        self.verticalLayout_8.addLayout(self.horizontalLayout_33)
        self.horizontalLayout_34 = QtGui.QHBoxLayout()
        self.horizontalLayout_34.setObjectName(_fromUtf8("horizontalLayout_34"))
        self.checkBoxEOGReject = QtGui.QCheckBox(self.frameRejectionPeakToPeak)
        self.checkBoxEOGReject.setObjectName(_fromUtf8("checkBoxEOGReject"))
        self.horizontalLayout_34.addWidget(self.checkBoxEOGReject)
        self.doubleSpinBoxEOGReject = QtGui.QDoubleSpinBox(self.frameRejectionPeakToPeak)
        self.doubleSpinBoxEOGReject.setMaximum(1000000000.0)
        self.doubleSpinBoxEOGReject.setProperty("value", 250.0)
        self.doubleSpinBoxEOGReject.setObjectName(_fromUtf8("doubleSpinBoxEOGReject"))
        self.horizontalLayout_34.addWidget(self.doubleSpinBoxEOGReject)
        self.verticalLayout_8.addLayout(self.horizontalLayout_34)
        self.horizontalLayout_30.addLayout(self.verticalLayout_8)
        self.gridLayout.addLayout(self.horizontalLayout_30, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frameRejectionPeakToPeak, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelChunkLength = QtGui.QLabel(self.groupBoxRejection)
        self.labelChunkLength.setEnabled(False)
        self.labelChunkLength.setObjectName(_fromUtf8("labelChunkLength"))
        self.horizontalLayout_2.addWidget(self.labelChunkLength)
        self.doubleSpinBoxChunkLength = QtGui.QDoubleSpinBox(self.groupBoxRejection)
        self.doubleSpinBoxChunkLength.setEnabled(False)
        self.doubleSpinBoxChunkLength.setProperty("value", 1.0)
        self.doubleSpinBoxChunkLength.setObjectName(_fromUtf8("doubleSpinBoxChunkLength"))
        self.horizontalLayout_2.addWidget(self.doubleSpinBoxChunkLength)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.frameRejectionFlatness = QtGui.QFrame(self.groupBoxRejection)
        self.frameRejectionFlatness.setEnabled(False)
        self.frameRejectionFlatness.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameRejectionFlatness.setFrameShadow(QtGui.QFrame.Raised)
        self.frameRejectionFlatness.setLineWidth(1)
        self.frameRejectionFlatness.setObjectName(_fromUtf8("frameRejectionFlatness"))
        self.gridLayout_5 = QtGui.QGridLayout(self.frameRejectionFlatness)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.labelRejectionsFlatness = QtGui.QLabel(self.frameRejectionFlatness)
        self.labelRejectionsFlatness.setObjectName(_fromUtf8("labelRejectionsFlatness"))
        self.gridLayout_5.addWidget(self.labelRejectionsFlatness, 0, 0, 1, 1)
        self.horizontalLayout_40 = QtGui.QHBoxLayout()
        self.horizontalLayout_40.setObjectName(_fromUtf8("horizontalLayout_40"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.horizontalLayout_41 = QtGui.QHBoxLayout()
        self.horizontalLayout_41.setObjectName(_fromUtf8("horizontalLayout_41"))
        self.checkBoxFlatGrad = QtGui.QCheckBox(self.frameRejectionFlatness)
        self.checkBoxFlatGrad.setObjectName(_fromUtf8("checkBoxFlatGrad"))
        self.horizontalLayout_41.addWidget(self.checkBoxFlatGrad)
        self.doubleSpinBoxFlatGrad = QtGui.QDoubleSpinBox(self.frameRejectionFlatness)
        self.doubleSpinBoxFlatGrad.setPrefix(_fromUtf8(""))
        self.doubleSpinBoxFlatGrad.setSuffix(_fromUtf8(""))
        self.doubleSpinBoxFlatGrad.setMaximum(1.0)
        self.doubleSpinBoxFlatGrad.setSingleStep(0.01)
        self.doubleSpinBoxFlatGrad.setProperty("value", 0.0)
        self.doubleSpinBoxFlatGrad.setObjectName(_fromUtf8("doubleSpinBoxFlatGrad"))
        self.horizontalLayout_41.addWidget(self.doubleSpinBoxFlatGrad)
        self.verticalLayout_11.addLayout(self.horizontalLayout_41)
        self.horizontalLayout_42 = QtGui.QHBoxLayout()
        self.horizontalLayout_42.setObjectName(_fromUtf8("horizontalLayout_42"))
        self.checkBoxFlatEeg = QtGui.QCheckBox(self.frameRejectionFlatness)
        self.checkBoxFlatEeg.setObjectName(_fromUtf8("checkBoxFlatEeg"))
        self.horizontalLayout_42.addWidget(self.checkBoxFlatEeg)
        self.doubleSpinBoxFlatEEG = QtGui.QDoubleSpinBox(self.frameRejectionFlatness)
        self.doubleSpinBoxFlatEEG.setSuffix(_fromUtf8(""))
        self.doubleSpinBoxFlatEEG.setMaximum(1.0)
        self.doubleSpinBoxFlatEEG.setSingleStep(0.01)
        self.doubleSpinBoxFlatEEG.setProperty("value", 0.0)
        self.doubleSpinBoxFlatEEG.setObjectName(_fromUtf8("doubleSpinBoxFlatEEG"))
        self.horizontalLayout_42.addWidget(self.doubleSpinBoxFlatEEG)
        self.verticalLayout_11.addLayout(self.horizontalLayout_42)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.checkBoxFlatECG = QtGui.QCheckBox(self.frameRejectionFlatness)
        self.checkBoxFlatECG.setObjectName(_fromUtf8("checkBoxFlatECG"))
        self.horizontalLayout_4.addWidget(self.checkBoxFlatECG)
        self.doubleSpinBoxFlatECG = QtGui.QDoubleSpinBox(self.frameRejectionFlatness)
        self.doubleSpinBoxFlatECG.setSuffix(_fromUtf8(""))
        self.doubleSpinBoxFlatECG.setMaximum(1.0)
        self.doubleSpinBoxFlatECG.setSingleStep(0.01)
        self.doubleSpinBoxFlatECG.setProperty("value", 0.0)
        self.doubleSpinBoxFlatECG.setObjectName(_fromUtf8("doubleSpinBoxFlatECG"))
        self.horizontalLayout_4.addWidget(self.doubleSpinBoxFlatECG)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_40.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.horizontalLayout_43 = QtGui.QHBoxLayout()
        self.horizontalLayout_43.setObjectName(_fromUtf8("horizontalLayout_43"))
        self.checkBoxFlatMag = QtGui.QCheckBox(self.frameRejectionFlatness)
        self.checkBoxFlatMag.setObjectName(_fromUtf8("checkBoxFlatMag"))
        self.horizontalLayout_43.addWidget(self.checkBoxFlatMag)
        self.doubleSpinBoxFlatMag = QtGui.QDoubleSpinBox(self.frameRejectionFlatness)
        self.doubleSpinBoxFlatMag.setSuffix(_fromUtf8(""))
        self.doubleSpinBoxFlatMag.setMaximum(1.0)
        self.doubleSpinBoxFlatMag.setSingleStep(0.01)
        self.doubleSpinBoxFlatMag.setProperty("value", 0.0)
        self.doubleSpinBoxFlatMag.setObjectName(_fromUtf8("doubleSpinBoxFlatMag"))
        self.horizontalLayout_43.addWidget(self.doubleSpinBoxFlatMag)
        self.verticalLayout_12.addLayout(self.horizontalLayout_43)
        self.horizontalLayout_44 = QtGui.QHBoxLayout()
        self.horizontalLayout_44.setObjectName(_fromUtf8("horizontalLayout_44"))
        self.checkBoxFlatEOG = QtGui.QCheckBox(self.frameRejectionFlatness)
        self.checkBoxFlatEOG.setObjectName(_fromUtf8("checkBoxFlatEOG"))
        self.horizontalLayout_44.addWidget(self.checkBoxFlatEOG)
        self.doubleSpinBoxFlatEOG = QtGui.QDoubleSpinBox(self.frameRejectionFlatness)
        self.doubleSpinBoxFlatEOG.setSuffix(_fromUtf8(""))
        self.doubleSpinBoxFlatEOG.setMaximum(1.0)
        self.doubleSpinBoxFlatEOG.setSingleStep(0.01)
        self.doubleSpinBoxFlatEOG.setProperty("value", 0.0)
        self.doubleSpinBoxFlatEOG.setObjectName(_fromUtf8("doubleSpinBoxFlatEOG"))
        self.horizontalLayout_44.addWidget(self.doubleSpinBoxFlatEOG)
        self.verticalLayout_12.addLayout(self.horizontalLayout_44)
        self.horizontalLayout_40.addLayout(self.verticalLayout_12)
        self.gridLayout_5.addLayout(self.horizontalLayout_40, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frameRejectionFlatness, 3, 0, 1, 1)
        self.checkBoxRejection = QtGui.QCheckBox(self.groupBoxRejection)
        self.checkBoxRejection.setObjectName(_fromUtf8("checkBoxRejection"))
        self.gridLayout_2.addWidget(self.checkBoxRejection, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBoxRejection, 2, 0, 1, 1)
        self.groupBoxIncludeChannels = QtGui.QGroupBox(covarianceRawDialog)
        self.groupBoxIncludeChannels.setObjectName(_fromUtf8("groupBoxIncludeChannels"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBoxIncludeChannels)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioButtonIncludeAll = QtGui.QRadioButton(self.groupBoxIncludeChannels)
        self.radioButtonIncludeAll.setChecked(True)
        self.radioButtonIncludeAll.setObjectName(_fromUtf8("radioButtonIncludeAll"))
        self.buttonGroupIncludeChannels = QtGui.QButtonGroup(covarianceRawDialog)
        self.buttonGroupIncludeChannels.setObjectName(_fromUtf8("buttonGroupIncludeChannels"))
        self.buttonGroupIncludeChannels.addButton(self.radioButtonIncludeAll)
        self.verticalLayout.addWidget(self.radioButtonIncludeAll)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.radioButtonIncludeList = QtGui.QRadioButton(self.groupBoxIncludeChannels)
        self.radioButtonIncludeList.setObjectName(_fromUtf8("radioButtonIncludeList"))
        self.buttonGroupIncludeChannels.addButton(self.radioButtonIncludeList)
        self.horizontalLayout_3.addWidget(self.radioButtonIncludeList)
        self.plainTextEditIncludeChannelList = QtGui.QPlainTextEdit(self.groupBoxIncludeChannels)
        self.plainTextEditIncludeChannelList.setEnabled(False)
        self.plainTextEditIncludeChannelList.setObjectName(_fromUtf8("plainTextEditIncludeChannelList"))
        self.horizontalLayout_3.addWidget(self.plainTextEditIncludeChannelList)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBoxIncludeChannels, 3, 0, 1, 1)
        self.groupBoxStartEnd = QtGui.QGroupBox(covarianceRawDialog)
        self.groupBoxStartEnd.setObjectName(_fromUtf8("groupBoxStartEnd"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBoxStartEnd)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.labelBeginTime = QtGui.QLabel(self.groupBoxStartEnd)
        self.labelBeginTime.setObjectName(_fromUtf8("labelBeginTime"))
        self.gridLayout_4.addWidget(self.labelBeginTime, 0, 0, 1, 1)
        self.doubleSpinBoxStartTime = QtGui.QDoubleSpinBox(self.groupBoxStartEnd)
        self.doubleSpinBoxStartTime.setPrefix(_fromUtf8(""))
        self.doubleSpinBoxStartTime.setObjectName(_fromUtf8("doubleSpinBoxStartTime"))
        self.gridLayout_4.addWidget(self.doubleSpinBoxStartTime, 0, 1, 1, 1)
        self.labelEndTime = QtGui.QLabel(self.groupBoxStartEnd)
        self.labelEndTime.setObjectName(_fromUtf8("labelEndTime"))
        self.gridLayout_4.addWidget(self.labelEndTime, 1, 0, 1, 1)
        self.doubleSpinBoxEndTime = QtGui.QDoubleSpinBox(self.groupBoxStartEnd)
        self.doubleSpinBoxEndTime.setObjectName(_fromUtf8("doubleSpinBoxEndTime"))
        self.gridLayout_4.addWidget(self.doubleSpinBoxEndTime, 1, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBoxStartEnd, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(covarianceRawDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_7.addWidget(self.buttonBox, 4, 0, 1, 1)

        self.retranslateUi(covarianceRawDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), covarianceRawDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), covarianceRawDialog.reject)
        QtCore.QObject.connect(self.radioButtonIncludeList, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.plainTextEditIncludeChannelList.setEnabled)
        QtCore.QObject.connect(self.checkBoxRejection, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.labelChunkLength.setEnabled)
        QtCore.QObject.connect(self.checkBoxRejection, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.doubleSpinBoxChunkLength.setEnabled)
        QtCore.QObject.connect(self.checkBoxRejection, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.frameRejectionPeakToPeak.setEnabled)
        QtCore.QObject.connect(self.checkBoxRejection, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.frameRejectionFlatness.setEnabled)
        QtCore.QObject.connect(self.radioButtonSubjectList, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.listViewSubjects.setEnabled)
        QtCore.QObject.connect(self.radioButtonElseWhere, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEditRawFile.setEnabled)
        QtCore.QObject.connect(self.radioButtonElseWhere, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.pushButtonBrowse.setEnabled)
        QtCore.QObject.connect(self.radioButtonElseWhere, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.listViewSubjects.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(covarianceRawDialog)

    def retranslateUi(self, covarianceRawDialog):
        covarianceRawDialog.setWindowTitle(_translate("covarianceRawDialog", "Dialog", None))
        self.groupBox.setTitle(_translate("covarianceRawDialog", "Use raw file from:", None))
        self.radioButtonSubjectList.setText(_translate("covarianceRawDialog", "subject list\n"
"(working file)", None))
        self.radioButtonElseWhere.setText(_translate("covarianceRawDialog", "elsewhere:", None))
        self.pushButtonBrowse.setText(_translate("covarianceRawDialog", "Browse...", None))
        self.pushButtonShowInfo.setText(_translate("covarianceRawDialog", "Show info for the selected raw file (will take a while)", None))
        self.groupBoxRejection.setTitle(_translate("covarianceRawDialog", "Rejection", None))
        self.labelRejections.setText(_translate("covarianceRawDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Reject chunks of data based on peak to peak amplitude:</span></p></body></html>", None))
        self.checkBoxGradReject.setText(_translate("covarianceRawDialog", "grad.", None))
        self.doubleSpinBoxGradReject.setSuffix(_translate("covarianceRawDialog", " fT/cm", None))
        self.checkBoxEEGReject.setText(_translate("covarianceRawDialog", "EEG", None))
        self.doubleSpinBoxEEGReject.setSuffix(_translate("covarianceRawDialog", " uV", None))
        self.checkBoxMagReject.setText(_translate("covarianceRawDialog", "mag.", None))
        self.doubleSpinBoxMagReject.setSuffix(_translate("covarianceRawDialog", " fT", None))
        self.checkBoxEOGReject.setText(_translate("covarianceRawDialog", "EOG", None))
        self.doubleSpinBoxEOGReject.setSuffix(_translate("covarianceRawDialog", " uV", None))
        self.labelChunkLength.setText(_translate("covarianceRawDialog", "Chunk length for rejection (tstep):", None))
        self.doubleSpinBoxChunkLength.setSuffix(_translate("covarianceRawDialog", " s", None))
        self.labelRejectionsFlatness.setText(_translate("covarianceRawDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Reject chunks of data based on signal flatness:</span></p></body></html>", None))
        self.checkBoxFlatGrad.setText(_translate("covarianceRawDialog", "grad.", None))
        self.checkBoxFlatEeg.setText(_translate("covarianceRawDialog", "EEG", None))
        self.checkBoxFlatECG.setText(_translate("covarianceRawDialog", "ECG", None))
        self.checkBoxFlatMag.setText(_translate("covarianceRawDialog", "mag.", None))
        self.checkBoxFlatEOG.setText(_translate("covarianceRawDialog", "EOG", None))
        self.checkBoxRejection.setText(_translate("covarianceRawDialog", "Reject signals based on parameters below", None))
        self.groupBoxIncludeChannels.setTitle(_translate("covarianceRawDialog", "Included channels:", None))
        self.radioButtonIncludeAll.setText(_translate("covarianceRawDialog", "All except bad", None))
        self.radioButtonIncludeList.setText(_translate("covarianceRawDialog", "Only the following:", None))
        self.plainTextEditIncludeChannelList.setPlainText(_translate("covarianceRawDialog", "***Problem: input to mne method is by channel indexes (0, 1 etc.), but user input should be by channel names (MEG1331 etc.)***", None))
        self.groupBoxStartEnd.setTitle(_translate("covarianceRawDialog", "Time interval:", None))
        self.labelBeginTime.setText(_translate("covarianceRawDialog", "Beginning of time interval (seconds from start):", None))
        self.doubleSpinBoxStartTime.setSuffix(_translate("covarianceRawDialog", " s", None))
        self.labelEndTime.setText(_translate("covarianceRawDialog", "End of time interval (seconds from start):", None))
        self.doubleSpinBoxEndTime.setSuffix(_translate("covarianceRawDialog", " s", None))


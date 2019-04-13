# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer_ui_files/linearSourceEstimateDialogUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_linearSourceEstimateDialog(object):
    def setupUi(self, linearSourceEstimateDialog):
        linearSourceEstimateDialog.setObjectName("linearSourceEstimateDialog")
        linearSourceEstimateDialog.resize(587, 540)
        linearSourceEstimateDialog.setModal(True)
        self.formLayout_3 = QtWidgets.QFormLayout(linearSourceEstimateDialog)
        self.formLayout_3.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName("formLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelSourceEstimateName = QtWidgets.QLabel(linearSourceEstimateDialog)
        self.labelSourceEstimateName.setObjectName("labelSourceEstimateName")
        self.horizontalLayout_6.addWidget(self.labelSourceEstimateName)
        self.lineEditSourceEstimateName = QtWidgets.QLineEdit(linearSourceEstimateDialog)
        self.lineEditSourceEstimateName.setObjectName("lineEditSourceEstimateName")
        self.horizontalLayout_6.addWidget(self.lineEditSourceEstimateName)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelBasedOn = QtWidgets.QLabel(linearSourceEstimateDialog)
        self.labelBasedOn.setObjectName("labelBasedOn")
        self.horizontalLayout.addWidget(self.labelBasedOn)
        self.lineEditBasedOn = QtWidgets.QLineEdit(linearSourceEstimateDialog)
        self.lineEditBasedOn.setEnabled(False)
        self.lineEditBasedOn.setObjectName("lineEditBasedOn")
        self.horizontalLayout.addWidget(self.lineEditBasedOn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.labelData = QtWidgets.QLabel(linearSourceEstimateDialog)
        self.labelData.setObjectName("labelData")
        self.horizontalLayout_8.addWidget(self.labelData)
        self.lineEditData = QtWidgets.QLineEdit(linearSourceEstimateDialog)
        self.lineEditData.setEnabled(False)
        self.lineEditData.setObjectName("lineEditData")
        self.horizontalLayout_8.addWidget(self.lineEditData)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.verticalLayout)
        self.inverseOperatorParameters = QtWidgets.QGroupBox(linearSourceEstimateDialog)
        self.inverseOperatorParameters.setObjectName("inverseOperatorParameters")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.inverseOperatorParameters)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.labelCovariance = QtWidgets.QLabel(self.inverseOperatorParameters)
        self.labelCovariance.setObjectName("labelCovariance")
        self.horizontalLayout_9.addWidget(self.labelCovariance)
        self.comboBoxCovariance = QtWidgets.QComboBox(self.inverseOperatorParameters)
        self.comboBoxCovariance.setObjectName("comboBoxCovariance")
        self.horizontalLayout_9.addWidget(self.comboBoxCovariance)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelLoose = QtWidgets.QLabel(self.inverseOperatorParameters)
        self.labelLoose.setObjectName("labelLoose")
        self.horizontalLayout_2.addWidget(self.labelLoose)
        self.doubleSpinBoxLoose = QtWidgets.QDoubleSpinBox(self.inverseOperatorParameters)
        self.doubleSpinBoxLoose.setMaximum(1.0)
        self.doubleSpinBoxLoose.setSingleStep(0.05)
        self.doubleSpinBoxLoose.setProperty("value", 0.2)
        self.doubleSpinBoxLoose.setObjectName("doubleSpinBoxLoose")
        self.horizontalLayout_2.addWidget(self.doubleSpinBoxLoose)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelDepth = QtWidgets.QLabel(self.inverseOperatorParameters)
        self.labelDepth.setObjectName("labelDepth")
        self.horizontalLayout_3.addWidget(self.labelDepth)
        self.doubleSpinBoxDepth = QtWidgets.QDoubleSpinBox(self.inverseOperatorParameters)
        self.doubleSpinBoxDepth.setMaximum(1.0)
        self.doubleSpinBoxDepth.setSingleStep(0.05)
        self.doubleSpinBoxDepth.setProperty("value", 0.8)
        self.doubleSpinBoxDepth.setObjectName("doubleSpinBoxDepth")
        self.horizontalLayout_3.addWidget(self.doubleSpinBoxDepth)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.inverseOperatorParameters)
        self.buttonBox = QtWidgets.QDialogButtonBox(linearSourceEstimateDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.groupBoxStcParameters = QtWidgets.QGroupBox(linearSourceEstimateDialog)
        self.groupBoxStcParameters.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBoxStcParameters.setObjectName("groupBoxStcParameters")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxStcParameters)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelLambda = QtWidgets.QLabel(self.groupBoxStcParameters)
        self.labelLambda.setObjectName("labelLambda")
        self.horizontalLayout_4.addWidget(self.labelLambda)
        self.doubleSpinBoxLambda = QtWidgets.QDoubleSpinBox(self.groupBoxStcParameters)
        self.doubleSpinBoxLambda.setSingleStep(0.1)
        self.doubleSpinBoxLambda.setProperty("value", 0.1)
        self.doubleSpinBoxLambda.setObjectName("doubleSpinBoxLambda")
        self.horizontalLayout_4.addWidget(self.doubleSpinBoxLambda)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelMethod = QtWidgets.QLabel(self.groupBoxStcParameters)
        self.labelMethod.setObjectName("labelMethod")
        self.horizontalLayout_5.addWidget(self.labelMethod)
        self.comboBoxMethod = QtWidgets.QComboBox(self.groupBoxStcParameters)
        self.comboBoxMethod.setObjectName("comboBoxMethod")
        self.comboBoxMethod.addItem("")
        self.comboBoxMethod.addItem("")
        self.comboBoxMethod.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBoxMethod)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.groupBoxStcParameters)
        self.groupBoxTimeParameters = QtWidgets.QGroupBox(linearSourceEstimateDialog)
        self.groupBoxTimeParameters.setEnabled(False)
        self.groupBoxTimeParameters.setObjectName("groupBoxTimeParameters")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxTimeParameters)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.labelStart = QtWidgets.QLabel(self.groupBoxTimeParameters)
        self.labelStart.setObjectName("labelStart")
        self.horizontalLayout_11.addWidget(self.labelStart)
        self.doubleSpinBoxStart = QtWidgets.QDoubleSpinBox(self.groupBoxTimeParameters)
        self.doubleSpinBoxStart.setEnabled(False)
        self.doubleSpinBoxStart.setMaximum(9999.0)
        self.doubleSpinBoxStart.setObjectName("doubleSpinBoxStart")
        self.horizontalLayout_11.addWidget(self.doubleSpinBoxStart)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.labelEnd = QtWidgets.QLabel(self.groupBoxTimeParameters)
        self.labelEnd.setObjectName("labelEnd")
        self.horizontalLayout_10.addWidget(self.labelEnd)
        self.doubleSpinBoxEnd = QtWidgets.QDoubleSpinBox(self.groupBoxTimeParameters)
        self.doubleSpinBoxEnd.setEnabled(False)
        self.doubleSpinBoxEnd.setMaximum(9999.0)
        self.doubleSpinBoxEnd.setObjectName("doubleSpinBoxEnd")
        self.horizontalLayout_10.addWidget(self.doubleSpinBoxEnd)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.groupBoxTimeParameters)

        self.retranslateUi(linearSourceEstimateDialog)
        self.buttonBox.accepted.connect(linearSourceEstimateDialog.accept)
        self.buttonBox.rejected.connect(linearSourceEstimateDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(linearSourceEstimateDialog)

    def retranslateUi(self, linearSourceEstimateDialog):
        _translate = QtCore.QCoreApplication.translate
        linearSourceEstimateDialog.setWindowTitle(_translate("linearSourceEstimateDialog", "Create new linear source estimate"))
        self.labelSourceEstimateName.setText(_translate("linearSourceEstimateDialog", "Source estimate name:"))
        self.labelBasedOn.setText(_translate("linearSourceEstimateDialog", "Based on forward solution:"))
        self.labelData.setText(_translate("linearSourceEstimateDialog", "Based on dataset:"))
        self.inverseOperatorParameters.setTitle(_translate("linearSourceEstimateDialog", "Inverse operator parameters:"))
        self.labelCovariance.setText(_translate("linearSourceEstimateDialog", "Noise covariance:"))
        self.labelLoose.setText(_translate("linearSourceEstimateDialog", "Loose:"))
        self.labelDepth.setText(_translate("linearSourceEstimateDialog", "Depth:"))
        self.groupBoxStcParameters.setTitle(_translate("linearSourceEstimateDialog", "Source estimate parameters:"))
        self.labelLambda.setText(_translate("linearSourceEstimateDialog", "Regularization parameter:"))
        self.labelMethod.setText(_translate("linearSourceEstimateDialog", "Method:"))
        self.comboBoxMethod.setItemText(0, _translate("linearSourceEstimateDialog", "dSPM"))
        self.comboBoxMethod.setItemText(1, _translate("linearSourceEstimateDialog", "MNE"))
        self.comboBoxMethod.setItemText(2, _translate("linearSourceEstimateDialog", "sLORETA"))
        self.groupBoxTimeParameters.setTitle(_translate("linearSourceEstimateDialog", "Time parameters (only for raw data)"))
        self.labelStart.setText(_translate("linearSourceEstimateDialog", "Start:"))
        self.labelEnd.setText(_translate("linearSourceEstimateDialog", "End:"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'urscape_hub_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_urscape_hub_form(object):
    def setupUi(self, urscape_hub_form):
        urscape_hub_form.setObjectName("urscape_hub_form")
        urscape_hub_form.setWindowModality(QtCore.Qt.ApplicationModal)
        urscape_hub_form.setEnabled(True)
        urscape_hub_form.resize(531, 364)
        urscape_hub_form.setMouseTracking(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(urscape_hub_form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.CboGrid = QgsMapLayerComboBox(urscape_hub_form)
        self.CboGrid.setShowCrs(True)
        self.CboGrid.setObjectName("CboGrid")
        self.gridLayout.addWidget(self.CboGrid, 1, 0, 1, 2)
        self.status = QtWidgets.QProgressBar(urscape_hub_form)
        self.status.setProperty("value", 24)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.status, 9, 0, 1, 2)
        self.LblOutput = QtWidgets.QLabel(urscape_hub_form)
        self.LblOutput.setObjectName("LblOutput")
        self.gridLayout.addWidget(self.LblOutput, 6, 0, 1, 2)
        self.LblHub = QtWidgets.QLabel(urscape_hub_form)
        self.LblHub.setObjectName("LblHub")
        self.gridLayout.addWidget(self.LblHub, 2, 0, 1, 2)
        self.CboHub = QgsMapLayerComboBox(urscape_hub_form)
        self.CboHub.setShowCrs(True)
        self.CboHub.setObjectName("CboHub")
        self.gridLayout.addWidget(self.CboHub, 3, 0, 1, 2)
        self.LblGridLayer = QtWidgets.QLabel(urscape_hub_form)
        self.LblGridLayer.setObjectName("LblGridLayer")
        self.gridLayout.addWidget(self.LblGridLayer, 0, 0, 1, 2)
        self.LblStatus = QtWidgets.QLabel(urscape_hub_form)
        self.LblStatus.setText("")
        self.LblStatus.setObjectName("LblStatus")
        self.gridLayout.addWidget(self.LblStatus, 8, 0, 1, 2)
        self.output_file_name = QgsFileWidget(urscape_hub_form)
        self.output_file_name.setObjectName("output_file_name")
        self.gridLayout.addWidget(self.output_file_name, 7, 0, 1, 2)
        self.CboHubAttribute = QgsFieldComboBox(urscape_hub_form)
        self.CboHubAttribute.setObjectName("CboHubAttribute")
        self.gridLayout.addWidget(self.CboHubAttribute, 5, 0, 1, 2)
        self.LblHubAttribute = QtWidgets.QLabel(urscape_hub_form)
        self.LblHubAttribute.setObjectName("LblHubAttribute")
        self.gridLayout.addWidget(self.LblHubAttribute, 4, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.BtnApplyClose = QtWidgets.QDialogButtonBox(urscape_hub_form)
        self.BtnApplyClose.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Close)
        self.BtnApplyClose.setObjectName("BtnApplyClose")
        self.verticalLayout.addWidget(self.BtnApplyClose)

        self.retranslateUi(urscape_hub_form)
        self.BtnApplyClose.accepted.connect(urscape_hub_form.accept)
        self.BtnApplyClose.rejected.connect(urscape_hub_form.reject)
        QtCore.QMetaObject.connectSlotsByName(urscape_hub_form)

    def retranslateUi(self, urscape_hub_form):
        _translate = QtCore.QCoreApplication.translate
        urscape_hub_form.setWindowTitle(_translate("urscape_hub_form", "Hub Distance"))
        self.LblOutput.setText(_translate("urscape_hub_form", "Output"))
        self.LblHub.setText(_translate("urscape_hub_form", "Hub Layer"))
        self.LblGridLayer.setText(_translate("urscape_hub_form", "Grid Layer"))
        self.LblHubAttribute.setText(_translate("urscape_hub_form", "Hub Layer Attribute"))

from qgsfieldcombobox import QgsFieldComboBox
from qgsfilewidget import QgsFileWidget
from qgsmaplayercombobox import QgsMapLayerComboBox

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    urscape_hub_form = QtWidgets.QDialog()
    ui = Ui_urscape_hub_form()
    ui.setupUi(urscape_hub_form)
    urscape_hub_form.show()
    sys.exit(app.exec_())


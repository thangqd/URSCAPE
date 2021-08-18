# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'urscape_build_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_urscape_build_form(object):
    def setupUi(self, urscape_build_form):
        urscape_build_form.setObjectName("urscape_build_form")
        urscape_build_form.setWindowModality(QtCore.Qt.ApplicationModal)
        urscape_build_form.setEnabled(True)
        urscape_build_form.resize(531, 364)
        urscape_build_form.setMouseTracking(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(urscape_build_form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.LblStatus = QtWidgets.QLabel(urscape_build_form)
        self.LblStatus.setText("")
        self.LblStatus.setObjectName("LblStatus")
        self.gridLayout.addWidget(self.LblStatus, 8, 0, 1, 2)
        self.status = QtWidgets.QProgressBar(urscape_build_form)
        self.status.setProperty("value", 24)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.status, 9, 0, 1, 2)
        self.CboGrid = QgsMapLayerComboBox(urscape_build_form)
        self.CboGrid.setProperty("showCrs", True)
        self.CboGrid.setObjectName("CboGrid")
        self.gridLayout.addWidget(self.CboGrid, 1, 0, 1, 2)
        self.CboHouse = QgsMapLayerComboBox(urscape_build_form)
        self.CboHouse.setProperty("showCrs", True)
        self.CboHouse.setObjectName("CboHouse")
        self.gridLayout.addWidget(self.CboHouse, 3, 0, 1, 2)
        self.LblGrid = QtWidgets.QLabel(urscape_build_form)
        self.LblGrid.setObjectName("LblGrid")
        self.gridLayout.addWidget(self.LblGrid, 0, 0, 1, 2)
        self.LblHouse = QtWidgets.QLabel(urscape_build_form)
        self.LblHouse.setObjectName("LblHouse")
        self.gridLayout.addWidget(self.LblHouse, 2, 0, 1, 2)
        self.LblOutput = QtWidgets.QLabel(urscape_build_form)
        self.LblOutput.setObjectName("LblOutput")
        self.gridLayout.addWidget(self.LblOutput, 6, 0, 1, 2)
        self.LblFloor = QtWidgets.QLabel(urscape_build_form)
        self.LblFloor.setObjectName("LblFloor")
        self.gridLayout.addWidget(self.LblFloor, 4, 0, 1, 2)
        self.output_file_name = QgsFileWidget(urscape_build_form)
        self.output_file_name.setObjectName("output_file_name")
        self.gridLayout.addWidget(self.output_file_name, 7, 0, 1, 2)
        self.CboFloor = QgsFieldComboBox(urscape_build_form)
        self.CboFloor.setObjectName("CboFloor")
        self.gridLayout.addWidget(self.CboFloor, 5, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.BtnApplyClose = QtWidgets.QDialogButtonBox(urscape_build_form)
        self.BtnApplyClose.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Close)
        self.BtnApplyClose.setObjectName("BtnApplyClose")
        self.verticalLayout.addWidget(self.BtnApplyClose)

        self.retranslateUi(urscape_build_form)
        self.BtnApplyClose.accepted.connect(urscape_build_form.accept)
        self.BtnApplyClose.rejected.connect(urscape_build_form.reject)
        QtCore.QMetaObject.connectSlotsByName(urscape_build_form)

    def retranslateUi(self, urscape_build_form):
        _translate = QtCore.QCoreApplication.translate
        urscape_build_form.setWindowTitle(_translate("urscape_build_form", "Building Area per Grid Cell"))
        self.LblGrid.setText(_translate("urscape_build_form", "Grid Layer (Polygon)"))
        self.LblHouse.setText(_translate("urscape_build_form", "House Layer (Polygon)"))
        self.LblOutput.setText(_translate("urscape_build_form", "Output"))
        self.LblFloor.setText(_translate("urscape_build_form", "Floor Field"))

from qgsfieldcombobox import QgsFieldComboBox
from qgsfilewidget import QgsFileWidget
from qgsmaplayercombobox import QgsMapLayerComboBox

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    urscape_build_form = QtWidgets.QDialog()
    ui = Ui_urscape_build_form()
    ui.setupUi(urscape_build_form)
    urscape_build_form.show()
    sys.exit(app.exec_())


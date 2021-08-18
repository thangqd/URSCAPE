# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'urscape_pop_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_urscape_pop_form(object):
    def setupUi(self, urscape_pop_form):
        urscape_pop_form.setObjectName("urscape_pop_form")
        urscape_pop_form.setWindowModality(QtCore.Qt.ApplicationModal)
        urscape_pop_form.setEnabled(True)
        urscape_pop_form.resize(531, 374)
        urscape_pop_form.setMouseTracking(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(urscape_pop_form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.LblDistrictPop = QtWidgets.QLabel(urscape_pop_form)
        self.LblDistrictPop.setObjectName("LblDistrictPop")
        self.gridLayout.addWidget(self.LblDistrictPop, 2, 0, 1, 2)
        self.LblDistrict = QtWidgets.QLabel(urscape_pop_form)
        self.LblDistrict.setObjectName("LblDistrict")
        self.gridLayout.addWidget(self.LblDistrict, 0, 0, 1, 2)
        self.LblGrid = QtWidgets.QLabel(urscape_pop_form)
        self.LblGrid.setObjectName("LblGrid")
        self.gridLayout.addWidget(self.LblGrid, 4, 0, 1, 2)
        self.LblStatus = QtWidgets.QLabel(urscape_pop_form)
        self.LblStatus.setText("")
        self.LblStatus.setObjectName("LblStatus")
        self.gridLayout.addWidget(self.LblStatus, 8, 0, 1, 2)
        self.CboGrid = QgsMapLayerComboBox(urscape_pop_form)
        self.CboGrid.setProperty("showCrs", True)
        self.CboGrid.setObjectName("CboGrid")
        self.gridLayout.addWidget(self.CboGrid, 5, 0, 1, 2)
        self.CboDistrict = QgsMapLayerComboBox(urscape_pop_form)
        self.CboDistrict.setProperty("showCrs", True)
        self.CboDistrict.setObjectName("CboDistrict")
        self.gridLayout.addWidget(self.CboDistrict, 1, 0, 1, 2)
        self.LblGridBuildingArea = QtWidgets.QLabel(urscape_pop_form)
        self.LblGridBuildingArea.setObjectName("LblGridBuildingArea")
        self.gridLayout.addWidget(self.LblGridBuildingArea, 6, 0, 1, 2)
        self.status = QtWidgets.QProgressBar(urscape_pop_form)
        self.status.setProperty("value", 24)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.status, 9, 0, 1, 2)
        self.CboDistrictPop = QgsFieldComboBox(urscape_pop_form)
        self.CboDistrictPop.setObjectName("CboDistrictPop")
        self.gridLayout.addWidget(self.CboDistrictPop, 3, 0, 1, 2)
        self.CboGridBuildingArea = QgsFieldComboBox(urscape_pop_form)
        self.CboGridBuildingArea.setObjectName("CboGridBuildingArea")
        self.gridLayout.addWidget(self.CboGridBuildingArea, 7, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.BtnApplyClose = QtWidgets.QDialogButtonBox(urscape_pop_form)
        self.BtnApplyClose.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Close)
        self.BtnApplyClose.setObjectName("BtnApplyClose")
        self.verticalLayout.addWidget(self.BtnApplyClose)

        self.retranslateUi(urscape_pop_form)
        self.BtnApplyClose.accepted.connect(urscape_pop_form.accept)
        self.BtnApplyClose.rejected.connect(urscape_pop_form.reject)
        QtCore.QMetaObject.connectSlotsByName(urscape_pop_form)

    def retranslateUi(self, urscape_pop_form):
        _translate = QtCore.QCoreApplication.translate
        urscape_pop_form.setWindowTitle(_translate("urscape_pop_form", "Population per Grid Cell"))
        self.LblDistrictPop.setText(_translate("urscape_pop_form", "District Population Field"))
        self.LblDistrict.setText(_translate("urscape_pop_form", "District Layer (Polygon)"))
        self.LblGrid.setText(_translate("urscape_pop_form", "Grid Layer with building area field (Polygon)"))
        self.LblGridBuildingArea.setText(_translate("urscape_pop_form", "Building Area per Grid Cell Field"))

from qgsfieldcombobox import QgsFieldComboBox
from qgsmaplayercombobox import QgsMapLayerComboBox

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    urscape_pop_form = QtWidgets.QDialog()
    ui = Ui_urscape_pop_form()
    ui.setupUi(urscape_pop_form)
    urscape_pop_form.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'urscape_creategrid_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_urscape_creategrid_form(object):
    def setupUi(self, urscape_creategrid_form):
        urscape_creategrid_form.setObjectName("urscape_creategrid_form")
        urscape_creategrid_form.setWindowModality(QtCore.Qt.ApplicationModal)
        urscape_creategrid_form.setEnabled(True)
        urscape_creategrid_form.resize(534, 440)
        urscape_creategrid_form.setMouseTracking(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(urscape_creategrid_form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.status = QtWidgets.QProgressBar(urscape_creategrid_form)
        self.status.setProperty("value", 24)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.status, 11, 0, 1, 2)
        self.CboInput = QgsMapLayerComboBox(urscape_creategrid_form)
        self.CboInput.setProperty("showCrs", True)
        self.CboInput.setObjectName("CboInput")
        self.gridLayout.addWidget(self.CboInput, 3, 0, 1, 2)
        self.LblStatus = QtWidgets.QLabel(urscape_creategrid_form)
        self.LblStatus.setText("")
        self.LblStatus.setObjectName("LblStatus")
        self.gridLayout.addWidget(self.LblStatus, 10, 0, 1, 2)
        self.LblGridType = QtWidgets.QLabel(urscape_creategrid_form)
        self.LblGridType.setObjectName("LblGridType")
        self.gridLayout.addWidget(self.LblGridType, 0, 0, 1, 1)
        self.LblCellsize = QtWidgets.QLabel(urscape_creategrid_form)
        self.LblCellsize.setObjectName("LblCellsize")
        self.gridLayout.addWidget(self.LblCellsize, 4, 0, 1, 2)
        self.LblLayers = QtWidgets.QLabel(urscape_creategrid_form)
        self.LblLayers.setObjectName("LblLayers")
        self.gridLayout.addWidget(self.LblLayers, 6, 0, 1, 1)
        self.LblGridExtend = QtWidgets.QLabel(urscape_creategrid_form)
        self.LblGridExtend.setObjectName("LblGridExtend")
        self.gridLayout.addWidget(self.LblGridExtend, 2, 0, 1, 2)
        self.lsLayers = QtWidgets.QListWidget(urscape_creategrid_form)
        self.lsLayers.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lsLayers.setSelectionRectVisible(False)
        self.lsLayers.setObjectName("lsLayers")
        self.gridLayout.addWidget(self.lsLayers, 7, 0, 1, 1)
        self.CboGridType = QtWidgets.QComboBox(urscape_creategrid_form)
        self.CboGridType.setObjectName("CboGridType")
        self.CboGridType.addItem("")
        self.CboGridType.addItem("")
        self.CboGridType.addItem("")
        self.CboGridType.addItem("")
        self.CboGridType.addItem("")
        self.gridLayout.addWidget(self.CboGridType, 1, 0, 1, 1)
        self.spinCellsize = QtWidgets.QSpinBox(urscape_creategrid_form)
        self.spinCellsize.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinCellsize.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinCellsize.setMinimum(1)
        self.spinCellsize.setMaximum(1000000)
        self.spinCellsize.setProperty("value", 100)
        self.spinCellsize.setObjectName("spinCellsize")
        self.gridLayout.addWidget(self.spinCellsize, 5, 0, 1, 2)
        self.LblOutput = QtWidgets.QLabel(urscape_creategrid_form)
        self.LblOutput.setObjectName("LblOutput")
        self.gridLayout.addWidget(self.LblOutput, 8, 0, 1, 1)
        self.output_file_name = QgsFileWidget(urscape_creategrid_form)
        self.output_file_name.setObjectName("output_file_name")
        self.gridLayout.addWidget(self.output_file_name, 9, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.BtnApplyClose = QtWidgets.QDialogButtonBox(urscape_creategrid_form)
        self.BtnApplyClose.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Close)
        self.BtnApplyClose.setObjectName("BtnApplyClose")
        self.verticalLayout.addWidget(self.BtnApplyClose)

        self.retranslateUi(urscape_creategrid_form)
        self.BtnApplyClose.accepted.connect(urscape_creategrid_form.accept)
        self.BtnApplyClose.rejected.connect(urscape_creategrid_form.reject)
        QtCore.QMetaObject.connectSlotsByName(urscape_creategrid_form)

    def retranslateUi(self, urscape_creategrid_form):
        _translate = QtCore.QCoreApplication.translate
        urscape_creategrid_form.setWindowTitle(_translate("urscape_creategrid_form", "Create Grid"))
        self.LblGridType.setText(_translate("urscape_creategrid_form", "Grid type"))
        self.LblCellsize.setText(_translate("urscape_creategrid_form", "Cell size (m)"))
        self.LblLayers.setText(_translate("urscape_creategrid_form", "Excluded layers (Polygon)"))
        self.LblGridExtend.setText(_translate("urscape_creategrid_form", "Grid extend"))
        self.lsLayers.setSortingEnabled(True)
        self.CboGridType.setItemText(0, _translate("urscape_creategrid_form", "Point"))
        self.CboGridType.setItemText(1, _translate("urscape_creategrid_form", "Line"))
        self.CboGridType.setItemText(2, _translate("urscape_creategrid_form", "Rectangle (Polygon)"))
        self.CboGridType.setItemText(3, _translate("urscape_creategrid_form", "Diamond (Polygon)"))
        self.CboGridType.setItemText(4, _translate("urscape_creategrid_form", "Hexagon (Polygon)"))
        self.LblOutput.setText(_translate("urscape_creategrid_form", "Output"))

from qgsfilewidget import QgsFileWidget
from qgsmaplayercombobox import QgsMapLayerComboBox

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    urscape_creategrid_form = QtWidgets.QDialog()
    ui = Ui_urscape_creategrid_form()
    ui.setupUi(urscape_creategrid_form)
    urscape_creategrid_form.show()
    sys.exit(app.exec_())


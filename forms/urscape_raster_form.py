# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'urscape_raster_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_urscape_raster_form(object):
    def setupUi(self, urscape_raster_form):
        urscape_raster_form.setObjectName("urscape_raster_form")
        urscape_raster_form.setWindowModality(QtCore.Qt.ApplicationModal)
        urscape_raster_form.setEnabled(True)
        urscape_raster_form.resize(531, 364)
        urscape_raster_form.setMouseTracking(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(urscape_raster_form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.CboGrid = QgsMapLayerComboBox(urscape_raster_form)
        self.CboGrid.setProperty("showCrs", True)
        self.CboGrid.setObjectName("CboGrid")
        self.gridLayout.addWidget(self.CboGrid, 1, 0, 1, 2)
        self.status = QtWidgets.QProgressBar(urscape_raster_form)
        self.status.setProperty("value", 24)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.status, 9, 0, 1, 2)
        self.LblOutput = QtWidgets.QLabel(urscape_raster_form)
        self.LblOutput.setObjectName("LblOutput")
        self.gridLayout.addWidget(self.LblOutput, 6, 0, 1, 2)
        self.LblRaster = QtWidgets.QLabel(urscape_raster_form)
        self.LblRaster.setObjectName("LblRaster")
        self.gridLayout.addWidget(self.LblRaster, 2, 0, 1, 2)
        self.CboRaster = QgsMapLayerComboBox(urscape_raster_form)
        self.CboRaster.setProperty("showCrs", True)
        self.CboRaster.setObjectName("CboRaster")
        self.gridLayout.addWidget(self.CboRaster, 3, 0, 1, 2)
        self.LblGridLayer = QtWidgets.QLabel(urscape_raster_form)
        self.LblGridLayer.setObjectName("LblGridLayer")
        self.gridLayout.addWidget(self.LblGridLayer, 0, 0, 1, 2)
        self.LblStatus = QtWidgets.QLabel(urscape_raster_form)
        self.LblStatus.setText("")
        self.LblStatus.setObjectName("LblStatus")
        self.gridLayout.addWidget(self.LblStatus, 8, 0, 1, 2)
        self.output_file_name = QgsFileWidget(urscape_raster_form)
        self.output_file_name.setObjectName("output_file_name")
        self.gridLayout.addWidget(self.output_file_name, 7, 0, 1, 2)
        self.CboBand = QgsRasterBandComboBox(urscape_raster_form)
        self.CboBand.setObjectName("CboBand")
        self.gridLayout.addWidget(self.CboBand, 5, 0, 1, 2)
        self.LblBand = QtWidgets.QLabel(urscape_raster_form)
        self.LblBand.setObjectName("LblBand")
        self.gridLayout.addWidget(self.LblBand, 4, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.BtnApplyClose = QtWidgets.QDialogButtonBox(urscape_raster_form)
        self.BtnApplyClose.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Close)
        self.BtnApplyClose.setObjectName("BtnApplyClose")
        self.verticalLayout.addWidget(self.BtnApplyClose)

        self.retranslateUi(urscape_raster_form)
        self.BtnApplyClose.accepted.connect(urscape_raster_form.accept)
        self.BtnApplyClose.rejected.connect(urscape_raster_form.reject)
        QtCore.QMetaObject.connectSlotsByName(urscape_raster_form)

    def retranslateUi(self, urscape_raster_form):
        _translate = QtCore.QCoreApplication.translate
        urscape_raster_form.setWindowTitle(_translate("urscape_raster_form", "Raster Value to Grid"))
        self.LblOutput.setText(_translate("urscape_raster_form", "Output"))
        self.LblRaster.setText(_translate("urscape_raster_form", "Raster Layer"))
        self.LblGridLayer.setText(_translate("urscape_raster_form", "Grid Layer (Polygon)"))
        self.LblBand.setText(_translate("urscape_raster_form", "Raster Band"))

from qgsfilewidget import QgsFileWidget
from qgsmaplayercombobox import QgsMapLayerComboBox
from qgsrasterbandcombobox import QgsRasterBandComboBox

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    urscape_raster_form = QtWidgets.QDialog()
    ui = Ui_urscape_raster_form()
    ui.setupUi(urscape_raster_form)
    urscape_raster_form.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-
import sys

try:
    from PyQt4 import QtCore, QtGui
    from manual_base import Ui_ManualDialog
except:
    print "ERROR: No se encuentra pyqt"
    Ui_ManualDialog = object
    pass

import os
import pilas

class VentanaManual(Ui_ManualDialog):

    def setupUi(self, main):
        self.main = main
        Ui_ManualDialog.setupUi(self, main)
        pilas.utils.centrar_ventana(main)
        self.cargar_manual()

    def cargar_manual(self):
        file_path = pilas.utils.obtener_ruta_al_recurso('manual/index.html')
        file_path = os.path.abspath(file_path)

        archivo = open(file_path, "rt")
        contenido = archivo.read().decode('utf8')
        archivo.close()

        base_dir =  QtCore.QUrl.fromLocalFile(file_path)
        self.webView.setHtml(contenido, base_dir)

def main(parent=None, do_raise=False):
    dialog = QtGui.QDialog(parent)
    dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowMinMaxButtonsHint)
    ui = VentanaManual()
    ui.setupUi(dialog)
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    dialog.show()
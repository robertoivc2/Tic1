# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(507, 285)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 101, 16))
        self.serialLista = QComboBox(self.centralwidget)
        self.serialLista.setObjectName(u"serialLista")
        self.serialLista.setGeometry(QRect(50, 20, 111, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 49, 16))
        self.serialConectar = QPushButton(self.centralwidget)
        self.serialConectar.setObjectName(u"serialConectar")
        self.serialConectar.setGeometry(QRect(10, 80, 71, 24))
        self.serialDesconectar = QPushButton(self.centralwidget)
        self.serialDesconectar.setObjectName(u"serialDesconectar")
        self.serialDesconectar.setEnabled(False)
        self.serialDesconectar.setGeometry(QRect(90, 80, 71, 24))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 110, 49, 16))
        self.alertaSonido = QCheckBox(self.centralwidget)
        self.alertaSonido.setObjectName(u"alertaSonido")
        self.alertaSonido.setEnabled(False)
        self.alertaSonido.setGeometry(QRect(10, 130, 76, 20))
        self.alertaLED = QCheckBox(self.centralwidget)
        self.alertaLED.setObjectName(u"alertaLED")
        self.alertaLED.setEnabled(False)
        self.alertaLED.setGeometry(QRect(10, 150, 76, 20))
        self.verticalSlider = QSlider(self.centralwidget)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setEnabled(False)
        self.verticalSlider.setGeometry(QRect(110, 130, 22, 101))
        self.verticalSlider.setMaximum(500)
        self.verticalSlider.setSingleStep(50)
        self.verticalSlider.setValue(300)
        self.verticalSlider.setTracking(False)
        self.verticalSlider.setOrientation(Qt.Vertical)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 110, 49, 16))
        self.alertaPrueba = QPushButton(self.centralwidget)
        self.alertaPrueba.setObjectName(u"alertaPrueba")
        self.alertaPrueba.setEnabled(False)
        self.alertaPrueba.setGeometry(QRect(10, 210, 75, 24))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 0, 49, 16))
        self.sensorLectura = QLabel(self.centralwidget)
        self.sensorLectura.setObjectName(u"sensorLectura")
        self.sensorLectura.setGeometry(QRect(200, 40, 81, 16))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(310, 10, 181, 51))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(170, 0, 20, 241))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.serialActualizar = QPushButton(self.centralwidget)
        self.serialActualizar.setObjectName(u"serialActualizar")
        self.serialActualizar.setGeometry(QRect(10, 50, 151, 24))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(200, 60, 291, 181))
        self.textEdit.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 507, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CONFIGURACI\u00d3N", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Serial", None))
        self.serialConectar.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.serialDesconectar.setText(QCoreApplication.translate("MainWindow", u"Desconectar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Alerta", None))
        self.alertaSonido.setText(QCoreApplication.translate("MainWindow", u"Sonido", None))
        self.alertaLED.setText(QCoreApplication.translate("MainWindow", u"LED", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Umbral", None))
        self.alertaPrueba.setText(QCoreApplication.translate("MainWindow", u"Prueba", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"ESTADO", None))
        self.sensorLectura.setText(QCoreApplication.translate("MainWindow", u"Lectura: 100", None))
        self.serialActualizar.setText(QCoreApplication.translate("MainWindow", u"Actualizar lista", None))
    # retranslateUi


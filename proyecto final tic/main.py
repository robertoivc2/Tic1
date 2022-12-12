import sys
import serial
import serial.tools.list_ports
from PySide6 import QtWidgets, QtCore
from interfaz import Ui_MainWindow

# Cargar interfaz
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    timer = QtCore.QBasicTimer()
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.timer.start(5, self)
    def timerEvent(self, event):
        loop()
    
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()

# Variables
serialInstancia = serial.Serial()
prueba = 0

# Loop
def loop():
    if serialInstancia.is_open:
        try:
            if serialInstancia.in_waiting > 0:
                msg = str(serialInstancia.readline())[2:-5]
                window.sensorLectura.setText("Lectura: " + msg)
        except serial.SerialException:
            printConsola("Error")
            serialDesconectar()

## Lógica de interfaz
def printConsola(texto):
    window.textEdit.append(texto)

# Actualizar lista de puertos serial
def serialActualizar():
    # Guardar que puerto esta seleccionado
    serialSeleccionado = window.serialLista.currentText()
    # Limpiar lista
    window.serialLista.clear()
    # Reconstruir lista
    for p in serial.tools.list_ports.comports():
        if p.pid:
            window.serialLista.addItem(p.device, p)
            # Si el puerto antes seleccionado se vuelve a encontrar, reseleccionarlo
            if p.device == serialSeleccionado:
                window.serialLista.setCurrentIndex(window.serialLista.count() - 1)
serialActualizar()
window.serialActualizar.clicked.connect(serialActualizar)

def serialConectar():
    global serialInstancia
    puerto = window.serialLista.currentData()
    if puerto:
        serialInstancia.port = puerto.device
        serialInstancia.timeout = 2
        try:
            serialInstancia.open()
            interfazConectado()
            printConsola("Conectado a " + puerto.device)
            alertaActualizar()
        except serial.SerialException:
            printConsola("Error")
            serialDesconectar()
window.serialConectar.clicked.connect(serialConectar)

def serialDesconectar():
    serialInstancia.close()
    interfazDesconectado()
    printConsola("Desconectado")
    serialActualizar()
window.serialDesconectar.clicked.connect(serialDesconectar)

# Enviar configuración de alerta a Arduino
def alertaActualizar():
    if serialInstancia.is_open:
        sonido = int(window.alertaSonido.isChecked())
        led = int(window.alertaLED.isChecked())
        umbral = window.verticalSlider.value()
        msg = str(prueba) + str(sonido) + str(led) + str(umbral)
        print(msg)
        serialInstancia.write(msg.encode("utf-8"))
        printConsola("Actualizando configuración")
        printConsola("SND: " + str(sonido) + " LED: " + str(led) + " UMB: " + str(umbral))
window.alertaSonido.clicked.connect(alertaActualizar)
window.alertaLED.clicked.connect(alertaActualizar)
window.verticalSlider.valueChanged.connect(alertaActualizar)

def alertaPrueba():
    global prueba
    prueba = 1
    alertaActualizar()
    prueba = 0
window.alertaPrueba.clicked.connect(alertaPrueba)

# Activar/desactivar elementos de la interfaz
def interfazConectado():
    window.serialConectar.setEnabled(False)
    window.serialLista.setEnabled(False)
    window.serialActualizar.setEnabled(False)
    window.serialDesconectar.setEnabled(True)
    window.alertaLED.setEnabled(True)
    window.alertaSonido.setEnabled(True)
    window.verticalSlider.setEnabled(True)
    window.alertaPrueba.setEnabled(True)
def interfazDesconectado():
    window.serialConectar.setEnabled(True)
    window.serialLista.setEnabled(True)
    window.serialActualizar.setEnabled(True)
    window.serialDesconectar.setEnabled(False)
    window.alertaLED.setEnabled(False)
    window.alertaSonido.setEnabled(False)
    window.verticalSlider.setEnabled(False)
    window.alertaPrueba.setEnabled(False)

window.show()
app.exec()
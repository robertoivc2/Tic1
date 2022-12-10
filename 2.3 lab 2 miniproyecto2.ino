#include "SoftwareSerial.h"

#define   LED   9          //Pin para el LED
#define   VERDE 6
SoftwareSerial ModuloHC05 (10, 11);  //pin RX, pin TX

void setup() {

 Serial.begin(9600);        //Inicializa puerto serie por hard
 ModuloHC05.begin(9600);    //Inicializa puerto serie por soft

 pinMode (LED, OUTPUT);      //Salida
 pinMode (VERDE,OUTPUT);
 digitalWrite (LED, 0);
 digitalWrite (VERDE,0);
}

void loop() {
 char dato;
 if (ModuloHC05.available()) {              //Llega algo por bluetooth?
  dato=ModuloHC05.read();                   //Leer lo que llegÃ³
  Serial.write(dato);                       //Sacarlo a la terminal
  if (dato=='a') digitalWrite (LED, 1);     //Si es "1", prende el LED
  if (dato=='b') digitalWrite (LED, 0);     //Si es "0", apaga el LED
  if (dato=='c') digitalWrite (VERDE, 1);
  if (dato=='d') digitalWrite (VERDE, 0);
 }
           

}

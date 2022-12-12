int prueba = 0;
int sonido = 0;
int led = 0;
int umbral = 300;
int timerPrueba = -1;

int redLed = 11;
int greenLed = 10;
int buzzer = 9;
int smokeA0 = A5;

void setup() {
  pinMode(redLed, OUTPUT);
  pinMode(greenLed, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(smokeA0, INPUT);
  Serial.begin(9600);
}

void loop() {
  // ALERTA (PRENDO O NO LA ALERTA)
  int analogSensor = analogRead(smokeA0);
  // PRUEBA
  if (timerPrueba >= 0) {
    analogSensor = 500;
    timerPrueba -= 1;
  }
  Serial.println(analogSensor);
  if (led) { //LEDS ACTIVADOS
    if (analogSensor > umbral) {
      digitalWrite(redLed, HIGH);
      digitalWrite(greenLed, LOW);
    } else {
      digitalWrite(redLed, LOW);
      digitalWrite(greenLed, HIGH);
    }
  } else {  //LEDS DESACTIVADOS
    digitalWrite(redLed, LOW);
    digitalWrite(greenLed, LOW);
  }
  // SONIDO
  if (sonido && analogSensor > umbral) {
    tone(buzzer, 1000, 200);
  } else {
    noTone(buzzer);
  }
  // CONFIGURACIÓN (RECIBO MENSAJES DE PYTHON)
  if (Serial.available() > 0) {
    char data[10];
    int bytes = Serial.readBytesUntil('\n', data, 10);
    // PRUEBA
    if (data[0] == '1') {prueba = 1; timerPrueba = 30;} else {prueba = 0; timerPrueba = -1;}
    // SONIDO
    if (data[1] == '1') {sonido = 1;} else {sonido = 0;}
    // LED
    if (data[2] == '1') {led = 1;} else {led = 0;}
    // UMBRAL
    umbral = 0;
    for (int i = 0; i < bytes - 3; i++) {
      int numero = data[i+3] - 48;
      umbral += numero * pow(10.0, bytes - 3 - i - 1);
    }
    if (umbral >= 99) {
      umbral += 1;
    }
  }
  delay(100);
}

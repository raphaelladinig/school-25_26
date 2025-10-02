#include "HardwareSerial.h"
#include <Arduino.h>
#include <DallasTemperature.h>
#include <OneWire.h>

#define ONE_WIRE_BUS 2
#define L298N_PIN 5

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

unsigned long previousMillis = 0;
const long interval = 1000;
int power = 0;

void setup() {
    Serial.begin(9600);
    sensors.begin();
    pinMode(L298N_PIN, OUTPUT);
}

void loop() {
    unsigned long currentMillis = millis();
    
    // nach 30 s wird der Motor Controller auf 50 gesetzt
    if (currentMillis >= 30000) {
        power = 50;
        analogWrite(L298N_PIN, power);
    }

    // Wird alle 1000 ms ausgeführt
    if (currentMillis - previousMillis >= interval) {
        previousMillis = currentMillis;

        // Temperatur wird vom Sensor abgefragt
        sensors.requestTemperatures();
        float temperature = sensors.getTempCByIndex(0);

        // Daten werden am Serial Monitor ausgegeben
        Serial.print(currentMillis);
        Serial.print('\t');
        Serial.print(power);
        Serial.print('\t');
        Serial.println(temperature);
    }
}

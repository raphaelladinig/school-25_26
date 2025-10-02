#include "HardwareSerial.h"
#include <Arduino.h>
#include <DallasTemperature.h>
#include <OneWire.h>

#define ONE_WIRE_BUS 2

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

unsigned long previousMillis = 0;
const long interval = 1000;

void setup() {
    Serial.begin(9600);
    sensors.begin();
}

void loop() {
    unsigned long currentMillis = millis();
    
    // Wird alle 1000 ms ausgeführt
    if (currentMillis - previousMillis >= interval) {
        previousMillis = currentMillis;
        
        // Temperatur wird vom Sensor abgefragt
        sensors.requestTemperatures();
        float temperature = sensors.getTempCByIndex(0);
      
        // Daten werden am Serial Monitor ausgegeben
        Serial.print(currentMillis);
        Serial.print('\t');
        Serial.println(temperature);
    }
}

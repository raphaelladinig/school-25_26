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
int power = 55;

void setup() {
    Serial.begin(9600);
    sensors.begin();
    pinMode(L298N_PIN, OUTPUT);
}

void loop() {
    unsigned long currentMillis = millis();

    // Wird alle 1000 ms ausgeführt
    if (currentMillis - previousMillis >= interval) {
        previousMillis = currentMillis;
        
        /*
         * Power wird in alle 1000 ms um 40 erhöt wenn er
         * den Wert 255 überschreitet wird er auf 55 gesetzt
        */ 
        power += 40;
        if (power > 255) {
            power = 55;
        }
        
        // Stärke des Motor Controllers wird gesetzt
        analogWrite(L298N_PIN, power);


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

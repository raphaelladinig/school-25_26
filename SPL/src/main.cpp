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
const double targetTemp = 3;
const double hysterese = 0.2;
int power = 0;
float startTemp = 0;
bool heating = true;

void setup() {
    Serial.begin(9600);
    sensors.begin();
    pinMode(L298N_PIN, OUTPUT);

    sensors.requestTemperatures();
    startTemp = sensors.getTempCByIndex(0);
    Serial.println(startTemp);

    delay(3000);
}

void loop() {
    unsigned long currentMillis = millis();

    if (currentMillis - previousMillis >= interval) {
        sensors.requestTemperatures();
        float temperature = sensors.getTempCByIndex(0);
        float tempDiff = abs(startTemp - temperature);

        if (tempDiff < targetTemp - hysterese) {
            heating = true;
        }

        if (tempDiff < targetTemp + hysterese && heating) {
            power = 50;
        } else {
            power = 0;
            heating = false;
        }

        analogWrite(L298N_PIN, power);
        previousMillis = currentMillis;

        Serial.print(float(currentMillis / (1000.0 * 60.0)));
        Serial.print('\t');
        Serial.print(power);
        Serial.print('\t');
        Serial.println(tempDiff);
    }
}

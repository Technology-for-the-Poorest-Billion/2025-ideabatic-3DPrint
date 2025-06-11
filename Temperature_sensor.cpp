#include "DHT.h"


#define DHTPIN 2    
#define DHTTYPE DHT22    // DHT 22 (AM2302)
#define BUZZER_PIN 8    
int buzzer_state = 0;

unsigned long previousMillis = 0;   
unsigned long elapsedMinutes = 0;  

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);    
  dht.begin();             
  pinMode(BUZZER_PIN, OUTPUT); 
  Serial.println("Timer started.");
}

void loop() {
  float temperature = dht.readTemperature(); // Read temperature in Celsius
  unsigned long currentMillis = millis();
  delay(500); // Wait 2 seconds between measurements

 
  if (currentMillis - previousMillis >= 60000) {
    previousMillis = currentMillis;  // Update the last time marker
    elapsedMinutes++;                // Increment minute counter

    Serial.print("Elapsed time: ");
    Serial.print(elapsedMinutes);
    Serial.println(" minute(s)");
    
    // Print temperature to Serial Monitor
    Serial.print("Temperature: ");
    Serial.print(temperature);
    Serial.println(" °C");
  }



  // Check if reading failed
  if (isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    digitalWrite(BUZZER_PIN, LOW); // Ensure buzzer is off on error
    return;
  }

  
  // Turn buzzer on if temperature > 20 °C
  if (temperature > 10) {
    digitalWrite(BUZZER_PIN, buzzer_state);
    if (buzzer_state == 1){
      buzzer_state = 0;
    } 
    else {
      buzzer_state = 1;
    }
  } else {
    digitalWrite(BUZZER_PIN, LOW);
  }
}

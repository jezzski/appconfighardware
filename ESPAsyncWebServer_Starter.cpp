// I forgot what is the source I used for this code, you can google the code
// Import required libraries
#include "WiFi.h"
#include "ESPAsyncWebServer.h"
#include "SPIFFS.h"

// Replace with your network credentials
const char* ssid = "zanobia";
const char* password = "7202967428";


// Create AsyncWebServer object on port 80
AsyncWebServer server(80);


void setup(){
  // Serial port for debugging purposes
  Serial.begin(9600);

  // Initialize SPIFFS
  if(!SPIFFS.begin(true)){
    Serial.println("An Error has occurred while mounting SPIFFS");
    return;
  }

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }

  // Print ESP32 Local IP Address
  Serial.println(WiFi.localIP());

  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
        request->send(200, "text/plain", "Hello, world");
  });

  // Route for root / web page
  //server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
  //  request->send(SPIFFS, "/html.html","text/html");
 // });
  
  // Route to load style.css file
  //server.on("/NCSU.css", HTTP_GET, [](AsyncWebServerRequest *request){
  //  request->send(SPIFFS, "/NCSU.css", "text/css");
  //});

    // Route to load test.js file
  //server.on("/NCSU.css", HTTP_GET, [](AsyncWebServerRequest *request){
  //  request->send(SPIFFS, "/test.js", "text/javascript");
  //});

  // Start server
  server.begin();
}
 
void loop(){
  
}

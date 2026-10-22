#include <Servo.h>

#define TRIG_PIN 7
#define ECHO_PIN 6
#define SERVO_PIN 9
#define LED_PIN 12
#define BUZZER_PIN 4

#define JOYSTICK_X A0
#define JOYSTICK_Y A1
#define JOYSTICK_SW 2

Servo radarServo;

int angle = 90;
int direction = 1;

bool autoMode = true;

bool lastButtonState = HIGH;
unsigned long lastDebounceTime = 0;

unsigned long lastScanTime = 0;
const unsigned long scanInterval = 120;

float getDistance() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  unsigned long duration = pulseIn(ECHO_PIN, HIGH, 30000);

  if (duration == 0) {
    return -1;
  }

  return duration * 0.0343 / 2.0;
}

void checkAlarm(float distance) {

  if (distance < 0 || distance > 50) {
    digitalWrite(LED_PIN, LOW);
    noTone(BUZZER_PIN);
  }

  else if (distance >= 20) {
    digitalWrite(LED_PIN, HIGH);
    tone(BUZZER_PIN, 1000, 80);
  }

  else {
    digitalWrite(LED_PIN, HIGH);
    tone(BUZZER_PIN, 2000, 150);
  }
}

void checkButton() {
  bool buttonState = digitalRead(JOYSTICK_SW);

  if (buttonState == LOW && lastButtonState == HIGH) {
    if (millis() - lastDebounceTime > 250) {
      autoMode = !autoMode;
      lastDebounceTime = millis();
    }
  }

  lastButtonState = buttonState;
}

void updateServo() {

  if (autoMode) {
    angle += direction * 5;

    if (angle >= 165) {
      angle = 165;
      direction = -1;
    }

    if (angle <= 15) {
      angle = 15;
      direction = 1;
    }
  }

  else {
    int joystickValue = analogRead(JOYSTICK_X);

    if (joystickValue < 400) {
      angle -= 3;
    }

    else if (joystickValue > 600) {
      angle += 3;
    }

    angle = constrain(angle, 15, 165);
  }

  radarServo.write(angle);
}

void setup() {
  Serial.begin(9600);

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);

  pinMode(JOYSTICK_SW, INPUT_PULLUP);

  radarServo.attach(SERVO_PIN);
  radarServo.write(angle);

  delay(1000);
}

void loop() {
  checkButton();

  if (millis() - lastScanTime >= scanInterval) {
    lastScanTime = millis();

    updateServo();

    delay(50);

    float distance = getDistance();

    checkAlarm(distance);

    // Keep Python radar data format unchanged
    Serial.print(angle);
    Serial.print(",");

    if (distance < 0) {
      Serial.println(-1);
    } else {
      Serial.println(distance, 2);
    }
  }
}
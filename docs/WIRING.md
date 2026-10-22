\# 📡 RADAR-X — Hardware Wiring Guide



\## 1. Overview



RADAR-X uses an ELEGOO Mega 2560 microcontroller to control an ultrasonic scanning system.



The hardware includes:



\* Arduino Mega 2560

\* SG90 servo motor

\* HC-SR04 ultrasonic sensor

\* Joystick module

\* Passive buzzer

\* Red LED

\* 220Ω resistor

\* Breadboard and jumper wires



\## 2. Complete Pin Configuration



| Component      | Component Pin   | Arduino Mega              |

| -------------- | --------------- | ------------------------- |

| SG90 Servo     | Signal (Orange) | D9                        |

| SG90 Servo     | Power (Red)     | 5V                        |

| SG90 Servo     | Ground (Brown)  | GND                       |

| HC-SR04        | VCC             | 5V                        |

| HC-SR04        | TRIG            | D7                        |

| HC-SR04        | ECHO            | D6                        |

| HC-SR04        | GND             | GND                       |

| Joystick       | VRx             | A0                        |

| Joystick       | VRy             | A1                        |

| Joystick       | SW              | D2                        |

| Joystick       | +5V             | 5V                        |

| Joystick       | GND             | GND                       |

| Red LED        | Anode (+)       | D12 through 220Ω resistor |

| Red LED        | Cathode (-)     | GND                       |

| Passive Buzzer | Positive (+)    | D4                        |

| Passive Buzzer | Negative (-)    | GND                       |



\## 3. Servo Motor



The SG90 servo rotates the ultrasonic sensor.



It operates within the programmed range of 15°–165°.



The Arduino Servo library controls its position.



\## 4. Ultrasonic Sensor



The HC-SR04 measures the distance between the sensor and nearby objects using ultrasonic sound waves.



The Arduino sends a trigger pulse through D7 and receives the echo through D6.



\## 5. Joystick Module



The joystick provides manual control of the radar.



\* Move left: Rotate servo left.

\* Move right: Rotate servo right.

\* Press joystick button: Switch between AUTO and MANUAL modes.



The joystick button uses `INPUT\_PULLUP`.



\## 6. Proximity Alarm



The red LED and passive buzzer provide distance-based warnings.



| Measured Distance   | LED | Buzzer  |

| ------------------- | --- | ------- |

| Greater than 50 cm  | OFF | OFF     |

| 20–50 cm            | ON  | 1000 Hz |

| Less than 20 cm     | ON  | 2000 Hz |

| Invalid measurement | OFF | OFF     |



\## 7. Power Considerations



The Arduino Mega receives power through USB during development.



The HC-SR04 and joystick use the Arduino's 5V supply.



The SG90 servo can draw significant current, especially when moving under load. If the servo jitters, stalls, or resets the Arduino, stop testing and use a suitable external regulated 5V supply for the servo.



When using an external servo supply, connect its ground to the Arduino ground.



\## 8. Important Safety Notes



\* Disconnect USB power before changing wiring.

\* Always use a current-limiting resistor with the LED.

\* Do not force the servo beyond its mechanical limits.

\* Prevent the rotating sensor from pulling or twisting jumper wires.

\* Check polarity before powering the circuit.

\* Do not connect the MFRC522 RFID module directly to 5V logic without suitable voltage protection.



\## 9. Future Hardware Improvements



Potential additions include:



\* LCD status display

\* Green status LED

\* Adjustable detection threshold

\* NFC-based arming and disarming

\* Dedicated servo power supply

\* Protective enclosure



\*\*Note:\*\* NFC authentication was considered but was not implemented in the current RADAR-X build.




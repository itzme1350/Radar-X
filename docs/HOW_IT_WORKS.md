\# 📡 How RADAR-X Works



\## 1. Project Overview



RADAR-X is an Arduino-based ultrasonic object detection system.



It uses an HC-SR04 ultrasonic sensor mounted on an SG90 servo motor to scan the surrounding environment.



The Arduino Mega 2560 processes sensor measurements and sends data to a computer for real-time visualization.



\## 2. System Architecture



```text

&#x20;       HC-SR04 Ultrasonic Sensor

&#x20;                 |

&#x20;                 v

&#x20;         Arduino Mega 2560

&#x20;                 |

&#x20;      +----------+----------+

&#x20;      |          |          |

&#x20;      v          v          v

&#x20;  SG90 Servo   Joystick   LED/Buzzer

&#x20;      |

&#x20;      v

&#x20;  Scanning Motion



&#x20;       Arduino Mega 2560

&#x20;                 |

&#x20;                 v

&#x20;         USB Serial (9600)

&#x20;                 |

&#x20;                 v

&#x20;          Python Application

&#x20;                 |

&#x20;         +-------+-------+

&#x20;         |               |

&#x20;         v               v

&#x20;    Live Radar        2D Mapping

```



\## 3. Ultrasonic Distance Measurement



The HC-SR04 emits ultrasonic pulses and measures how long the echoes take to return.



Distance is calculated using:



Distance = (Echo Time × Speed of Sound) / 2



The speed of sound is approximately 343 m/s at 20°C.



The division by two accounts for the sound traveling to the object and returning.



\## 4. Servo Motor Control



The SG90 servo rotates the ultrasonic sensor between approximately 15° and 165°.



RADAR-X supports two operating modes:



\### Automatic Mode



The servo continuously sweeps between its programmed angular limits.



\### Manual Mode



The joystick controls the servo's position.



Pressing the joystick button switches between automatic and manual operation.



\## 5. Proximity Detection



The system categorizes valid distance measurements:



| Distance | Response |

|----------|----------|

| Greater than 50 cm | No alarm |

| 20–50 cm | Red LED and 1000 Hz warning |

| Less than 20 cm | Red LED and 2000 Hz warning |

| Invalid measurement | No alarm |



The Arduino controls the buzzer using the `tone()` function.



\## 6. Serial Communication



The Arduino transmits measurements to the computer at 9600 baud.



Each measurement follows this format:



```text

angle,distance

```



Example:



```text

45,120.50

50,85.20

55,30.45

60,-1

```



A distance of `-1` represents an invalid or missing echo.



Python uses the `pyserial` library to receive these measurements.



\## 7. Live Radar Visualization



The `radar.py` application uses Pygame to display:



\- Current scanning angle

\- Measured distance

\- Radar sweep line

\- Detected object points

\- Distance reference rings



\## 8. 2D Environmental Mapping



The `mapping.py` application converts polar measurements into Cartesian coordinates.



The coordinate equations are:



x = distance × cos(angle)



y = distance × sin(angle)



These coordinates are plotted relative to the sensor's position.



The resulting map provides an approximate representation of nearby obstacles.



\## 9. System Limitations



RADAR-X is an ultrasonic scanning system, not electromagnetic radar.



Its limitations include:



\- Limited scanning range

\- Approximate object positioning

\- Ultrasonic reflections and measurement noise

\- No object identification

\- No continuous 360° rotation

\- Possible delays between measurements



The system is intended for educational experimentation.



\## 10. Future Development



Possible improvements include:



\- Automatic object tracking

\- Motion detection

\- Noise filtering

\- Improved mapping algorithms

\- Computer-controlled scanning

\- Data logging

\- NFC-based arming and disarming


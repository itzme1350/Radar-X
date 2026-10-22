\# 📡 RADAR-X

\### Arduino-Based Ultrasonic Radar \& Object Detection System



RADAR-X is an Arduino-based ultrasonic scanning system designed

to detect nearby objects, measure distances, and visualize

the surrounding environment in real time.



The project integrates embedded systems, sensor technology,

motor control, and Python-based data visualization.



\## 🚀 Features



\- 180° ultrasonic scanning system

\- Real-time object detection

\- Distance measurement in centimeters

\- Automatic and manual scanning modes

\- Joystick-controlled servo movement

\- Proximity warning using LED and buzzer

\- Live radar visualization using Python and Pygame

\- 2D environmental mapping

\- Serial communication between Arduino and computer



\## 🛠️ Hardware Components



\- ELEGOO Mega 2560

\- SG90 Servo Motor

\- HC-SR04 Ultrasonic Sensor

\- Joystick Module

\- Passive Buzzer

\- Red LED

\- 220Ω Resistor

\- Breadboard and Jumper Wires

\- USB Cable



\## ⚙️ Pin Configuration



| Component | Arduino Pin |

|-----------|-------------|

| Servo Signal | D9 |

| Ultrasonic TRIG | D7 |

| Ultrasonic ECHO | D6 |

| Red LED | D12 |

| Buzzer | D4 |

| Joystick VRx | A0 |

| Joystick VRy | A1 |

| Joystick SW | D2 |



\## 🧠 How It Works



1\. The Arduino controls an SG90 servo motor.

2\. The servo rotates the HC-SR04 ultrasonic sensor.

3\. The sensor transmits ultrasonic pulses and receives echoes.

4\. The Arduino calculates the distance to nearby objects.

5\. Measurements are transmitted to the computer through USB.

6\. Python receives the data and displays a live radar interface.

7\. The system activates an LED and buzzer when objects are nearby.



\### Distance Calculation



Distance is calculated using:



Distance = (Echo Time × Speed of Sound) / 2



The speed of sound is approximately 0.0343 cm/µs.



\## 🎮 Operating Modes



\### Automatic Mode

The servo continuously scans between 15° and 165°.



\### Manual Mode

The user controls the servo using the joystick.



Pressing the joystick button switches between AUTO and MANUAL.



\## 💻 Software Requirements



\- Arduino IDE

\- Python 3

\- pygame-ce

\- pyserial



Install Python dependencies:



```bash

py -m pip install pygame-ce pyserial

```



\## ▶️ How to Run



1\. Connect the Arduino Mega 2560 to your computer.

2\. Upload `arduino/Radar\_X/Radar\_X.ino` using Arduino IDE.

3\. Verify your Arduino's COM port.

4\. Close Arduino Serial Monitor.

5\. Open Command Prompt.

6\. Navigate to the Python folder:



```cmd

cd python

```



Run the radar visualization:



```cmd

py radar.py

```



Or run the 2D mapping application:



```cmd

py mapping.py

```



Update the COM port in the Python files if necessary.



\## 📁 Project Structure



```text

RADAR-X/

├── README.md

├── arduino/

│   └── Radar\_X/

│       └── Radar\_X.ino

├── python/

│   ├── radar.py

│   └── mapping.py

├── docs/

└── images/

```



\## 📸 Project Gallery



Hardware photographs and demonstration screenshots

will be added in a future update.



\## 🔮 Future Improvements



\- Automatic target tracking

\- Motion detection

\- Sensor noise filtering

\- Advanced environmental mapping

\- Computer-based control station

\- NFC-controlled arming and disarming



\## ⚠️ Limitations



RADAR-X uses ultrasonic sensing rather than radio-frequency radar.



The SG90 servo provides a limited scanning range, and the

HC-SR04 cannot reliably identify objects or people.



This project is intended for educational and experimental use,

not as a safety-critical detection or security system.



\## 👨‍💻 Author



\*\*Hpone Myat\*\*



Computer Engineering — University of Maryland, Baltimore County (UMBC)



\## 📜 License



MIT License


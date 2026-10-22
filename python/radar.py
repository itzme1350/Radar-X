import pygame
import serial
import math
import sys

# CHANGE THIS TO YOUR ARDUINO COM PORT
PORT = "COM3"
BAUD_RATE = 9600

# Connect to Arduino
try:
    arduino = serial.Serial(PORT, BAUD_RATE, timeout=0.01)
except serial.SerialException as error:
    print(f"Cannot connect to Arduino: {error}")
    sys.exit()

pygame.init()

WIDTH = 1000
HEIGHT = 650

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RADAR-X | Ultrasonic Detection System")

clock = pygame.time.Clock()

GREEN = (0, 255, 100)
DARK_GREEN = (0, 100, 40)
RED = (255, 60, 60)
BLACK = (5, 12, 10)
WHITE = (230, 255, 230)

font = pygame.font.SysFont("consolas", 20)
small_font = pygame.font.SysFont("consolas", 15)

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT - 80

RADIUS = 440
MAX_DISTANCE = 200

angle = 90
distance = -1

detections = {}

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read Arduino data
    try:
        line = arduino.readline().decode("utf-8", errors="ignore").strip()

        if "," in line:
            values = line.split(",")

            angle = int(values[0])
            distance = float(values[1])

            if 0 <= angle <= 180:
                if 0 < distance <= MAX_DISTANCE:
                    detections[angle] = distance
                else:
                    detections.pop(angle, None)

    except (ValueError, serial.SerialException):
        pass

    screen.fill(BLACK)

    # Radar distance rings
    for r in range(1, 5):
        radius = int(RADIUS * r / 4)

        pygame.draw.arc(
            screen,
            DARK_GREEN,
            (
                CENTER_X - radius,
                CENTER_Y - radius,
                radius * 2,
                radius * 2,
            ),
            math.pi * 0,
            math.pi,
            1,
        )

    # Angle lines
    for a in range(0, 181, 30):
        rad = math.radians(a)

        x = CENTER_X + RADIUS * math.cos(rad)
        y = CENTER_Y - RADIUS * math.sin(rad)

        pygame.draw.line(
            screen,
            DARK_GREEN,
            (CENTER_X, CENTER_Y),
            (x, y),
            1,
        )

    # Scanning line
    rad = math.radians(angle)

    scan_x = CENTER_X + RADIUS * math.cos(rad)
    scan_y = CENTER_Y - RADIUS * math.sin(rad)

    pygame.draw.line(
        screen,
        GREEN,
        (CENTER_X, CENTER_Y),
        (scan_x, scan_y),
        3,
    )

    # Detected objects
    for detected_angle, detected_distance in detections.items():

        rad = math.radians(detected_angle)

        r = detected_distance / MAX_DISTANCE * RADIUS

        x = CENTER_X + r * math.cos(rad)
        y = CENTER_Y - r * math.sin(rad)

        pygame.draw.circle(
            screen,
            RED,
            (int(x), int(y)),
            5,
        )

    # Text information
    title = font.render("RADAR-X | LIVE ULTRASONIC SCANNER", True, GREEN)
    screen.blit(title, (20, 20))

    angle_text = font.render(f"ANGLE: {angle}°", True, WHITE)
    screen.blit(angle_text, (20, 55))

    if distance > 0:
        distance_text = font.render(
            f"DISTANCE: {distance:.1f} cm", True, WHITE
        )
    else:
        distance_text = font.render("DISTANCE: OUT OF RANGE", True, RED)

    screen.blit(distance_text, (20, 85))

    # Distance labels
    for i in range(1, 5):
        label = small_font.render(
            f"{int(MAX_DISTANCE * i / 4)} cm",
            True,
            GREEN,
        )

        x = CENTER_X + int(RADIUS * i / 4) - 25
        y = CENTER_Y - 20

        screen.blit(label, (x, y))

    pygame.display.flip()
    clock.tick(60)

arduino.close()
pygame.quit()
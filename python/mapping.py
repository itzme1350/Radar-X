import pygame
import serial
import math
import sys

# Arduino connection
PORT = "COM3"
BAUD_RATE = 9600

# Display configuration
WIDTH = 1000
HEIGHT = 750
MAX_DISTANCE = 200

BACKGROUND = (10, 15, 20)
GRID = (35, 65, 65)
GREEN = (0, 255, 120)
RED = (255, 70, 70)
WHITE = (230, 230, 230)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RADAR-X | 2D Environment Mapping")

clock = pygame.time.Clock()

font = pygame.font.SysFont("consolas", 22)
small_font = pygame.font.SysFont("consolas", 16)

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT - 80

SCALE = 2.8

# Store latest measurement for each angle
points = {}

current_angle = 90
current_distance = -1

try:
    arduino = serial.Serial(PORT, BAUD_RATE, timeout=0.01)
except serial.SerialException as error:
    print(f"Arduino connection failed: {error}")
    pygame.quit()
    sys.exit()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read Arduino measurements
    try:
        line = arduino.readline().decode(
            "utf-8", errors="ignore"
        ).strip()

        if "," in line:
            values = line.split(",")

            angle = int(values[0])
            distance = float(values[1])

            if 0 <= angle <= 180:

                current_angle = angle
                current_distance = distance

                if 0 < distance <= MAX_DISTANCE:

                    radians = math.radians(angle)

                    x = distance * math.cos(radians)
                    y = distance * math.sin(radians)

                    points[angle] = (x, y)

                else:
                    points.pop(angle, None)

    except (ValueError, serial.SerialException):
        pass

    screen.fill(BACKGROUND)

    # Draw distance grid
    for distance_mark in [50, 100, 150, 200]:

        radius = int(distance_mark * SCALE)

        pygame.draw.circle(
            screen,
            GRID,
            (CENTER_X, CENTER_Y),
            radius,
            1
        )

        label = small_font.render(
            f"{distance_mark} cm",
            True,
            GRID
        )

        screen.blit(
            label,
            (CENTER_X + radius + 5, CENTER_Y - 20)
        )

    # Draw angle guide lines
    for angle_mark in range(0, 181, 30):

        radians = math.radians(angle_mark)

        end_x = CENTER_X + MAX_DISTANCE * SCALE * math.cos(radians)
        end_y = CENTER_Y - MAX_DISTANCE * SCALE * math.sin(radians)

        pygame.draw.line(
            screen,
            GRID,
            (CENTER_X, CENTER_Y),
            (end_x, end_y),
            1
        )

    # Draw detected objects
    for angle, (x, y) in points.items():

        screen_x = CENTER_X + x * SCALE
        screen_y = CENTER_Y - y * SCALE

        pygame.draw.circle(
            screen,
            RED,
            (int(screen_x), int(screen_y)),
            5
        )

    # Current scanning direction
    radians = math.radians(current_angle)

    end_x = CENTER_X + MAX_DISTANCE * SCALE * math.cos(radians)
    end_y = CENTER_Y - MAX_DISTANCE * SCALE * math.sin(radians)

    pygame.draw.line(
        screen,
        GREEN,
        (CENTER_X, CENTER_Y),
        (end_x, end_y),
        2
    )

    # Sensor position
    pygame.draw.circle(
        screen,
        GREEN,
        (CENTER_X, CENTER_Y),
        10
    )

    # Information display
    title = font.render(
        "RADAR-X | 2D ENVIRONMENT MAPPING",
        True,
        GREEN
    )

    screen.blit(title, (20, 20))

    angle_text = font.render(
        f"ANGLE: {current_angle} deg",
        True,
        WHITE
    )

    screen.blit(angle_text, (20, 60))

    distance_text = font.render(
        f"DISTANCE: {current_distance:.1f} cm"
        if current_distance > 0
        else "DISTANCE: OUT OF RANGE",
        True,
        WHITE
    )

    screen.blit(distance_text, (20, 95))

    count_text = font.render(
        f"MAPPED POINTS: {len(points)}",
        True,
        GREEN
    )

    screen.blit(count_text, (20, 130))

    pygame.display.flip()
    clock.tick(60)

arduino.close()
pygame.quit()
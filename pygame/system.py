import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Солнечная система')

# Цвета
white = (255, 255, 255)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

# Радиусы планет (просто для примера)
sun_radius = 50
mercury_radius = 10
venus_radius = 15
earth_radius = 17
mars_radius = 14

# Расстояния от солнца до планет (просто для примера)
mercury_distance = 100
venus_distance = 180
earth_distance = 260
mars_distance = 350

# Скорости вращения (просто для примера)
mercury_speed = 0.02
venus_speed = 0.015
earth_speed = 0.01
mars_speed = 0.008

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(white)

    # Рисуем солнце
    pygame.draw.circle(screen, yellow, (width // 2, height // 2), sun_radius)

    # Рисуем планеты
    pygame.draw.circle(screen, blue, (width // 2 + mercury_distance, height // 2), mercury_radius)
    pygame.draw.circle(screen, red, (width // 2 + venus_distance, height // 2), venus_radius)
    pygame.draw.circle(screen, blue, (width // 2 + earth_distance, height // 2), earth_radius)
    pygame.draw.circle(screen, red, (width // 2 + mars_distance, height // 2), mars_radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

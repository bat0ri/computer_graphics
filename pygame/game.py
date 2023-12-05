import pygame


WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption('tanki')

square = pygame.Surface((70, 40))
square.fill('white')

#bg = pygame.image.load('bg.jpg')


import pygame
import math

class Tank:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0.2  # Задай скорость танка
        self.angle = 0  # Угол поворота танка
        self.image = pygame.image.load('glider.png')  # Загрузи изображение для танка
        self.rotated_image = self.image  # Изображение танка после поворота
        self.is_moving_forward = False
        self.is_moving_backward = False
        self.is_rotating_left = False
        self.is_rotating_right = False
        self.bullets = []  # Список для хранения снарядов

    def shoot(self):
        # Создание снаряда и добавление его в список снарядов
        bullet = Bullet(self.x, self.y, self.angle)
        self.bullets.append(bullet)

    def update_bullets(self):
        # Обновление положения каждого снаряда и удаление снарядов за пределами экрана
        for bullet in self.bullets:
            bullet.move()
            if not (0 <= bullet.x <= WINDOW_WIDTH and 0 <= bullet.y <= WINDOW_HEIGHT):
                self.bullets.remove(bullet)

    def draw(self, surface):
        # Получаем повернутое изображение танка
        rotated_tank, new_rect = self.rot_center(self.image, self.angle)
        # Отображаем повернутое изображение танка на указанной поверхности
        surface.blit(rotated_tank, (self.x - new_rect.width / 2, self.y - new_rect.height / 2))

    def rot_center(self, image, angle):
        # Получаем повернутое изображение и его ограничивающий прямоугольник
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center=image.get_rect().center)
        return rotated_image, new_rect

    def update(self):
        if self.is_moving_forward:
            self.move_forward()
        if self.is_moving_backward:
            self.move_backward()
        if self.is_rotating_left:
            self.rotate_left()
        if self.is_rotating_right:
            self.rotate_right()

    def check_collision(self, obstacle):
        tank_rect = pygame.Rect(self.x, self.y, self.rotated_image.get_width(), self.rotated_image.get_height())
        obstacle_rect = pygame.Rect(obstacle.x, obstacle.y, obstacle.width, obstacle.height)
        return tank_rect.colliderect(obstacle_rect)

    def move_forward(self):
        for obstacle in obstacles:
            if self.check_collision(obstacle):
                return

        new_x = self.x + self.speed * math.cos(math.radians(self.angle))
        new_y = self.y - self.speed * math.sin(math.radians(self.angle))
        if 0 <= new_x <= WINDOW_WIDTH and 0 <= new_y <= WINDOW_HEIGHT:
            self.x = new_x
            self.y = new_y

    def move_backward(self):
        for obstacle in obstacles:
            if self.check_collision(obstacle):
                return

        new_x = self.x - self.speed * math.cos(math.radians(self.angle))
        new_y = self.y + self.speed * math.sin(math.radians(self.angle))
        if 0 <= new_x <= WINDOW_WIDTH and 0 <= new_y <= WINDOW_HEIGHT:
            self.x = new_x
            self.y = new_y

    def rotate_left(self):
        # Поворот влево на 5 градусов
        self.angle += 1

    def rotate_right(self):
        # Поворот вправо на 5 градусов
        self.angle -= 1

class Bullet:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.speed = 3  # Скорость снаряда
        self.angle = angle

    def move(self):
        # Движение снаряда в направлении угла его выстрела
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y -= self.speed * math.sin(math.radians(self.angle))

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50  # Ширина препятствия
        self.height = 50  # Высота препятствия

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), (self.x, self.y, self.width, self.height))

obstacle = Obstacle(300, 300)  # Пример создания препятствия
obstacles = [obstacle]

tank = Tank(500, 505)

running = True
while running:
    screen.fill('white')

    tank.draw(screen)
    tank.update()
    tank.update_bullets()  # Обновление положения снарядов

    for bullet in tank.bullets:
        pygame.draw.circle(screen, (255, 0, 0), (int(bullet.x), int(bullet.y)), 5)

    for obs in obstacles:  # Отрисовка всех препятствий
        obs.draw(screen)

    for bullet in tank.bullets:
        for obs in obstacles:  # Проверка столкновения снарядов с препятствиями
            if obs.x < bullet.x < obs.x + obs.width and obs.y < bullet.y < obs.y + obs.height:
                tank.bullets.remove(bullet)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

         # Обработка нажатий клавиш для управления танком
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                tank.is_moving_forward = True
            elif event.key == pygame.K_s:
                tank.is_moving_backward = True
            elif event.key == pygame.K_a:
                tank.is_rotating_left = True
            elif event.key == pygame.K_d:
                tank.is_rotating_right = True

        # Обработка отпускания клавиш
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                tank.is_moving_forward = False
            elif event.key == pygame.K_s:
                tank.is_moving_backward = False
            elif event.key == pygame.K_a:
                tank.is_rotating_left = False
            elif event.key == pygame.K_d:
                tank.is_rotating_right = False
            elif event.key == pygame.K_SPACE:
                tank.shoot()


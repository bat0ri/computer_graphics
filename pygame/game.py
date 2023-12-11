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
    def __init__(self, x, y, angle: int = 0):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.max_health = 5 
        self.health = self.max_health 
        self.speed = 0.5 
        self.angle = angle
        self.image = pygame.image.load('glider.png') 
        self.rotated_image = self.image 
        self.is_moving_forward = False
        self.is_moving_backward = False
        self.is_rotating_left = False
        self.is_rotating_right = False
        self.bullets = [] 


    def receive_damage(self):
        self.health -= 1
    
    def draw_health_bar(self, surface):
        health_bar_length = 50 
        health_ratio = self.health / self.max_health 
        pygame.draw.rect(surface, (255, 0, 0), (self.x - 25, self.y - 40, health_bar_length, 5))  
        pygame.draw.rect(surface, (0, 255, 0), (self.x - 25, self.y - 40, health_bar_length * health_ratio, 5))

    
    def shoot(self):
        bullet = Bullet(self.x, self.y, self.angle)
        self.bullets.append(bullet)

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.move()
            if not (0 <= bullet.x <= WINDOW_WIDTH and 0 <= bullet.y <= WINDOW_HEIGHT):
                self.bullets.remove(bullet)

    def draw(self, surface):
        rotated_tank, new_rect = self.rot_center(self.image, self.angle)
        surface.blit(rotated_tank, (self.x - new_rect.width / 2, self.y - new_rect.height / 2))
        self.draw_health_bar(surface=surface)

    def rot_center(self, image, angle):
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
        new_x = self.x + self.speed * math.cos(math.radians(self.angle))
        new_y = self.y - self.speed * math.sin(math.radians(self.angle))
        next_rect = pygame.Rect(new_x - self.width / 2, new_y - self.height / 2, self.width, self.height)

        for obstacle in obstacles:
            if next_rect.colliderect(pygame.Rect(obstacle.x, obstacle.y, obstacle.width, obstacle.height)):
                return 

        if 0 <= new_x <= WINDOW_WIDTH and 0 <= new_y <= WINDOW_HEIGHT:
            self.x = new_x
            self.y = new_y

    def move_backward(self):
        new_x = self.x - self.speed * math.cos(math.radians(self.angle))
        new_y = self.y + self.speed * math.sin(math.radians(self.angle))
        next_rect = pygame.Rect(new_x - self.width / 2, new_y - self.height / 2, self.width, self.height)

        for obstacle in obstacles:
            if next_rect.colliderect(pygame.Rect(obstacle.x, obstacle.y, obstacle.width, obstacle.height)):
                return

        if 0 <= new_x <= WINDOW_WIDTH and 0 <= new_y <= WINDOW_HEIGHT:
            self.x = new_x
            self.y = new_y

    def rotate_left(self):
        self.angle += 0.5

    def rotate_right(self):
        self.angle -= 0.5

class Bullet:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.speed = 1 
        self.angle = angle

    def move(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y -= self.speed * math.sin(math.radians(self.angle))

    def check_collision(self, tank):
        bullet_rect = pygame.Rect(self.x, self.y, 5, 5)
        tank_rect = pygame.Rect(tank.x - tank.width / 2, tank.y - tank.height / 2, tank.width, tank.height)  
        return bullet_rect.colliderect(tank_rect)

class Obstacle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h 

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), (self.x, self.y, self.width, self.height))

gate1 = Obstacle(200, 100, 600, 10) 
gate2 = Obstacle(200, 900, 600, 10)
central = Obstacle(400, 400, 200, 200)
vertical_gate1 = Obstacle(250, 200, 20, 250)
vertical_gate2 = Obstacle(750, 550, 20, 250)
obstacles = [gate1, gate2, central, vertical_gate1, vertical_gate2]


tank = Tank(100, 505)
tank2 = Tank(900, 505, angle=180)

last_shot_time_tank = pygame.time.get_ticks()
shoot_cooldown = 1000 

running = True
while running:
    if tank.health <= 0 or tank2.health <= 0:
        running = False 
    screen.fill('white')

    current_time = pygame.time.get_ticks()
    if current_time - last_shot_time_tank > shoot_cooldown:
        tank.shoot()
        tank2.shoot()
        last_shot_time_tank = current_time


    tank.draw(screen)
    tank.update()
    tank.update_bullets()

    tank2.draw(screen)
    tank2.update()
    tank2.update_bullets()

    for bullet in tank.bullets:
        if bullet.check_collision(tank2):
            tank2.receive_damage()
            tank.bullets.remove(bullet)
        pygame.draw.circle(screen, (255, 0, 0), (int(bullet.x), int(bullet.y)), 5)

    for bullet2 in tank2.bullets:
        if bullet2.check_collision(tank):
            tank.receive_damage()
            tank2.bullets.remove(bullet2)
        pygame.draw.circle(screen, (255, 0, 0), (int(bullet2.x), int(bullet2.y)), 5)

    for obs in obstacles:
        obs.draw(screen)

    for bullet in tank.bullets:
        for obs in obstacles: 
            if obs.x < bullet.x < obs.x + obs.width and obs.y < bullet.y < obs.y + obs.height:
                tank.bullets.remove(bullet)

    for bullet2 in tank2.bullets:
        for obs in obstacles: 
            if obs.x < bullet2.x < obs.x + obs.width and obs.y < bullet2.y < obs.y + obs.height:
                tank2.bullets.remove(bullet2)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        # Обработка нажатий клавиш для управления первым танком
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                tank.is_moving_forward = True
            elif event.key == pygame.K_s:
                tank.is_moving_backward = True
            elif event.key == pygame.K_a:
                tank.is_rotating_left = True
            elif event.key == pygame.K_d:
                tank.is_rotating_right = True
            elif event.key == pygame.K_SPACE:
                tank.shoot()

        # Обработка отпускания клавиш для управления первым танком
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                tank.is_moving_forward = False
            elif event.key == pygame.K_s:
                tank.is_moving_backward = False
            elif event.key == pygame.K_a:
                tank.is_rotating_left = False
            elif event.key == pygame.K_d:
                tank.is_rotating_right = False

        # Обработка нажатий клавиш для управления вторым танком
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                tank2.is_moving_forward = True
            elif event.key == pygame.K_DOWN:
                tank2.is_moving_backward = True
            elif event.key == pygame.K_LEFT:
                tank2.is_rotating_left = True
            elif event.key == pygame.K_RIGHT:
                tank2.is_rotating_right = True
            elif event.key == pygame.K_RCTRL:
                tank2.shoot()

        # Обработка отпускания клавиш для управления вторым танком
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                tank2.is_moving_forward = False
            elif event.key == pygame.K_DOWN:
                tank2.is_moving_backward = False
            elif event.key == pygame.K_LEFT:
                tank2.is_rotating_left = False
            elif event.key == pygame.K_RIGHT:
                tank2.is_rotating_right = False



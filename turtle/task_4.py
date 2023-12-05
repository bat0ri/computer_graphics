import turtle
import math
import random, time



class Moon:
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.bgcolor("black")
        self.wn.title("Звездное ночное небо")

        self.stars = turtle.Turtle()
        self.stars.color("white")
        self.stars.penup()
        self.stars.speed(0)
        #self.draw_stars()

        self.moon = turtle.Turtle()
        self.moon.color("white")
        self.moon.penup()
        self.moon.speed('fastest')
        self.move_moon()

        


    def star(self, n, dlina):
        self.stars.begin_fill()
        if n % 2 != 0:
            for i in range(n):
                self.stars.forward(dlina)
                angle = n // 2 * 360 / n
                self.stars.left(angle)
        self.stars.end_fill()


    def draw_stars(self):
        for _ in range(random.randint(20, 80)):
            x = random.randint(-turtle.window_width()//2, turtle.window_width()//2)
            y = random.randint(-turtle.window_height()//2, turtle.window_height()//2)
            self.stars.goto(x, y)
            self.star(random.randint(4, 9), random.randint(5, 30))

    def draw_moon(self, radius, b):
        self.moon.pendown()
        self.moon.width(2)
        self.moon.fillcolor('yellow')
        self.moon.begin_fill()
        self.moon.circle(radius, -180)
        dx, dy = self.moon.pos()
        for deg in range(180):
            rad = math.radians(deg)
            x = b * math.sin(rad) + dx
            y = radius * math.cos(rad) - radius + dy
            self.moon.goto(x, y)
        self.moon.left(180)
        self.moon.end_fill()


    def move_moon(self):
        self.wn.tracer(1)
        self.moon.speed('fastest')
        for i in range(100):
            self.draw_moon(100, i - 30)
            time.sleep(1)
            self.moon.clear()
            turtle.update()
    


def move_moon():
    for i in range(360):
        x = i
        y = -0.001 * (x - 280) ** 2  # Движение через центр по параболе
        moon.goto(x - turtle.window_width() // 2, y)

        phase = int((i / 360) * 8)
        moon.color("white")
        if phase == 1:
            moon.color("gray")
        elif phase == 2:
            moon.color("black")

m = Moon()
turtle.done()

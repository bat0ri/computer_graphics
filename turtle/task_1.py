import turtle
import math

class Bullet:
    def __init__(self):
        self.bullet = turtle.Turtle()
        self.bullet.penup()
        self.bullet.goto(-600, -275)
        self.bullet.pendown()
        self.bullet.shape('square')
        self.bullet.shapesize(stretch_wid=1.0, stretch_len=6.0)
        self.bullet.color('black')
        self.bullet.lt(50)

    def turn_right(self):
        if self.bullet.heading() > 0:
            self.bullet.rt(5)

    def turn_left(self):
        if self.bullet.heading() < 75:
            self.bullet.lt(5)

    def shoot(self):
        self.bullet.speed(0)
        self.bullet.goto(-600, -275)
        angle = self.bullet.heading()
        speed = 100

        dx = speed * math.cos(math.radians(angle))
        dy = speed * math.sin(math.radians(angle))

        self.bullet.speed(2)
        while self.bullet.ycor() >= -375:
            self.bullet.goto(self.bullet.xcor() + dx, self.bullet.ycor() + dy)
            dy += gravity

class Cannon:
    def __init__(self):
        self.p1 = turtle.Turtle()
        self.p1.pencolor("black")
        self.p1.pensize(3)
        self.p1.fillcolor("black")
        self.p1.penup()
        self.p1.goto(-600, -275)
        self.p1.pendown()

    def cannon(self):
        self.p1.pendown()
        self.p1.speed(0)
        self.p1.begin_fill()
        self.p1.circle(-20)
        self.p1.end_fill()
        self.p1.shape("circle")
        self.p1.penup()

    def setup_controls(self, window):
        window.onkey(self.turn_left, 'Up')
        window.onkey(self.turn_right, 'Down')
        window.onkey(self.shoot, 'space')

    def turn_right(self):
        bullet.turn_right()

    def turn_left(self):
        bullet.turn_left()

    def shoot(self):
        bullet.shoot()

gravity = -9.81

def main():
    window = turtle.Screen()
    window.setup(1400, 700)
    window.listen()

    cannon = Cannon()
    cannon.cannon()
    cannon.setup_controls(window)

    global bullet
    bullet = Bullet()

    window.mainloop()

if __name__ == "__main__":
    main()

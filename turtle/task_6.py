import turtle
import math
window = turtle.Screen()
window.setup(1400, 700)
window.listen()


p1 = turtle.Turtle()
p1.pencolor("black")
p1.pensize(3)
p1.fillcolor("black")
p1.penup()
p1.goto(-600, -275)
p1.pendown()

bullet = turtle.Turtle()
bullet.penup()
bullet.goto(-600, -275)
bullet.pendown()
bullet.shape('square')
bullet.shapesize(stretch_wid=1.0, stretch_len=6.0)
bullet.color('black')
bullet.lt(50)


def cannon(t):
    t.pendown()
    t.speed(0)
    t.begin_fill()
    t.circle(-20)
    t.end_fill()
    t.shape("circle")
    t.penup()



cannon(p1)

def turn_right():
    if bullet.heading() > 0:
        bullet.rt(5)


def turn_left():
    if bullet.heading() < 75:
        bullet.lt(5)


def shoot_gun():
    t = p1
    t.speed(0)
    p1.goto(-600, -275)
    angle = bullet.heading()
    speed = 100
    cannon(t)

    dx = speed * math.cos(math.radians(angle))
    dy = speed * math.sin(math.radians(angle))

    t.speed(2)
    while t.ycor() >= -375:
        t.goto(t.xcor() + dx, t.ycor() + dy)
        dy += gravity


window.onkey(turn_left, 'Up')
window.onkey(turn_right, 'Down')
window.onkey(shoot_gun, 'space')

gravity = -9.81


window.mainloop()
import turtle
import time
import math

# Создание экрана для рисования
screen = turtle.Screen()
screen.title("Аналоговые часы")
screen.setup(width=600, height=600)
screen.tracer(0)

# Создание черепахи для отрисовки окружности
circle_pen = turtle.Turtle()
circle_pen.speed(0)
circle_pen.hideturtle()
circle_pen.penup()
circle_pen.goto(0, -150)
circle_pen.color("black")
circle_pen.pendown()
circle_pen.circle(150)

# Создание черепахи для часовой стрелки
hour_hand = turtle.Turtle()
hour_hand.shape("arrow")
hour_hand.shapesize(stretch_wid=0.5, stretch_len=8)
hour_hand.color("black")
hour_hand.penup()
hour_hand.goto(0, 0)

# Создание черепахи для минутной стрелки
minute_hand = turtle.Turtle()
minute_hand.shape("arrow")
minute_hand.shapesize(stretch_wid=0.5, stretch_len=10)
minute_hand.color("blue")
minute_hand.penup()
minute_hand.goto(0, 0)

# Создание черепахи для секундной стрелки
second_hand = turtle.Turtle()
second_hand.shape("arrow")
second_hand.shapesize(stretch_wid=0.2, stretch_len=14)
second_hand.color("red")
second_hand.penup()
second_hand.goto(0, 0)


def draw_clock():
    while True:
        current_time = time.localtime()
        hours = current_time.tm_hour
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        hour_angle = math.radians((hours % 12) * 30 + minutes * 0.5)
        minute_angle = math.radians(minutes * 6)
        second_angle = math.radians(seconds * 6)

        hour_hand.setheading(90 - math.degrees(hour_angle))
        minute_hand.setheading(90 - math.degrees(minute_angle))
        second_hand.setheading(90 - math.degrees(second_angle))

        screen.update()

        time.sleep(1)


draw_clock()
screen.mainloop()

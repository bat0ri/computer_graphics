import turtle

# Создание окна
win = turtle.Screen()
win.title("Пинг-понг")
win.bgcolor("black")
win.setup(width=600, height=400)

# Создание объекта для отрисовки границ поля
board = turtle.Turtle()
board.speed(0)
board.color("white")
board.penup()
board.goto(-290, 190)  # Начальные координаты верхнего левого угла поля
board.pendown()
board.pensize(3)

# Рисование границ поля
for side in range(4):
    if side % 2 == 0:
        board.forward(580)
    else:
        board.forward(380)
    board.right(90)

# Завершение рисования
board.hideturtle()


# Создание ракеток
racket_a = turtle.Turtle()
racket_a.speed(0)
racket_a.shape("square")
racket_a.color("white")
racket_a.shapesize(stretch_wid=6, stretch_len=1)
racket_a.penup()
racket_a.goto(-250, 0)

racket_b = turtle.Turtle()
racket_b.speed(0)
racket_b.shape("square")
racket_b.color("white")
racket_b.shapesize(stretch_wid=6, stretch_len=1)
racket_b.penup()
racket_b.goto(250, 0)

# Создание мяча
ball = turtle.Turtle()
ball.speed(40)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1  # Скорость по x
ball.dy = -1  # Скорость по y

# Функции для движения ракеток
def racket_a_up():
    y = racket_a.ycor()
    if y < 150:
        y += 20
    racket_a.sety(y)

def racket_a_down():
    y = racket_a.ycor()
    if y > -140:
        y -= 20
    racket_a.sety(y)

def racket_b_up():
    y = racket_b.ycor()
    if y < 150:
        y += 20
    racket_b.sety(y)

def racket_b_down():
    y = racket_b.ycor()
    if y > -140:
        y -= 20
    racket_b.sety(y)

# Обработка клавиш
win.listen()
win.onkeypress(racket_a_up, "w")
win.onkeypress(racket_a_down, "s")
win.onkeypress(racket_b_up, "Up")
win.onkeypress(racket_b_down, "Down")

# Основной игровой цикл
while True:
    win.update()

    # Движение мяча
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Отскок от верхней и нижней стенок
    if ball.ycor() > 190:
        ball.sety(190)
        ball.dy *= -1

    if ball.ycor() < -190:
        ball.sety(-190)
        ball.dy *= -1

    # Отскок от ракеток
    if (ball.dx > 0) and (
        racket_b.xcor() - 10 < ball.xcor() < racket_b.xcor() + 10
    ) and (racket_b.ycor() + 50 > ball.ycor() > racket_b.ycor() - 50):
        ball.setx(racket_b.xcor() - 10)
        ball.dx *= -1

    if (ball.dx < 0) and (
        racket_a.xcor() - 10 < ball.xcor() < racket_a.xcor() + 10
    ) and (racket_a.ycor() + 50 > ball.ycor() > racket_a.ycor() - 50):
        ball.setx(racket_a.xcor() + 10)
        ball.dx *= -1

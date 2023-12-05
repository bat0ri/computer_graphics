import turtle


class Pong():

    def __init__(self):
        self.win = turtle.Screen()
        self.win.title("Пинг-понг")
        self.win.bgcolor("black")
        self.win.setup(width=800, height=600)
        self.draw_board()
        self.draw_rackets()
        self.draw_ball()
        self.win.listen()
        self.win.onkeypress(self.racket_a_up, "w")
        self.win.onkeypress(self.racket_a_down, "s")
        self.win.onkeypress(self.racket_b_up, "Up")
        self.win.onkeypress(self.racket_b_down, "Down")
        self.score_a = 0
        self.score_b = 0
        self.score_display = turtle.Turtle()
        self.score_display.speed(0)
        self.score_display.color("white")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.update_score()
        self.game()


    def draw_board(self):
        board = turtle.Turtle()
        board.speed(0)
        board.color("white")
        board.penup()
        board.goto(-300, 200) 
        board.pendown()
        board.pensize(3)
        for side in range(4):
            if side % 2 == 0:
                board.forward(600)
            else:
                board.forward(400)
            board.right(90)
        board.hideturtle()

    def draw_rackets(self):
        self.racket_a = turtle.Turtle()
        self.racket_a.speed(0)
        self.racket_a.shape("square")
        self.racket_a.color("white")
        self.racket_a.shapesize(stretch_wid=4, stretch_len=1)
        self.racket_a.penup()
        self.racket_a.goto(-250, 0)

        self.racket_b = turtle.Turtle()
        self.racket_b.speed(0)
        self.racket_b.shape("square")
        self.racket_b.color("white")
        self.racket_b.shapesize(stretch_wid=4, stretch_len=1)
        self.racket_b.penup()
        self.racket_b.goto(250, 0)

    def draw_ball(self):
        self.ball = turtle.Turtle()
        self.ball.speed(40)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 2  # Скорость по x
        self.ball.dy = -2  # Скорость по y

    def racket_a_up(self):
        y = self.racket_a.ycor()
        if y < 150:
            y += 20
        self.racket_a.sety(y)

    def racket_a_down(self):
        y = self.racket_a.ycor()
        if y > -140:
            y -= 20
        self.racket_a.sety(y)

    def racket_b_up(self):
        y = self.racket_b.ycor()
        if y < 150:
            y += 20
        self.racket_b.sety(y)

    def racket_b_down(self):
        y = self.racket_b.ycor()
        if y > -140:
            y -= 20
        self.racket_b.sety(y)

    def game(self):
        while True:
            self.win.update()

            # Движение мяча
            self.ball.setx(self.ball.xcor() + self.ball.dx)
            self.ball.sety(self.ball.ycor() + self.ball.dy)

            if self.ball.xcor() > 290:
                self.goal()
            elif self.ball.xcor() < -290:
                self.goal()

            # Отскок от верхней и нижней стенок
            if self.ball.ycor() > 190:
                self.ball.sety(190)
                self.ball.dy *= -1

            if self.ball.ycor() < -190:
                self.ball.sety(-190)
                self.ball.dy *= -1

            # Отскок от ракеток
            if (self.ball.dx > 0) and (
                self.racket_b.xcor() - 10 < self.ball.xcor() < self.racket_b.xcor() + 10
            ) and (self.racket_b.ycor() + 50 > self.ball.ycor() > self.racket_b.ycor() - 50):
                self.ball.setx(self.racket_b.xcor() - 10)
                self.ball.dx *= -1

            if (self.ball.dx < 0) and (
                self.racket_a.xcor() - 10 < self.ball.xcor() < self.racket_a.xcor() + 10
            ) and (self.racket_a.ycor() + 50 > self.ball.ycor() > self.racket_a.ycor() - 50):
                self.ball.setx(self.racket_a.xcor() + 10)
                self.ball.dx *= -1

    def goal(self):
        if self.ball.xcor() > 290:
            self.score_a += 1
        elif self.ball.xcor() < -290:
            self.score_b += 1

        self.update_score()

        if self.score_a == 3 or self.score_b == 3:
            self.game_over()
        else:
            self.ball.goto(0, 0)
            self.ball.dx *= -1

            self.ball.goto(0, 0)
            self.ball.dx *= -1  # меняем направление мяча

    def update_score(self):
        self.score_display.clear()
        self.score_display.goto(0, 150)
        self.score_display.write(f"Игрок A: {self.score_a}  Игрок B: {self.score_b}", align="center", font=("Courier", 18, "normal"))

    def game_over(self):
        self.ball.goto(0, 0)
        self.ball.dx = 0
        self.ball.dy = 0
        self.score_display.goto(0, 0)
        if self.score_a == 3:
            self.score_display.write("Игрок A победил!", align="center", font=("Courier", 24, "normal"))
        else:
            self.score_display.write("Игрок B победил!", align="center", font=("Courier", 24, "normal"))
        self.racket_a.hideturtle()
        self.racket_b.hideturtle()
        self.ball.hideturtle()

pong = Pong()
turtle.done()
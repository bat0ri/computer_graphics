import turtle
import random
import math

class Moon:
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.bgcolor("black")
        self.wn.title("Звездное ночное небо")

        self.stars = turtle.Turtle()
        self.stars.color("white")
        self.stars.penup()
        self.stars.speed(0)
        self.draw_stars()

        self.moonWhite1 = turtle.Turtle()
        self.moonWhite2 = turtle.Turtle()
        self.moonBlack = turtle.Turtle()

        self.moonWhite1.speed(0)
        self.moonWhite2.speed(0)
        self.moonBlack.speed(0)

        self.moonWhite1.hideturtle()
        self.moonWhite2.hideturtle()
        self.moonBlack.hideturtle()

        self.moonWhite1.pencolor('white')
        self.moonWhite2.pencolor('white')
        self.moonBlack.pencolor(self.wn.bgcolor())

    def star(self, n, dlina):
        self.stars.begin_fill()
        if n % 2 != 0:
            for _ in range(n):
                self.stars.forward(dlina)
                angle = n // 2 * 360 / n
                self.stars.left(angle)
        self.stars.end_fill()

    def draw_stars(self):
        for _ in range(random.randint(20, 80)):
            x = random.randint(-turtle.window_width() // 2, turtle.window_width() // 2)
            y = random.randint(-turtle.window_height() // 2, turtle.window_height() // 2)
            self.stars.goto(x, y)
            self.star(random.randint(4, 9), random.randint(5, 30))

    def draw_moon(self):
        x = [i for i in range(-700, 700)]
        y = [-0.001 * i ** 2 + 50 for i in x]

        delay = 0
        for i in range(len(x)):
            if i <= 700:
                delay = i * 1.2
            else:
                delay = delay + 0.7

            if i % 2 == 0:
                self.moonWhite1.up()
                self.moonWhite1.goto(x[i], y[i])
                self.moonWhite1.down()
                self.moonWhite1.dot(150)

                self.moonBlack.up()
                self.moonBlack.goto(x[int(delay)], y[int(delay)])
                self.moonBlack.down()
                self.moonBlack.dot(150)

                self.moonWhite2.clear()
                turtle.update()
            else:
                self.moonWhite2.up()
                self.moonWhite2.goto(x[i], y[i])
                self.moonWhite2.down()
                self.moonWhite2.dot(150)

                self.moonBlack.up()
                self.moonBlack.goto(x[int(delay)], y[int(delay)])
                self.moonBlack.down()
                self.moonBlack.dot(150)

                self.moonWhite1.clear()
                turtle.update()

        self.wn.exitonclick()

if __name__ == "__main__":
    moon = Moon()
    moon.draw_moon()

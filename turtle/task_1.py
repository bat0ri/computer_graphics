from random import randint
from turtle import *

WIDTH, HEIGHT = 1200, 900


class Tree:
    def __init__(self, w, h):
        
        self.screen = Screen()
        self.screen.title('Tree with L system')
        self.screen.bgcolor('white')
        self.screen.setup(w, h)
        self.screen.screensize(3 * w, 3 * h)

        self.axiom = 'X'

        self.pen = Turtle()
        self.pen.pensize(20)
        self.pen.seth(90)

    def get_rules(self, gen):
        chr_1, rule_1 = 'X', 'F[@[-X]+X]'
        for i in range(gen):
            self.axiom = ''.join([rule_1 if chr == chr_1 else chr for chr in self.axiom])
            print('gen', i, 'is', self.axiom)

    def draw(self):
        self.pen.speed("fastest")
        self.screen.tracer(0)

        step = 100
        angle = lambda: randint(-5, 30)
        stack = []
        thickness = 20

        for chr in self.axiom:
            if chr == 'F' or chr == 'X':
                if step > 0:
                    self.pen.forward(step)
            elif chr == '@':
                step -= randint(2, 10)
                thickness -= 2
                thickness = max(1, thickness)
                self.pen.pensize(thickness)
            elif chr == '+':
                self.pen.right(angle())
            elif chr == '-':
                self.pen.left(angle())
            elif chr == '[':
                angle_, pos_ = self.pen.heading(), self.pen.pos()
                stack.append((angle_, pos_, thickness, step))
            elif chr == ']':
                angle_, pos_, thickness, step = stack.pop()
                self.pen.pensize(thickness)
                self.pen.setheading(angle_)
                self.pen.penup()
                self.pen.goto(pos_)
                self.pen.pendown()

        self.screen.mainloop()


if __name__ == '__main__':
    tree = Tree(WIDTH, HEIGHT)
    tree.get_rules(10)
    tree.draw()

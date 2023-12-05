import turtle
from random import randint

class StockGraph:
    def __init__(self, width, height):
        self.screen = turtle.Screen()
        self.screen.title("Stock Price Graph")
        self.screen.setup(width, height)
        self.set_params(width, height)

        self.color = False

    def set_params(self, width, height):
        self.len_Y_axe = height - height/10
        self.len_X_axe = width - width/10
        self.start_X = -self.len_X_axe/2

    def draw_axes(self):
        self.axis = turtle.Turtle()
        self.axis.width(3)
        self.axis.penup()
        self.axis.goto(-self.len_X_axe/2, self.len_Y_axe/2)
        self.axis.right(90)
        self.axis.pendown()

        self.axis.forward(self.len_Y_axe)

        self.axis.left(90)
        self.axis.forward(self.len_X_axe)
        self.axis.hideturtle()

    def p_price(self, p):
        self.p_line = turtle.Turtle()
        self.p_line.penup()
        self.p_line.goto(-self.len_X_axe/2, p - self.len_Y_axe/2)
        self.p_line.pendown()
        self.p_line.forward(self.len_X_axe)

    def get_X(self, n):
        h = self.len_X_axe / n
        self.time = []
        for x in range(n):
            self.time.append(-self.len_X_axe/2 + x*h)
    
    def get_Y(self, n):
        self.price = [randint(-self.len_Y_axe//2, self.len_Y_axe//2) for _ in range(n)]


    def graph(self, p):
        self.g = turtle.Turtle()
        self.g.width(4)
        self.g.penup()
        self.g.goto(self.time[0], self.price[0])
        self.g.pendown()
        p = p - self.len_Y_axe/2

        for i in range(1, len(self.time)):
            x1 = self.time[i - 1]
            y1 = self.price[i - 1]
            x2 = self.time[i]
            y2 = self.price[i]

            if y2 > p and y1 < p:
                self.g.color('green')
            if y2 < p:
                self.g.color('red')


            self.g.pendown()
            self.g.goto(x2, y2)
            self.g.penup()

if __name__ == "__main__":
    stock_graph = StockGraph(1000, 500)
    stock_graph.draw_axes()
    stock_graph.p_price(250)
    stock_graph.get_X(50)
    stock_graph.get_Y(50)
    stock_graph.graph(250)

    turtle.done()

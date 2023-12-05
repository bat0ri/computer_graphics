import turtle

class YinYang:
    def __init__(self, radius):

        self.screen = turtle.Screen()
        self.screen.title("Yin and Yang")
        self.screen.setup(width=5*radius, height=5*radius)
        self.set_params(radius)

    def set_params(self, radius):
        self.main_radius = radius
        self.half_radius = radius / 2
        self.eye_radius = radius / 8
        self.eye_height = self.half_radius - self.eye_radius


    def draw_circle(self):
        self.circle = turtle.Turtle()
        self.circle.circle(self.main_radius)
        self.circle.hideturtle()

    def draw_yang(self):
        self.yin = turtle.Turtle()
        self.yin.fillcolor('black')
        self.yin.begin_fill()
        self.yin.circle(self.main_radius, 180)
        self.yin.circle(self.half_radius, -180)
        self.yin.circle(-self.half_radius, -180)
        self.yin.end_fill()
        self.yin.penup()
        self.yin.right(90)
        self.yin.fd(self.eye_height)
        self.yin.pendown()
        self.yin.right(90)
        self.yin.fillcolor('white')
        self.yin.begin_fill()
        self.yin.circle(self.eye_radius, 360)
        self.yin.end_fill()

        self.yin.hideturtle()

    def draw_yin(self):
        self.yang = turtle.Turtle()
        self.yang.penup()
        self.yang.left(90)
        self.yang.forward(2*self.main_radius - self.eye_height)
        self.yang.pendown()
        self.yang.left(90)
        self.yang.fillcolor("black")
        self.yang.begin_fill()
        self.yang.circle(self.eye_radius, 360)
        self.yang.end_fill()

        self.yang.hideturtle()

if __name__ == "__main__":
    yin_yang = YinYang(200)
    yin_yang.draw_circle()
    yin_yang.draw_yang()
    yin_yang.draw_yin()

    turtle.done()

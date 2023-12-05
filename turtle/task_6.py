import turtle
import math


class Ballistic:

    def __init__(self, w, h):
        self.screen = turtle.Screen()
        self.screen.title("Моделирование баллистики")
        self.screen.setup(width=w, height=h)
        self.draw_gun(w, h)
        self.set_snar()


    def set_snar(self):
        self.projectile = turtle.Turtle()
        self.projectile.hideturtle()
        self.projectile.shape('circle')
        self.projectile.color('red')
        self.projectile.penup()
        self.projectile.setpos(self.gun.xcor(), self.gun.ycor())
        self.projectile.left(45)
        self.projectile.speed(0)
        self.projectile.pendown()


    def draw_gun(self, w, h):
        self.gun = turtle.Turtle()
        self.gun.speed('fastest')
        self.gun.penup()
        self.gun.setpos(-w//2 + w//10 - w/100 , -h//2 + h//10)
        self.gun.right(90)
        
        self.gun.begin_fill()
        self.gun.color('black')
        self.gun.circle(w/100, 360)
        self.gun.end_fill()


        shape = ((10, 0), (10, 100), (-10, 100), (-10, 0))

        turtle.register_shape('gun', shape)
        self.gun.shape('gun')
        self.gun.left(135)

        self.gun.penup()
        self.gun.setpos(-w//2 + w//10 , -h//2 + h//10)
        self.gun.pendown()


    def rotate_up(self):
        self.gun.left(5)
        self.projectile.left(5)

    def rotate_down(self):
        self.gun.right(5)
        self.projectile.right(5)

    def shot(self):
        print('shot')
        self.fire_projectile()

    def setup_controls(self):
        self.screen.listen()
        self.screen.onkeypress(self.rotate_up, "Up")
        self.screen.onkeypress(self.rotate_down, "Down")
        self.screen.onkeypress(self.shot, "space")

    def get_X(self, start):
        h = (900 - start)/100
        x = []
        x.append(start)
        for i in range(1, 100):
            x.append(x[i-1] + h)
        
        return x

    def get_time(self):
        time = []
        time.append(0)
        x = self.get_X(self.projectile.xcor())
        for i in range(1, 100):
            time.append((x[i] -  self.projectile.xcor())/ speed)

    
    def get_Y(self, start, speed):
        time = self.get_time()
        
        

       


    def fire_projectile(self):
        self.projectile.setpos(self.gun.xcor(), self.gun.ycor())
        self.projectile.forward(100)
        self.get_X(self.projectile.xcor())
        self.get_Y(self.projectile.ycor(), 100)



        




b = Ballistic(1800, 600)
b.setup_controls()
turtle.done()
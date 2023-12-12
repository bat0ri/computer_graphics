import turtle

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def draw_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter):
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.tracer(0)

    turtle_speed = 0
    turtle_width = 1

    for y in range(height):
        for x in range(width):
            cx = xmin + (xmax - xmin) * x / width
            cy = ymin + (ymax - ymin) * y / height
            c = complex(cx, cy)
            color = mandelbrot(c, max_iter)
            screen.colormode(255)
            turtle.penup()
            turtle.goto(x - width // 2, height // 2 - y)
            turtle.pendown()
            turtle.width(turtle_width)
            turtle.speed(turtle_speed)
            turtle.color(color % 256, (color * 7) % 256, (color * 13) % 256)
            turtle.forward(1)

        screen.update()

if __name__ == "__main__":
    width, height = 300, 200
    xmin, xmax = -2.0, 1.0
    ymin, ymax = -1.5, 1.5
    max_iter = 50

    draw_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter)
    turtle.done()

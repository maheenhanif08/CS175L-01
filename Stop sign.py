#Maheen Hanif Ghaffar
#CS-175L 01
#Stop Sign


import math
import turtle

m = math
t = turtle

screen = t.Screen()
screen.bgcolor("black")

window_width = 400
window_height = 400
animation_speed = 0
num_sides = 8
length = 100
angle = 45
test_x = -5
test_y = -10

s = length
x = s / m.sqrt(2)
diameter = s + (2 * x)

t.color("white", "yellow")
t.setup(window_width, window_height)

def draw_stopsign(t, x, y, length):
    t.penup()
    t.setpos(x - length / 2, y + length / 2 / (math.pi/8))
    t.pendown()
    t.color("white", "red")
    t.pensize = (length // 10)
    t.begin_fill()

    for x in range(8):
        t.forward(length)
        t.right(45)
    t.end_fill()

    fontsize = int(length / 2)
    t.penup()
    t.setpos(x, y - fontsize / 2 )
    t.pendown()
    t.write ("STOP", move = False, align = "center", font = ("Arial", fontsize, "normal"))
    t.hideturtle()

draw_stopsign(t, 0, 0, 100)

turtle.mainloop

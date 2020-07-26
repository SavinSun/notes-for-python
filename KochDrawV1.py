#KochDrawV1.py
import turtle
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0,90,-180,90]:
            turtle.left(angle)
            koch(size/3,n-1)
def main():
    turtle.setup(600,600)
    turtle.pu()
    turtle.goto(-200,100)
    turtle.pd()
    turtle.pensize(2)
    level = 3
    koch(500, level)
    turtle.right(120)
    koch(500, level)
    turtle.right(120)
    koch(500,level)
    turtle.hideturtle()
main()

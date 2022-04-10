from turtle import *

bgcolor("palevioletred")
def curve():
    for i in range(200):
        right(1)
        forward(1)

def heart():
    fillcolor("gold")
    begin_fill()
    left(140)
    forward(110)
    curve()
    left(120)
    curve()
    forward(110)
    end_fill()



heart()
penup()
goto(-100,-200)
pendown()
color("gold")
write("I love python!",font=("Arial",24,"bold"))
hideturtle()
done()

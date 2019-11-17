

from turtle import forward, exitonclick, penup, pendown


for cislo in range(8):
    forward(cislo + 10)
    penup()
    forward(10)
    pendown()


exitonclick()

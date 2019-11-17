from turtle import penup, pendown, forward, right, left, goto, setx, exitonclick
from math import sqrt, cos, radians, pi

pocet = int(input("Zadej počet stran: " ))

uhel = pocet * 1
strana=2


for i in range(pocet):
    forward(strana)
    left(180 -(180 *(1 - (strana/uhel))))


exitonclick()
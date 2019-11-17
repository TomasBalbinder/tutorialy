
from turtle import forward, right, left, exitonclick
from math import sqrt, cos, radians
strana = 50

for i in range(1):
    forward(strana)
    left(90)
    forward(strana)
    left(90 + 45)
    forward(strana*sqrt(2))
    right(90 + 45)
    forward(strana)
    right(90)
    forward(strana)
    left(90 + 45)
    forward(strana * cos(radians(45)))
    left(90)
    forward(strana * cos(radians(45)))
    left(90)
    forward(strana*sqrt(2))
    left(45)


    

exitonclick()
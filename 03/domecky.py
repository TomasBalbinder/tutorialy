from turtle import penup, pendown, forward, right, left, goto, setx, exitonclick
from math import sqrt, cos, radians
strana = 50


penup()
setx(-250)
pendown()
for i in range(5):   
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
    
    forward(50)

    

exitonclick()
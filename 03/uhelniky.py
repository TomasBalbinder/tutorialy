from turtle import penup, pendown, forward, right, left, goto, setx, exitonclick
from math import sqrt, cos, radians, pi

strana = 50

penup()
setx(-250)
pendown()
for i in range(1): 
   
    for i in range(5):
        forward(strana)
        left(180 -(180 *(1 - (strana/125))))
    
    penup()
    forward(100)
    pendown()

    for i in range(6):
        forward(strana)
        left(180 -(180 *(1 - (strana/150))))

    penup()
    forward(125)
    pendown()

    for i in range(7):
        forward(strana)
        left(180 -(180 *(1 - (strana/175))))
        

    penup()
    forward(150)
    pendown()

    for i in range(8):
        forward(strana)
        left(180 -(180 *(1 - (strana/200))))
        
        


    

exitonclick()
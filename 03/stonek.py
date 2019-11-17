#Jednoduchy program na kreslení

from turtle import forward,right, left, exitonclick, shape, penup, pendown ,setx, sety
penup()
sety(200)
pendown()

for i in range(1):
    left(-90)
    forward(150)
    left(90)
    for i in range(20):
        forward(2)
        left(2)
    
    left(135)
for b in range(20):
    forward(2)
    left(2)
right(90)

        
        
        

    

penup()   
exitonclick()

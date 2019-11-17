#Jednoduchy program na kreslení

from turtle import forward,right, left, exitonclick, shape, penup, pendown ,setx, sety

penup()
sety(200)
pendown()

for i in range(18):
    for i in range(4):
        forward(50)
        left(90)

    left(20)

for i in range(1):
    right(90)
    forward(150)

# Kytička není dokončena chybí ji listy. 
        
        
        

    

penup()   
exitonclick()

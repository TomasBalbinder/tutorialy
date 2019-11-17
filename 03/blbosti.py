#Jednoduchy program na kreslení


from turtle import forward,right, left, exitonclick, shape, penup, pendown
shape("turtle")

for i in range(10):
    forward(50)
    penup()
    forward(50)
    pendown()



exitonclick()

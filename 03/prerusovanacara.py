#Jednoduchy program na kreslení


from turtle import forward,right, left, exitonclick, shape, penup, pendown
shape("turtle")

for i in range(10):
    forward(10)
    penup()
    forward(10)
    pendown()



exitonclick()

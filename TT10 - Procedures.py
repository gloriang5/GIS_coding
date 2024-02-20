import turtle

def square_draw(x,y,sz):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(3):
        turtle.forward(sz)
        turtle.left(120)
        
for y in range (-200,200,20):
    for x in range (-200, 200,20):
        square_draw(x,y,10)

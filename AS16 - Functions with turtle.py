import turtle

wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Turtle meets a function")

tur = turtle.Turtle()
tur.pencolor("pink")
tur.pensize(5)
tur.speed(0)

def square(size, t):
    for i in range(4):
        t.fd(size)
        t.lt(90)
        

##exericse 1
#for i in range(5):
    #square(20, alex)
    #tur.pu()
    #tur.fd(40)
    #tur.pd()

##exercise 2
#size = 20
#for i in range(5):
    #square(size, alex)
    #alex.pu()
    #for j in range(2):
        #tur.rt(90)
        #tur.fd(10)
    #tur.pd()
    #tur.rt(180)
    #size += 20

##exercise 3
def draw_polygon(t, n, sz):
    angle = 180 - ((180*n - 360) / n)
    for i in range(n):
        t.fd(sz)
        t.lt(angle)

#draw_polygon(tur, 8, 50)

##exercise 4
#for i in range (20):
    #square(100, tur)
    #tur.rt(18)

##exercise 5
#length = 20
#tur.pensize(2)
#for i in range(100):
    #tur.fd(length)
    #tur.lt(91) #90 for the first picture
    #length += 5

##exerice 6
def draw_equitriangle(sz, t):
    draw_polygon(t ,3, sz)
    
#draw_equitriangle(120, tur)

##exercise 7
def sum_to(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    return print(sum)

##exercise 8
def area_of_circle(r):
    area = 3.142*(r**2)
    return print(area)

##exericse 9

def draw_star(t):
    for i in range(5):
        t.fd(100)
        t.rt(144)

##exercise 10
tur.pu()
tur.goto(-200, 40)
tur.pd()
for i in range(5):
    draw_star(tur)
    tur.pu()
    tur.fd(350)
    tur.rt(144)
    tur.pd()














    
    

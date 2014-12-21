import turtle
def button(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(x,y+50)
    turtle.goto(x+100,y+50)
    turtle.goto(x+100,y)
    turtle.goto(x,y)
    turtle.end_fill()
    turtle.pu()
def colour(x,y,z):
    turtle.pu()
    turtle.pencolor(z)
    turtle.goto(x,y)
    turtle.pd()
    turtle.begin_fill()
    turtle.goto(x+10, y)
    turtle.goto(x+10, y+10)
    turtle.goto(x,y+10)
    turtle.goto(x,y)
    turtle.end_fill()
    turtle.pu()
def frame(x,y):
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.goto(x+1000, y)
    turtle.goto(x+1000, y+600)
    turtle.goto(x,y+600)
    turtle.goto(x,y)
def starting():
    turtle.speed(0)
    button(-600, -300)
    button(-600, -200)
    button(-600, -100)
    button(-600,0)
    colour(-420, 400, "red")
    colour(-440, 400, "blue")
    colour(-430,400, "green")
    frame(-450,-300) 
    turtle.penup()
    turtle.goto(0,0)
global n
n=1
i=0
def clear():
    turtle.clear()
    button(-600, -300)
    turtle.penup()
    turtle.goto(0,0)
    starting()
what=0
def draw(x,y):
    global what
    if what==0:
        turtle.goto(x,y)
        turtle.pd()
    if what==1:
        turtle.pu()
        turtle.goto(x,y)
        turtle.begin_fill()
        turtle.circle(4)
        turtle.end_fill()
def press(x,y):
    if x<-500 and x>-600 and y<-250 and y>-300:
        global what
        what=1
    if x<-500 and x>-600 and y<-150 and y>-200:
        x=0
    if x>-450 and x<550 and y>-300 and y<300 :
        draw(x,y)
    else:
        turtle.pu()
        turtle.goto(x,y)
turtle.penup()
starting()
global size
size=1
def large():
    global size
    size=size+5
    turtle.pensize(size)
def small():
    global size
    size=size-5
    turtle.pensize(size)
def stoping():
    global i
    if (i==0):
        i=i+1
        turtle.penup()
    else:
        i=i-1
        turtle.pendown()
colors=["red", "blue", "green"]
turtle.onscreenclick(press, btn=1, add=True)
turtle.getscreen().onkeypress(clear, "CapsLock")
turtle.getscreen().listen()
turtle.getscreen().onkeypress(stoping, "Delete")
turtle.getscreen().listen()
turtle.ondrag(turtle.goto, btn=1, add=True)
turtle.getscreen().onkeypress(large, "minus")
turtle.getscreen().listen()
turtle.getscreen().onkeypress(small, "equal")
turtle.getscreen().listen()
turtle.mainloop

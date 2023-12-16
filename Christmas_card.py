import turtle
import random
import time

name = 'Giannis \nPanagiotopoulos'

width = height = 500 
window = turtle.Screen() 
window.setup(width, height) 
window.bgcolor("dim grey") 
window.title("Ho Ho Ho")
sp = 6

def treecirc (colour,xpos,ypos,rad,cir):
    cir.speed("fastest")
    cir.hideturtle()
    cir.color(colour)
    cir.fillcolor(colour)
    cir.up()
    cir.setposition(x= xpos,y=ypos)
    cir.down()
    cir.begin_fill()
    cir.circle(rad, extent=None, steps=None)
    cir.end_fill()

def balls(colour, xpos, ypos,bal):
    bal.hideturtle()
    bal.color(colour)
    bal.fillcolor(colour)
    bal.up()
    bal.setposition(x=xpos, y=ypos)
    bal.down()
    bal.begin_fill()
    bal.circle(11, extent=None, steps=None)
    bal.end_fill()

def string (xpos,st):
    '''
    This function is creating the string of lights above the christmas tree
    '''
    st.hideturtle()
    st.color('black')
    st.up()
    st.setposition(x= xpos,y=260)
    st.down()
    st.circle(180,extent=None, steps=None)

def bulb(x,y,color,bl):
    bl.hideturtle()
    bl.color(color)
    bl.up()
    bl.setposition(x,y)
    bl.down()
    bl.dot(8)

def snowflake (x,y,size,sn):
    '''
    This function is creating the shape of a snowflake
    '''
    sn.penup()
    sn.hideturtle()
    sn.setposition(x,y)
    for ang in range (30,361,60):
        z = sn.pos()
        sn.pendown()
        sn.color('white')
        sn.pensize(size)
        sn.left(ang)
        sn.forward(size*3)
        sn.left(180)
        sn.forward(size)
        sn.left(120)
        sn.forward(size)
        sn.left(180)
        sn.forward(size)
        sn.right(60)
        sn.forward(size)
        sn.up()
        sn.setposition(z[0],z[1])
        sn.setheading(0)
        

def snowflakechangepos (rng,sf,blb):
    '''
    The first part of this function is generating the bulbs and "changes" their colour
    The second part creates a list of 3 elements: x, y, snowflake size.
    After that, it appends the new list in a list of lists
    In the "for loop" it subtracts a constant number from the y coordinate of all the elements in the list
    That`s how we generate the sense of snowfalling
    '''
    for k in range (rng):
        for col in ['yellow','goldenrod']:
            blb = turtle.Turtle() 
            blb.hideturtle()
            xposition = [i for i in range(-480,481,80)]
            yposition = [280,260,280,265,265,280,260,280,265,265,280,260,280]
            for x,y in zip(xposition,yposition): 
                bulb(x,y,col,blb)
    #            window.update()
            for i in range(10):
                listc = []
                listc.append(random.randint(-width,5*width))    # x cor
                listc.append(height)                            # y cor
                listc.append(random.randint(1,3))               # snowflake size
                lst.append(listc)
                sf.hideturtle()
                sf.clear()
                for i in lst:
                    if i[1]<-height or i[0]>width:
                        lst.remove(i)
                    else:
                        i[1] -= sp
                        snowflake(i[0],i[1],i[2],sf)
                window.update()


# Tree

base = turtle.Turtle()
base.hideturtle()
base.speed("fastest")
base.fillcolor('sienna')
base.up()
base.color('sienna')
base.setposition(x= -30,y=-170)
base.down()
base.begin_fill()
base.setposition(x= 30,y=-170)
base.setposition(x= 30,y=-270)
base.setposition(x= -30,y=-270)
base.end_fill()

cir = turtle.Turtle()
cir.hideturtle()
treecirc('dark green',0,-190,600,cir)
treecirc('dim gray',500,-240,510,cir)
treecirc('dim gray',-500,-240,510,cir)
treecirc('green',250,-90,500,cir)
treecirc('green',-250,-90,500,cir)
treecirc('dim gray',470,-170,481,cir)
treecirc('dim gray',-470,-170,481,cir)
treecirc('forest green',200,20,500,cir)
treecirc('forest green',-200,20,500,cir)
treecirc('dim gray',440,-70,501,cir)
treecirc('dim gray',-440,-70,501,cir)

window.tracer(0)

star = turtle.Turtle()
star.hideturtle()
star.fillcolor('gold')
star.up()
star.setposition(x= -25,y=205)
star.begin_fill()
for i in range(5):
    star.forward(50)
    star.right(144)
star.end_fill()

treeballs = turtle.Turtle() 
treeballs.hideturtle()
balls('crimson',150,5,treeballs)
balls('indigo',-150,5,treeballs)
balls('white',190,-100,treeballs)
balls('crimson',-190,-100,treeballs)
balls('indigo',210,-170,treeballs)
balls('yellow',-210,-170,treeballs)
balls('indigo',-50,-120,treeballs)
balls('crimson',60,-140,treeballs)
balls('yellow',20,0,treeballs)
balls('lavender',-15,80,treeballs)


# Ground
ground = turtle.Turtle() 
ground.hideturtle()
ground.fillcolor('white')
ground.up()
ground.setposition(x= -width,y=-height/2)
ground.down()
ground.color('white')
ground.begin_fill()
while ground.xcor()<width:
    ground.speed("fastest")
    ground.pensize(random.randint(10,15))
    ground.forward(5)
ground.setposition(x= width,y=-height)
ground.setposition(x= -width,y=-height)
ground.setposition(x= -width,y=-height/2)
ground.end_fill()

window.update()

# Stringlights
stringlights = turtle.Turtle()
string(-400,stringlights)
string(-200,stringlights)
string(0,stringlights)
string(200,stringlights)
string(400,stringlights)
stringlights.fillcolor('black')
stringlights.up()
stringlights.setposition(x= -1000,y=290)
stringlights.down()
stringlights.color('black')
stringlights.begin_fill()
stringlights.setposition(x= -1000,y=height)
stringlights.setposition(x= 1000,y=height)
stringlights.setposition(x= 1000,y=290)
stringlights.end_fill()
stringlights.hideturtle()



snow = turtle.Turtle()
snow.hideturtle()
bulbs = turtle.Turtle()
bulbs.hideturtle()
lst = []
snowflakechangepos(6,snow,bulbs)

wishes = turtle.Turtle()
wishes.color("dark red") 
wishes.penup() 
wishes.setposition(-300,100) 
wishes.write("Merry Christmas", font=("Comic Sans MS", 40, "bold"), align="center") 
wishes.hideturtle() 
snowflakechangepos(1,snow,bulbs)
wishes.setposition(450, -120) 
wishes.color("peru") 
wishes.write("from", font=("Arial", 20, "italic"), align="right") 
wishes.setposition(450, -185) 
wishes.color("peru") 
wishes.write(name, font=("Arial", 20, "bold italic"), align="right") 
wishes.hideturtle() 

snowflakechangepos(10,snow,bulbs)


turtle.mainloop()
turtle.bye()

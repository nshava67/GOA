from turtle import *


#i want to paint a house

#step one draw a square
speed(30)
width(7)
color("red")
forward (200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("green")
left(90)
forward(120)#height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#draw a window
penup()
goto(20, 180)
pendown()
left(30)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
penup()
goto(135,180)
pendown()
left(90)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
left(90)
forward(45)

exitonclick()
import turtle

#Setup the screen and the turtle
window = turtle.Screen()
window.bgcolor("lightgray")

t = turtle.Turtle()
t.shape("turtle")
t.pensize(5)

#Draw a Red Triangle
t.color("red")
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

#Move to a new spot without leaving a trail
t.penup()
t.forward(150)
t.pendown()

#Draw a Blue Square using a simple loop
t.color("blue")
for _ in range(4):
    t.forward(80)
    t.left(90)

#Keep the window open
window.exitonclick()
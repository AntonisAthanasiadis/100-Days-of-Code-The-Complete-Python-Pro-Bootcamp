import turtle

#create a window for the turtle to draw in
window = turtle.Screen()
window.title("Drawing Turtle!")
window.bgcolor("darkslategray")  # Set a nice background color

#Create our turtle instance and customize it
t = turtle.Turtle()
t.shape("turtle")
t.speed(3)
t.pensize(3)

#Drawing functions
def draw_square(size, color_name):
    t.color(color_name)

    for _ in range(4):
        t.forward(size)
        t.right(90)


def draw_polygon(sides, size, color_name):
    t.color(color_name)

    angle = 360 / sides

    for _ in range(sides):
        t.forward(size)
        t.right(angle)


def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


#Shape 1: A simple blue square
move_to(-200, 100)
draw_square(100, "deepskyblue")

#Shape 2: A small pink triangle (3 sides)
move_to(0, 100)
draw_polygon(3, 80, "hotpink")

#Shape 3: A large yellow hexagon (6 sides)
move_to(150, 150)
draw_polygon(6, 60, "gold")

#Shape 4: A colorful spiral star
move_to(-150, -150)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(30):
    t.color(colors[i % len(colors)])

    t.forward(i * 7)
    t.right(144)

window.exitonclick()
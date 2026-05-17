import random
import turtle

#setup
screen = turtle.Screen()
screen.title("Python Turtle Random Walk")
screen.bgcolor("black")

walker = turtle.Turtle()
walker.shape("turtle")
walker.color("green")
walker.pensize(5)
walker.speed(2)

colors = [
    "red",
    "green",
    "blue",
    "yellow",
    "magenta",
    "cyan",
    "orange",
    "purple",
    "pink",
    "white",
]

directions = [0, 90, 180, 270]

#better error handling
try:
    for _ in range(200):
        walker.color(random.choice(colors))
        walker.setheading(random.choice(directions))
        walker.forward(30)


except turtle.Terminator:
    print("Animation closed by user.")
except Exception as e:
    print(f"Window closed: {e}")

screen.exitonclick()
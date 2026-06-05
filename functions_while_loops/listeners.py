from turtle import Turtle, Screen

tony = Turtle()
screen = Screen()
screen.title("Use WASD to move, click to exit!")
def move_forwards():
    tony.forward(10)
def move_backwards():
    tony.backward(10)
def turn_left():
    new_heading = tony.heading() +10
    tony.setheading(new_heading)
def turn_right():
    new_heading = tony.heading() -10
    tony.setheading(new_heading)

screen.listen()
screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "a", fun = turn_left)
screen.onkey(key = "d", fun = turn_right)



screen.exitonclick()
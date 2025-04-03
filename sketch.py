from turtle import Turtle, Screen

reo = Turtle()
screen = Screen()

def move_forward():
    reo.forward(10)
def move_left():
    reo.left(90)
def move_right():
    reo.right(90)
def move_back():
    reo.forward(-10)
def clear():
    reo.clear()
    reo.reset()

screen.listen()

screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Left", fun=move_left)
screen.onkey(key="Right", fun=move_right)
screen.onkey(key='c', fun=clear)
screen.onkey(key='Down', fun=move_back)



screen.exitonclick()

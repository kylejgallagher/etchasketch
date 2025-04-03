from turtle import Turtle, Screen

reo = Turtle()
rui = Turtle()

rui.color("dark blue")
reo.color("green")

screen = Screen()

def move_forward():
    reo.forward(10)
def move_left():
    reo.left(90)
def move_right():
    reo.right(90)
def move_back():
    reo.forward(-10)

def move_forward_rui():
    rui.forward(10)
def move_left_rui():
    rui.left(90)
def move_right_rui():
    rui.right(90)
def move_back_rui():
    rui.forward(-10)


def clear():
    reo.clear()
    reo.reset()
    rui.clear()
    rui.reset()

screen.listen()

screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Left", fun=move_left)
screen.onkey(key="Right", fun=move_right)
screen.onkey(key='c', fun=clear)
screen.onkey(key='Down', fun=move_back)

screen.onkey(key="w", fun=move_forward_rui)
screen.onkey(key="a", fun=move_left_rui)
screen.onkey(key="d", fun=move_right_rui)
screen.onkey(key='c', fun=clear)
screen.onkey(key='s', fun=move_back_rui)


screen.exitonclick()

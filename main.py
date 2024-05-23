from turtle import Turtle, Screen

turtle1 = Turtle()
screen = Screen()
screen.listen()


def move_up():
    turtle1.forward(20)


def move_down():
    turtle1.backward(20)


def move_right():
    turtle1.right(20)


def move_left():
    turtle1.left(20)


def clear_screen():
    turtle1.clear()
    turtle1.penup()
    # Method-1
    turtle1.setposition(0, 0)
    turtle1.setheading(0)
    # Method-2
    # turtle1.home()
    turtle1.pendown()


screen.onkey(key='w', fun=move_up)
screen.onkey(key='s', fun=move_down)
screen.onkey(key='d', fun=move_right)
screen.onkey(key='a', fun=move_left)
screen.onkey(key='c', fun=clear_screen)

screen.exitonclick()

import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Mandala")

board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()



colors = ["red", "orange", "yellow", "lime", "cyan", "violet", "pink", "white"]
for i in range(80):
    board.color(colors[i % len(colors)])
    board.width(2)
    board.forward(i * 2)
    board.right(91)
    
board.penup()
board.goto(0, -60)
board.setheading(90)
board.pendown()
board.color("gold", "yellow")
board.begin_fill()
for i in range(5):
    board.forward(130)
    board.right(144)
board.end_fill()    


turtle.done()
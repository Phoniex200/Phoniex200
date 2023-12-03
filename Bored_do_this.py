import turtle
import tkinter as tk
import tkinter.simpledialog 
from tkinter import colorchooser 

# Set up the game window
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Create the paddles
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Create the ball
ball = turtle.Turtle()
ball.speed(300)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = -0.5

# Function to move paddle A up
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
    paddle_a.sety(y)

# Function to move paddle A down
def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 20
    paddle_a.sety(y)

# Function to move paddle B up
def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
    paddle_b.sety(y)

# Function to move paddle B down
def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 20
    paddle_b.sety(y)

# movment
buttona=tk.Button(text="Up", command=paddle_a_up)
buttona.pack()
buttona.place(x=0, y=1055)

button_a=tk.Button(text="Down", command= paddle_a_down)
button_a.pack()
button_a.place(x=0, y=1200)

buttonb=tk.Button(text="Up", command=paddle_b_up)
buttonb.pack()
buttonb.place(x=610, y=1055)

button_b=tk.Button(text="Down", command= paddle_b_down)
button_b.pack()
button_b.place(x=610, y=1200)

#settings
def settings():
    ask=tkinter.simpledialog.askstring("Input", "1,change ball speed or 2,bgcolor or 3,paddle color: ")
    if ask=="1":
      num1=tkinter.simpledialog.askfloat("Input", "Enter number: ")
      num2=tkinter.simpledialog.askfloat("Input", "Enter number with - example -0.5: ")
      ball.dx=num1
      ball.dy=num2
    elif ask=="2":
      color=colorchooser.askcolor()[1]
      if color:
        window.bgcolor(color)
    elif ask=="3":
      what_paddle=tkinter.simpledialog.askstring("Input", "paddle_a or paddle_b: ")
      if what_paddle=="paddle_a":
        a=colorchooser.askcolor()[1]
        if a:
          paddle_a.color(a)
      if what_paddle=="paddle_b":
        b=colorchooser.askcolor()[1]
        if b:
          paddle_b.color(b)    
    
button1=tk.Button(text="Settings", command=settings)
button1.pack()
button1.place(x=0, y=0)

#point system
pointa=0
point_a=turtle.Turtle()
point_a.ht()
point_a.color("white")
point_a.penup()
point_a.goto(-350, 300)
point_a.write(pointa, font=("Arial", 21, "normal"))

pointb=0
point_b=turtle.Turtle()
point_b.ht()
point_b.color("white")
point_b.penup()
point_b.goto(298, 300)
point_b.write(pointb, font=("Arial", 21, "normal"))

def ai_control():
    if ball.ycor() > paddle_a.ycor():
        paddle_a.sety(paddle_a.ycor() + 10)
    elif ball.ycor() < paddle_a.ycor():
        paddle_a.sety(paddle_a.ycor() - 10)

# Main game loop
while True:
    window.update()
    ai_control()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for collisions with the borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        pointa=pointa+1
        point_a.clear()
        point_a.write(pointa, font=("Arial", 21, "normal"))
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        pointb=pointb+1
        point_b.clear()
        point_b.write(pointb, font=("Arial", 21, "normal"))
        

    # Check for collisions with the paddles
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        
turtle.mainloop()

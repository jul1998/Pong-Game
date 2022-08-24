from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, x_cor, y_cor): # It creates paddles
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(x_cor, y_cor)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self): # It makes paddles to move upwards
        new_y = self.ycor() + 20 # It will sum both the paddle Y coordinate and 20 in order to move 20 pixels everytime
        self.goto(self.xcor(), new_y)

    def down(self): # It makes paddles to move downwards
        new_y = self.ycor() - 20 # It will subtract both the paddle Y coordinate and 20 in order to move 20 pixels everytime
        self.goto(self.xcor(), new_y)
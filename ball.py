from turtle import Turtle


class Ball(Turtle):

    def __init__(self): # It creates ball
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_cor = 10
        self.y_cor = 10

    def move_ball(self):
        x_cor = self.xcor() + self.x_cor # This moves ball within x-axis
        y_cor = self.ycor() + self.y_cor # This moves bal within y-axis
        self.goto(x_cor, y_cor)

    def bounce_y(self): # It causes ball to bounce within y-axis
        self.y_cor *= -1

    def colission_with_r_paddle(self): # It makes ball to bounce when hits right paddle
        self.x_cor = - (abs(self.x_cor))

    def colission_with_l_paddle(self): # It makes ball to bounce when hits left paddle
        self.x_cor = (abs(self.x_cor))

    def reset_ball(self): # It resets ball position and makes ball go to opposite direction once it spawns again
        self.goto(0, 0)
        self.x_cor *= -1
from turtle import Turtle

class Score(Turtle):
    def __init__(self): # Create turtle for being showed as scoreboard
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.paddle_scores() # Show right and paddle scores

    def paddle_scores(self):
        self.clear()
        self.goto(-180, 240)
        self.write(self.l_score, move=False, align='center', font=('Arial', 40, 'normal'))
        self.goto(180, 240)
        self.write(self.r_score, move=False, align='center', font=('Arial', 40, 'normal'))


    def update_l_paddle_score(self): # Update left paddle score
        self.l_score += 1

    def update_r_paddle_score(self): # Update right paddle score
        self.r_score += 1


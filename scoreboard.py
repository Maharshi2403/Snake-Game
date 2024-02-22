from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,270)
        self.color("White")
        self.score = 0
        self.write(f"Score: {self.score}",move=False,align='center', font=('Arial', 15, 'normal'))
        self.hideturtle()

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}",move=False,align='center', font=('Arial', 15, 'normal'))
        self.hideturtle()

    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER",move=False,align='center', font=('Arial', 24, 'normal'))
        self.hideturtle()
    




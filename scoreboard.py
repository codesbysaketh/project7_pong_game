from turtle import Turtle

align = "center"
font = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.goto(0, 260)
        self.print_score()

    def print_score(self):
        self.write(f"{self.l_score} | {self.r_score}", False, align, font)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.print_score()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.print_score()

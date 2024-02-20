from turtle import Turtle
MOVE = True
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        file = open("data.txt")
        self.highscore = int(file.read())
        self.color = "blue"
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write("Score: " + str(self.score) + " High Score: " + str(self.highscore), MOVE, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            file = open("data.txt", mode="w")
            file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", MOVE, ALIGNMENT, FONT)

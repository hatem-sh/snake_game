from turtle import Turtle

FONT = ("Arial", 24, "normal")
ALIGN = "center"

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.write(f"Your score: {self.score} ", False, ALIGN, FONT)


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over ", False, ALIGN, FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Your score: {self.score} High score: {self.high_score} ", False, "center", ("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
            self.update_scoreboard()
        self.score = 0
        self.update_scoreboard()


    def score_increase(self):
        self.score += 1
        # with open("data.txt") as data:
        #     data.write("self.score")
        self.update_scoreboard()

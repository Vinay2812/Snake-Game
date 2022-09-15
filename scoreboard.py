from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        # color, goto.. everything should be always before write, then only color n position will be shown
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=260)
        self.write(
            f"Score : {self.score}",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def increment_score(self):
        self.score += 1
        self.clear()
        self.write(
            f"Score : {self.score}",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def game_over(self):
        self.goto(0, 0)
        self.write(
            "Game Over",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")

class Scoreboard(Turtle):
    
    def __init__(self, player1_name, player2_name):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 200)
        self.write(f"{self.player1_name}: {self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(200, 200)
        self.write(f"{self.player2_name}: {self.r_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self, winner_name):
        self.color("red")
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=("Courier", 50, "bold"))
        self.goto(0, -60)
        self.write(f"{winner_name} wins!", align=ALIGNMENT, font=("Courier", 40, "normal"))

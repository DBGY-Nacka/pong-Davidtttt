from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    player1_name = screen.textinput("Player 1", "Enter your name:")
    player2_name = screen.textinput("Player 2", "Enter your name:")

    left_paddle = Paddle(position=(-350, 0))
    right_paddle = Paddle(position=(350, 0))

    ball = Ball()

    scoreboard = Scoreboard(player1_name, player2_name)

    screen.listen()
    screen.onkey(left_paddle.move_up, "w")
    screen.onkey(left_paddle.move_down, "s")
    screen.onkey(right_paddle.move_up, "Up")
    screen.onkey(right_paddle.move_down, "Down")

    game_is_on = True
    while game_is_on:
        time.sleep(0.05)
        screen.update()

        ball.move()

        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.bounce_y()

        if (ball.distance(right_paddle) < 40 and ball.xcor() > 330) or (ball.distance(left_paddle) < 40 and ball.xcor() < -330):
            ball.bounce_x()

        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()

        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()

        if scoreboard.l_score == 5:
            scoreboard.game_over(player1_name)
            game_is_on = False

        if scoreboard.r_score == 5:
            scoreboard.game_over(player2_name)
            game_is_on = False

    screen.update()
    screen.textinput("Game Over", "Press Enter to exit")

if __name__ == "__main__":
    main()


import turtle
from turtle import Screen
from snake_food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

UP_HEIGHT = 300
DOWN_HEIGHT = -287
LEFT_WIDTH = -300
RIGHT_WIDTH = 287

screen = Screen()


def snake_game():
    screen.clear()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    # it removes the animation and
    # update() is used for refreshing with the position without animations
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score_board = Scoreboard()

    screen.listen()

    screen.onkey(fun=snake.turn_up, key="Up")
    screen.onkey(fun=snake.turn_right, key="Right")
    screen.onkey(fun=snake.turn_down, key="Down")
    screen.onkey(fun=snake.turn_left, key="Left")

    game_is_on = True
    while game_is_on:
        # update is done in order to remove the animations and refresh every 0.1 sec
        screen.update()
        time.sleep(0.1)
        snake.move()

        # detect collision with food
        if snake.head.distance(food) < 15:
            snake.extend()
            score_board.increment_score()
            food.new_food()

        # detect collision with body
        def collision_with_body():
            # This can be avoided with slicing, since we don't want head to be considered

            # for i in range(1, len(snake.segments)):
            #     if snake.head.distance(snake.segments[i].position()) < 10:
            #         return True
            # return False
            for segment in snake.segments[1:]:
                if snake.head.distance(segment.position()) < 10:
                    return True
            return False

        # detect collosion with wall
        if (
            snake.head.xcor() > RIGHT_WIDTH
            or snake.head.xcor() < LEFT_WIDTH
            or snake.head.ycor() > UP_HEIGHT
            or snake.head.ycor() < DOWN_HEIGHT
        ) or collision_with_body():
            score_board.game_over()
            game_is_on = False


snake_game()
while True:
    answer = turtle.textinput(title="Snake Game", prompt="Do you want to play again?")
    if answer is None or answer.lower().startswith("n"):
        break
    else:
        snake_game()

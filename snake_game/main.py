from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score_board
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()
score_board = Score_board()
score = 0
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
is_game_on = True


while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score_board.update_scoreboard()
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.score_increase()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()


screen.exitonclick()

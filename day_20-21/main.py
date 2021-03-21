from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snek")
screen.tracer(0)

snake = Snake()
food = Food()
sb = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_running = True
while game_is_running:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        sb.increase_score()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() <-290:
        game_is_running = False
        sb.game_over()

    for seg in snake.snek[1:]:
        if snake.head.distance(seg) < 10:
            game_is_running = False
            sb.game_over()

screen.exitonclick()
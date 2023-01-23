from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

#create a window
screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(0)

snake = Snake()

def quit():
    global game_is_on
    game_is_on = False

#snake control

screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
screen.onkey(quit, "q")

#food
food = Food()

#scoreboard
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    scoreboard.upgrade_scoreboard()

    #detect collision with food:
    if snake.snake_head.distance(food) < 20:
        food.spawn()
        scoreboard.increase_point()
        snake.increase_tail()

    #detect collision with wall:
    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290:
        scoreboard.reset()
        snake.reset()
   


    if snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290:
        scoreboard.reset()
        snake.reset()
    

    #detect collision with your own tail

    for segment in snake.segments[1:len(snake.segments)]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()



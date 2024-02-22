from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen  = Screen()
screen.setup(height=600, width=600)
screen.title("My Snack Game")
screen.bgcolor("black")
screen.tracer(0)


fn = Snake()
fn.add_portion()
food = Food()
score = Score()

screen.listen()
screen.onkey(fn.Up,"W")
screen.onkey(fn.Down,"S")
screen.onkey(fn.Right,"D")
screen.onkey(fn.Left,"A")
screen.update()
is_gameOn = True
while is_gameOn: 
    screen.update()
    time.sleep(0.1)
    fn.move()

    # detacting collision with food
    if fn.segments[0].distance(food) < 15:
       food.refresh()
       score.refresh_score()
       fn.extend_Snake()
   
    #detacting collision with wall
    if fn.segments[0].xcor() >300 or fn.segments[0].ycor() >300 or fn.segments[0].ycor() <-300 or fn.segments[0].xcor() <-300:
        score.gameOver()
        is_gameOn = False

    #detacting 
    for segment in fn.segments:
        if segment == fn.segments[0]:
            pass
        elif fn.segments[0].distance(segment) <5:
            score.gameOver()
            is_gameOn =False
    


screen.exitonclick()

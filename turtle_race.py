from turtle import Turtle, Screen
import random

game_is_on = False
x = -225
y = 125
colors = ["red", "green", "purple", "black", "orange", "brown"]
racers = []
for i in range(0, 6):
    player = Turtle(shape="turtle")
    player.color(colors[i])
    player.penup()
    player.goto(x=x, y=y)
    y -= 50
    racers.append(player)

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Your choice for the winner", prompt="Choose the turtle color which you want to "
                                                                          "bet upon.")
if user_choice:
    game_is_on = True

while game_is_on:
    for racer in racers:
        steps = random.randint(0, 10)
        racer.forward(steps)
        racer.speed(7)
        if racer.xcor() >= 250:
            winner = racer.color()[0]
            if winner == user_choice:
                print(f"Congratulations!, your racer: {winner} turtle is the winner. ")
            else:
                print(f"Sorry your racer has lost. The winner of the race is: {winner} turtle.")
            game_is_on = False

screen.exitonclick()

import turtle as t

screen = t.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")


class Paddle(t.Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5, 1)
        self.goto(position)
        self.showturtle()
        self.speed("fastest")

    def go_up(self):
        new_y = self.ycor() + 35
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 35
        self.goto(self.xcor(), new_y)


class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("slowest")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def collision(self):
        self.y_move *= -1

    def bonk(self):
        self.x_move *= -1

    def reset(self):
        self.hideturtle()
        self.speed("fast")
        self.goto(0, 0)
        self.speed("slowest")
        self.showturtle()

    def clear(self):
        self.clear()


class LeftScoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-200, 270)
        self.write(f"{self.score}", align="center", font=("Arial", 15, "normal"))

    def counter(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align="center", font=("Arial", 15, "normal"))


class RightScoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(200, 270)
        self.write(f"{self.score}", align="center", font=("Arial", 15, "normal"))

    def counter(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align="center", font=("Arial", 15, "normal"))


class GlobalCounter(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.counter = 0

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 30, "normal"))

    def turns(self):
        self.counter += 1


lpad = Paddle((-350, 0))
rpad = Paddle((350, 0))

scoreboard = GlobalCounter()

ball = Ball()

rscore = RightScoreboard()
lscore = LeftScoreboard()

screen.listen()

screen.onkey(rpad.go_up, "Up")
screen.onkey(rpad.go_down, "Down")

screen.onkey(lpad.go_up, "w")
screen.onkey(lpad.go_down, "s")

game_on = True
while game_on:
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.collision()

    elif ball.distance(lpad) < 30 or ball.distance(rpad) < 30:
        ball.bonk()

    elif ball.xcor() > 400:
        lscore.counter()
        scoreboard.turns()
        ball.reset()
        ball.move()

    elif ball.xcor() < -400:
        rscore.counter()
        scoreboard.turns()
        ball.reset()
        ball.move()

    elif scoreboard.counter >= 10:
        game_on = False
        ball.hideturtle()
        scoreboard.game_over()

screen.mainloop()

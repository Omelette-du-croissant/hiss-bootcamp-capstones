import turtle as t
import random
import time

colors = ["red", "orange", "yellow", "green", "blue", "purple", "IndianRed", "lime", "aqua"]
font = ("Arial", 20, "bold")


class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)

    def go_to_start(self):
        self.goto(0, -280)

    def finish_line(self):
        if self.ycor() > 275:
            return True
        else:
            return False


class Cars(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.step = 0

    def make_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = t.Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(colors))

            random_y = random.randint(-245, 245)
            new_car.goto(310, random_y)

            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(2 + self.step)

            if car.xcor() < -400:
                car.hideturtle()

    def increase_speed(self):
        self.step += 1


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-220, 260)
        self.write(arg=f"Level: {self.current_level}", align="center", font=font)
        self.current_level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align="center", font=font)


screen = t.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")

car_factory = Cars()

score = Scoreboard()

game_on = True
while game_on:
    time.sleep(0.05)
    screen.update()

    # Create and move car
    car_factory.make_car()
    car_factory.move()

    # Detect collision with car
    for car in car_factory.all_cars:
        if player.distance(car) < 21:
            score.game_over()
            game_on = False

    # Detect successful crossing and speed up cars
    if player.finish_line():
        player.go_to_start()
        car_factory.increase_speed()
        score.update_scoreboard()


screen.mainloop()

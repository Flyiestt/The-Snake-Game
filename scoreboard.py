from turtle import  Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        with open('data.txt', mode='r') as file:
            self.high_score = int(file.read())
        self.color('white')
        self.penup()
        self.goto(0, 265)
        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER.", align='center', font=('Arial', 24, 'normal'))

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='center', font=('Arial', 24, 'normal'))

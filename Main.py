import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def play(self):
        print("Time to play")
        self.progress += 0.12
        self.gladness -= 5

    def sleep(self):
        print("I will sleep")
        self.gladness += 3

    def eat(self):
        print("I want eat")
        self.gladness += 5
        self.progress = 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False
        return self.alive

    def end_of_day(self, day):
        print(f"{'='*20} Day {day} {'='*20}")
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self):
        day = 1
        while day <= 365 and self.alive:
            print(f"{'='*20} Day {day} {'='*20}")
            live_cube = random.randint(1, 3)
            if live_cube == 1:
                self.play()
            elif live_cube == 2:
                self.sleep()
            elif live_cube == 3:
                self.eat()
            self.end_of_day(day)
            self.is_alive()
            day += 1
        if day > 365:
            print("One year has passed.")


cat = Cat("Whiskers")
cat.live()

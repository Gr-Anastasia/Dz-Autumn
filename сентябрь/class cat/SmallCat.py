from Cat import Cat
from Timer import count_time

class SmallCat(Cat):
    def __init__(self):
        pass

    @count_time
    def eat(self):
        print("Я маленький котёнок, я ем")

    def sleep(self):
        print("Я маленький котёнок, я сплю")

    def run(self):
        print("Я маленький котёнок, я бегаю")

    def cati(self):
        pass
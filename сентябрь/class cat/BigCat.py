from Cat import Cat
from Timer import count_time

class BigCat(Cat):
    def __init__(self):
        pass

    @count_time
    def eat(self):
        print("Я большой кот, я ем")

    @count_time
    def sleep(self):
        print("Я большой кот, я сплю")

    @count_time
    def run(self):
        print("Я большой кот, я бегаю")

    def cati(self):
        pass
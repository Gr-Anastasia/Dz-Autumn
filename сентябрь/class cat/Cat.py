import abc

class Cat(abc.ABC):
    @abc.abstractmethod
    def cati(self):
        pass

    def eat(self):
        print("Кот ест")

    def sleep(self):
        print("Кот спит")

    def run(self):
        print("Кот бежит")
class Library:
    def __init__(self, name, adress, count):
        self.name = name
        self.__adress = adress
        self.__count = count

    def get_count(self):
        return self.__count

    def __add__(self, other):
        return self.__count + other

    def __radd__(self, other):
        return self.__count + other

    def __sub__(self, other):
        return self.__count - other

    def __rsub__(self, other):
        return self.__count - other

    def __imul__(self, other):
        return self.__count += other

    def __isub__(self, other):
        return self.__count -= other

    def __lt__(self, other):
        return self.__count < other

    def __le__(self, other):
        return self.__count <= other

    def __eq__(self, other):
        return self.__count == other

    def __ne__(self, other):
        return self.__count != other

    def __ge__(self, other):
        return self.__count >= other

    def __gt__(self, other):
        return self.__count > other



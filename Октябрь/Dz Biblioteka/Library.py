class Library:
    def __init__(self, name, address, count):
        self.name = name
        self.__address = address
        self.__count = count

    def get_count(self):
        return self.__count

    def get_address(self):
        return self.__address

    def __add__(self, other):
        return self.__count + other

    def __radd__(self, other):
        return other + self.__count

    def __sub__(self, other):
        return self.__count - other

    def __rsub__(self, other):
        return other - self.__count

    def __iadd__(self, other):
        self.__count += other
        return self

    def __isub__(self, other):
        self.__count -= other
        return self

    def __lt__(self, other):
        return self.__count < other

    def __gt__(self, other):
        return self.__count > other

    def __le__(self, other):
        return self.__count <= other

    def __ge__(self, other):
        return self.__count >= other

    def __eq__(self, other):
        return self.__count == other

    def __ne__(self, other):
        return self.__count != other

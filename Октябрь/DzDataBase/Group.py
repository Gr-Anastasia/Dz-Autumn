class Group:
    group_id = 0

    @classmethod
    def autoincrement(cls):
        cls. group_id += 1
        return cls. group_id

    def __init__(self, name):
        self.__id = Group.autoincrement()
        self.name = name

    def get_id(self):
        return self.__id

it_1 = Group(name="51Q")
bg_1 = Group(name="51B")
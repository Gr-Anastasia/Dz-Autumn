class Category:
    category_id = 0

    @classmethod
    def autoincrement(cls):
        cls.category_id += 1
        return cls.category_id

    def __init__(self, name):
        self.__category_id = Category.autoincrement()
        self.name = name


# cosmetic = Category("Cosmetic")

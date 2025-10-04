class Category:
    __category_id = 0

    @classmethod
    def autoincrement(cls):
        cls.__category_id += 1
        return cls.__category_id

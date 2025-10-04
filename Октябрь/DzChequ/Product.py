from Category import Category

class Product:
    product_id = 0
    # kit = dict()

    @classmethod
    def autoincrement(cls):
        cls.product_id += 1
        return cls.product_id

    def __init__(self, name, price, category):
        self.__product_id = Product.autoincrement()
        self.name = name
        self.__price = price
        self.category = category
        self.kit = dict()

    def get_price(self):
        return self.__price

    def get_product(self):
        return self.name

    def get_category(self):
        return self.category.name

    def change_price(self, new_price):
        if new_price <= 0:
            raise ValueError("Это отрицательное число")
        self.__price = new_price
        return self.__price

    def add_kit(self, product, price, category):
        self.kit[product] = (price, category)
        return self.kit


# mascara = Category("Cosmetic")
# lipstick = Category("Lipstick")
#
# mascara_brown = Product("RAD", 500, mascara)
# lipstick_red =Product("Love Generation", 700, lipstick)
# lipstick_sparkl = Product("Divage", 600, lipstick)
#
# mascara_brown.get_price()
# mascara_brown.change_price(2000)
# lipstick_red.change_price(500)
# lipstick_sparkl.change_price(800)
#
# mascara_brown.add_kit(mascara_brown.name,
#                       mascara_brown.get_price())




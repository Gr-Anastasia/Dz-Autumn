from datetime import date
import random
from Category import Category
from Product import Product

class Receipt:
    receipt_id = 0
    unic_control_sum = dict()

    @classmethod
    def autoincrement(cls):
        cls.receipt_id += 1
        return cls.receipt_id

    def __init__(self):
        self.__receipt_id = Receipt.autoincrement()
        self.__control_sum = dict()
        self.product_list = list()

    def get_receipt_id(self):
        return self.__receipt_id

    def get_data(self):
        today = date.today()
        return today

    def get_control_sum(self):
        control_summa = random.randint(100000, 200000)
        if control_summa in Receipt.unic_control_sum.values():
            control_summa = random.randint(100000, 200000)
        else:
            self.__control_sum[self.__receipt_id] = control_summa
            Receipt.unic_control_sum.update(self.__control_sum)
        return self.__control_sum

    def content_product_list(self, product):
        self.product_list.append(product)
        return self.product_list


mascara = Category("Cosmetic")
lipstick = Category("Lipstick")

ch1 = Receipt()
ch2 = Receipt()

mascara_brown = Product("RAD", 500, mascara)
lipstick_red = Product("Love Generation", 700, lipstick)
lipstick_sparkl = Product("Divage", 600, lipstick)

mascara_brown.change_price(2000)
lipstick_red.change_price(500)
lipstick_sparkl.change_price(800)

ch1_center = f"Ваш товарный чек: {ch1.get_receipt_id()}"
print(ch1_center.center(50))
print(f"Дата: {ch1.get_data()}")
print(f"Контрольная сумма: {ch1.get_control_sum()}")
ch1.content_product_list(mascara_brown.add_kit(mascara_brown.name,
                                               mascara_brown.get_price(),
                                               mascara_brown.get_category()))
print(f"Список товаров (бренд/цена/категория): {ch1.content_product_list
                                                (lipstick_red.add_kit(lipstick_red.name,
                                                                        lipstick_red.get_price(),
                                                                        lipstick_red.get_category()
                                              ))}")

ch2_center = f"Ваш товарный чек: {ch2.get_receipt_id()}"
print(ch2_center.center(50))
print(f"Дата: {ch2.get_data()}")
print(f"Контрольная сумма: {ch2.get_control_sum()}")
print(f"Список товаров (бренд/цена/категория): {ch2.content_product_list
                                                (lipstick_sparkl.add_kit(lipstick_red.name,
                                                                         lipstick_sparkl.get_price(),
                                                                         lipstick_sparkl.get_category()
                                              ))}")

# print(Receipt.unic_control_sum)



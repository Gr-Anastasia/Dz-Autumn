class Product:
    __product_id = 0

    @classmethod
    def autoincrement(cls):
        cls.__product_id += 1
        return cls.__product_id

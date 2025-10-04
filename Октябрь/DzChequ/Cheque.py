class Сheque:
    __cheque_id = 0

    @classmethod
    def autoincrement(cls):
        cls.__cheque_id  += 1
        return cls.__cheque_id





import time

def count_time(func):
    def count(*args):
        start = time.time()
        x = func(*args)
        end = time.time()
        res = end - start
        res2 = res * 1000
        return res2
    return count

class MutableString:
    def __init__(self, word, elem):
        self.string = list(word)
        self.elem = elem

    # @count_time
    def replace_elem(self, index):
        self.string[index] = self.elem
        return ''.join(self.string)

winter = MutableString("Winter", "k")
print("Замена 2 индекса слова 'Winter' на букву 'k': \n", winter.replace_elem(2))

# end = time.time()
# res = end - start
# res2 = res * 1000
# print(res2)



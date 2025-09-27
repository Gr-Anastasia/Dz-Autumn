import time

def count_time(func):
    def count(*args):
        start = time.time()
        function = func(*args)
        end = time.time()
        res = end - start
        res2 = res * 1000
        print(f"Время выполнения функции {res2} милисекунд")
        return function
    return count
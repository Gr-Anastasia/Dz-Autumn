line = input("Введите строки для записи в файл 'file_for_python.txt': ")

# line = "Пришла осень"
# line = '123'

with open('C:/Users/User/PycharmProjects/file_for_python.txt', 'w') as f:
    if line != '123':
        f.write(line)
        print("Строка записана в файл 'file_for_python.txt'")
    else:
        raise TypeError("Недопустимая строка для записи")


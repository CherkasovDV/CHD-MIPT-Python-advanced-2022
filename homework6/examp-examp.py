L = [88, 567, 988]

# 2. Запись файла
# 2.1. Открыть файл для записи
f = open('examp-examp.bin', 'wb')

# 2.2. Обход списка и запись данных в файл
for item in L:
    # добавить символ '\n', чтобы можно было распознать числа
    s = str(item) + '\n'

    # Метод encode() - конвертирует строку в последовательность байт
    bt = s.encode()
    f.write(bt)
f.close();

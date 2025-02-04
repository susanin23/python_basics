"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
# Приветственное сообщение
print("Программа перевода секунд в формат ЧЧ:ММ:СС\n\n")

# Создадим функцию ввода числа и проверки типа
def input_and_check_num(text):
    temp_in = input(text)
    while True:
        try:
            temp_in = abs(int(temp_in))
            return temp_in

        except Exception:
            print('Введите целое число ')
            temp_in = input()
            continue

# Для корректной работы цикла, объявляем переменную
in_sec = 1

while in_sec != 0:
    # Ввод исходных данных
    in_sec = input_and_check_num("Введите значение секунд для преобразования (0-завершение программы): ")

    # Арифметические преобразования и цикл
    calc_hours = in_sec // (60 * 60)
    calc_minuts = (in_sec - (calc_hours * 60 * 60))//60
    calc_sec = in_sec - calc_minuts * 60 - calc_hours * 60 * 60

    # Вывод результата на экран
    print(f"В {in_sec} секундах {calc_hours} часов {calc_minuts} минут {calc_sec} секунд")
    
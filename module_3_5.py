def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])

    # Если цифра одна, просто возвращаем её — больше умножать не на что
    if len(str_number) == 1:
        return first

    # Умножаем первую цифру на результат вызова функции с остальными цифрами
    return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(40203)
print(result)
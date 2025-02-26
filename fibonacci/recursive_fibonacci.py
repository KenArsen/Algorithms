def fibonacci(n):
    """
    Вычисляет n-е число Фибоначчи с использованием рекурсии.

    :param n: Порядковый номер числа Фибоначчи (целое число).
    :return: n-е число Фибоначчи.
    """
    # Базовый случай: 1-е число Фибоначчи равно 0
    if n == 1:
        return 0
    # Базовый случай: 2-е число Фибоначчи равно 1
    if n == 2:
        return 1
    # Рекурсивный случай: F(n) = F(n-1) + F(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)


# Пример использования функции
n = int(input("Введите число: "))
fibonacci_number = fibonacci(n)
print(f"{n}-е число Фибоначчи: {fibonacci_number}")

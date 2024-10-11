from custom_types import Number, NumericalMethod, OptimizationFnReturnValue

def bit_search(fn: NumericalMethod, a: Number, b: Number, eps: Number) -> OptimizationFnReturnValue:
    """
    Находит минимум функции с помощью метода поразрядного поиска.

    Параметры:\n
        fn (NumericalMethod): Функция, для которой необходимо найти минимум.\n
        a (Number): Левая граница интервала, в котором ищется минимум.\n
        b (Number): Правая граница интервала, в котором ищется минимум.\n
        eps (Number): Точность поиска (порог для завершения).\n

    Возвращает:\n
        OptimizationFnReturnValue: Словарь с координатами минимума. 
                                Ключ 'x' — значение аргумента, при котором достигается минимум.
                                Ключ 'y' — значение функции в точке минимума.

    Исключения:\n
        ValueError: Если eps <= 0 (некорректное значение точности).

    Примеры:
    >>> def f(x):
    ...     return (x - 3) ** 2
    >>> result = bit_search(f, 0, 6, 0.01)
    >>> print(result)
    {'x': 3.0, 'y': 0.0}
    """
    if eps <= 0:
        raise ValueError("Параметр eps должен быть положительным.")

    h = (b - a) / 4
    x_0 = a
    y_0 = fn(x_0)
    while True:
        x_1 = x_0 + h
        y_1 = fn(x_1)
        if y_0 > y_1:
            x_0 = x_1
            y_0 = y_1
            if a < x_0 < b: continue
        if x_0 <= a:
            h /= 4
            x_0 = a + h
        elif x_1 >= b:
            h = -h / 4
            x_0 = b + h
        if abs(h) <= eps:
            return {'x': x_0, 'y': fn(x_0)}
        else:
            x_0 = x_1
            y_0 = y_1
            h = -h / 4


if __name__ == "__main__":
    input_fn = lambda x: x ** 2 - 2 * x + 16 / (x - 1) - 13
    a, b = 2, 5
    eps = 10 ** -3
    res = bit_search(input_fn, a, b, eps)
    print(f'x: {res['x']}, y: {res['y']}')

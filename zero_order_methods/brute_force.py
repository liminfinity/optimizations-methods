from custom_types import Number, NumericalMethod, OptimizationFnReturnValue
from math import cos

def brute_forse(
    fn: NumericalMethod, interval: tuple[Number, Number], n: Number
) -> OptimizationFnReturnValue:
    """
    Находит минимум функции с помощью метода перебора.

    Параметры:\n
        fn (NumericalMethod): Функция, для которой необходимо найти минимум.\n
        inerval (tuple[Number, Number]): Интервал, в котором ищется минимум.\n
        n (Number): Количество точек на интервале.\n

    Возвращает:\n
        OptimizationFnReturnValue: Словарь с координатами минимума.
                                Ключ 'x' — значение аргумента, при котором достигается минимум.
                                Ключ 'y' — значение функции в точке минимума.


    Примеры:
    >>> def f(x):
    ...     return (x - 3) ** 2
    >>> result = brute_forse(f, interval=(0, 6), n=1000)
    >>> print(result)
    {'x': 3.0, 'y': 0.0}
    """

    a, b = interval
    x_values = [a + (b - a) / (n + 1) * i for i in range(1, n + 1)]
    y_values = [fn(x) for x in x_values]

    min_index = y_values.index(min(y_values))
    return {"x": x_values[min_index], "y": y_values[min_index]}


if __name__ == "__main__":
    fn = lambda x: cos(x) / x**2
    a, b = 9, 11
    n = 1000
    res = brute_forse(fn, interval=(a, b), n=n)
    print(f"x: {res['x']}, y: {res['y']}")

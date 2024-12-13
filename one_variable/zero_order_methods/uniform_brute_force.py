from custom_types import Number, NumericalMethod, OptimizationFnReturnValue
from math import cos
from lipschitz_constant import lipschitz_constant


def uniform_brute_force(
    fn: NumericalMethod, interval: tuple[Number, Number], L: Number, eps: Number
) -> OptimizationFnReturnValue:
    """
    Находит минимум функции с помощью метода равномерного перебора.

    Параметры:\n
        fn (NumericalMethod): Функция, для которой необходимо найти минимум.\n
        inerval (tuple[Number, Number]): Интервал, в котором ищется минимум.\n
        L (Number): Константа Липшица.\n
        eps (Number): Точность поиска.\n

    Возвращает:\n
        OptimizationFnReturnValue: Словарь с координатами минимума.
                                Ключ 'x' — значение аргумента, при котором достигается минимум.
                                Ключ 'y' — значение функции в точке минимума.

    Исключения:\n
        ValueError: Если eps <= 0 (некорректное значение точности).

    Примеры:
    >>> def f(x):
    ...     return (x - 3) ** 2
    >>> result = uniform_brute_force(f, interval=(0, 6), L=2, eps=10e-3)
    >>> print(result)
    {'x': 3.0, 'y': 0.0}
    """
    if eps <= 0:
        raise ValueError("Параметр eps должен быть положительным.")

    a, b = interval
    h = 2 * eps / L

    points = [a]
    x = a + h / 2
    while True:
        if x > b:
            points.append(min(x, b))
            break
        points.append(x)
        x = points[-1] + h

    values = [fn(x) for x in points]

    min_index = values.index(min(values))

    return {"x": points[min_index], "y": values[min_index]}


if __name__ == "__main__":
    fn = lambda x: cos(x) / x**2
    a, b = 9, 11
    eps = 10**-3
    L = lipschitz_constant(fn, interval=(a, b))
    res = uniform_brute_force(fn, interval=(a, b), L=L, eps=eps)
    print(f"x: {res['x']}, y: {res['y']}")

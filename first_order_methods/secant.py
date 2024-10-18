from custom_types import Number, NumericalMethod, OptimizationFnReturnValue
from math import exp


def secant(
    fn: NumericalMethod, d_fn: NumericalMethod, a: Number, b: Number, eps: Number
) -> OptimizationFnReturnValue:
    """
    Находит минимум функции с помощью метода секущих.

    Параметры:\n
        fn (NumericalMethod): Функция, для которой необходимо найти минимум.\n
        d_fn (NumericalMethod): Производная функции, для которой необходимо найти минимум.\n
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
    >>> def d_f(x):
    ...     return 2 * (x - 3) ** 2
    >>> result = secant(f, d_f, 0, 4, 0.01)
    >>> print(result)
    {'x': 3.0, 'y': 0.0}
    """
    if eps <= 0:
        raise ValueError("Параметр eps должен быть положительным.")
    if d_fn(a) * d_fn(b) > 0:
        if d_fn(a) > 0:
            return {"x": a, "y": fn(a)}
        else:
            return {"x": b, "y": fn(b)}
    if d_fn(a) * d_fn(b) == 0:
        if d_fn(a) == 0:
            return {"x": a, "y": fn(a)}
        else:
            return {"x": b, "y": fn(b)}

    x_0 = a
    x_1 = (a * d_fn(b) - b * d_fn(a)) / d_fn(b) - d_fn(a)
    x_2 = x_1 - d_fn(x_1) * (x_1 - x_0) / (d_fn(x_1) - d_fn(x_0))
    y_2 = d_fn(x_2)
    while abs(y_2) > eps:
        x_0 = x_1
        x_1 = x_2
        x_2 = x_1 - d_fn(x_1) * (x_1 - x_0) / (d_fn(x_1) - d_fn(x_0))
        y_2 = d_fn(x_2)
    else:
        return {"x": x_2, "y": fn(x_2)}


if __name__ == "__main__":
    fn = lambda x: x**2 - x + exp(-x)
    d_first_fn = lambda x: 2 * x - 1 - exp(-x)
    a, b = -0.5, 1.5
    eps = 10**-3
    res = secant(fn, d_first_fn, a, b, eps)
    print(f"x: {res['x']}, y: {res['y']}")

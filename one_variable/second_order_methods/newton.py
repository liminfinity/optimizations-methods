from custom_types import Number, NumericalMethod, OptimizationFnReturnValue
import numpy as np

def newton(
    f: NumericalMethod, f_1st: NumericalMethod, f_2nd: NumericalMethod, x_0: Number, eps: Number
) -> OptimizationFnReturnValue:
    """
    Находит минимум функции с помощью метода Ньютона.

    Параметры:\n
        f (NumericalMethod): Функция, для которой необходимо найти минимум.\n
        f_1st (NumericalMethod): Первая производная функции, для которой необходимо найти минимум.\n
        f_2nd (NumericalMethod): Вторая производная функции, для которой необходимо найти минимум.\n
        x_0 (Number): Начальное приближение.\n
        eps (Number): Точность поиска (порог для завершения).\n

    Возвращает:\n
        OptimizationFnReturnValue: Словарь с координатами минимума.
                                Ключ 'x' — значение аргумента, при котором достигается минимум.
                                Ключ 'y' — значение функции в точке минимума.

    Исключения:\n
        ValueError: Если eps <= 0 (некорректное значение точности).

    Примеры:
    >>> def f(x):
    ...     return x**2 - 2 * x + 16 / (x - 1) - 13
    >>> def f_1st(x):
    ...     return 2 * x - 1 - 16 / (x - 1)**2
    >>> def f_2nd(x):
    ...     return 2 - 16 / (x - 1)**3
    >>> result = newton(f, f_1st, f_2nd, 2, 10**-3)
    >>> print(result)
    {'x': 1.9999999999999998, 'y': 1.9999999999999998}
    """
    if eps <= 0:
        raise ValueError("Параметр eps должен быть положительным.")

    x = x_0 - f_1st(x_0) / f_2nd(x_0)
    d_y = f_1st(x)
    while abs(d_y) > eps:
        x = x - d_y / f_2nd(x)
        d_y = f_1st(x)
    else:
        return {"x": x, "y": f(x)}
   

if __name__ == "__main__":
    f = lambda x: x**2 - x + np.exp(-np.maximum(x, 0))
    f_1st = lambda x: 2 * x - 1 - np.exp(-np.maximum(x, 0))
    f_2nd = lambda x: 2 - np.exp(-np.maximum(x, 0))
    x_0 = 10
    eps = 1e-3
    res = newton(f, f_1st, f_2nd, x_0, eps)
    print(f"x: {res['x']}, y: {res['y']}")

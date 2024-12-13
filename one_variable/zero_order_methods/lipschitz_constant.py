import numpy as np
from scipy.misc import derivative
from custom_types import Number, NumericalMethod


def lipschitz_constant(f: NumericalMethod, interval: tuple[Number, Number], num_points=1000) -> float:
    """
    Находит константу Липшица для функции f на интервале interval.

    Параметры:\n
        f (function): Функция, для которой необходимо вычислить константу Липшица.\n
        interval (tuple): Интервал, в котором ищется константа Липшица.\n
        num_points (int): Количество точек на интервале.\n

    Возвращает:\n
        L (float): Константа Липшица.

    Примеры:
    >>> def f(x):
    ...     return (x - 3) ** 2
    >>> result = lipschitz_constant(f, interval=(0, 6), num_points=1000)
    >>> print(result)
    2.0
    """

    a, b = interval

    x_vals = np.linspace(a, b, num_points)

    derivatives = [abs(derivative(f, x, dx=1e-6)) for x in x_vals]

    L = max(derivatives)

    return L

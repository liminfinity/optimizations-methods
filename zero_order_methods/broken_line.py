# from scipy.misc import derivative
# from math import cos
# import numpy as np

# def my_func(x):
#    return cos(x) / x**2

# def lipschitz_constant(f, interval, num_points=1000):
#     a, b = interval

#     x_vals = np.linspace(a, b, num_points)

#     derivatives = [abs(derivative(f, x, dx=1e-6)) for x in x_vals]

#     L = max(derivatives)

#     return L


# def uniform_search(f, interval, epsilon):
#     a, b = interval
#     n = int((b - a) / epsilon) + 1

#     x_vals = np.linspace(a, b, n)

#     f_vals = [f(x) for x in x_vals]

#     min_index = np.argmin(f_vals)
#     x_min = x_vals[min_index]
#     f_min = f_vals[min_index]

#     return x_min, f_min


# def broken_line_method(f, interval, L, epsilon, max_iter=1000):
#     a, b = interval
#     x0 = (f(a) - f(b) + L*(a + b)) / (2 * L)
#     y0 = (f(a) + f(b) + L*(a - b)) / 2
#     values = []
#     fx = 0

#     for _ in range(max_iter):
#         (x, p) = get_min_p(values) if values else (x0, y0)
#         fx = f(x)

#         delta = (fx - p) / (2 * L)

#         if delta < epsilon:
#             return (x, fx)
#         else:
#             p = (fx + p) / 2
#             x1 = x - delta
#             x2 = x + delta

#             values = [(xi, pi) for (xi, pi) in values if xi != x]
#             values.append((x1, p))
#             values.append((x2, p))

#     return None


# def get_min_p(values):
#     min_x, min_p = min(values, key=lambda item: item[1])
#     return min_x, min_p

# interval = (9, 11)
# epsilon = 3e-2
# L = lipschitz_constant(my_func, interval)


# res1 = broken_line_method(my_func, interval, L, epsilon)

# print('-------------------')
# print('Метод ломанных:')
# if res1:
#    print(res1)
# else:
#     print("Метод не сошелся за заданное число операций")

# print('-------------------')

# print('Метод перебора:')
# res2 = uniform_search(my_func, interval, epsilon)
# print(res2)
# print('-------------------')


from custom_types import Number, NumericalMethod, OptimizationFnReturnValue
from math import cos
from lipschitz_constant import lipschitz_constant
from uniform_brute_force import uniform_brute_force
import numpy as np


def broken_line(
    fn: NumericalMethod, interval: tuple[Number, Number], L: Number, eps: Number
) -> OptimizationFnReturnValue:
    """
    Находит минимум функции с помощью метода ломаных.

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
    >>> result = broken_line(f, interval=(0, 6), L=2, eps=10e-3)
    >>> print(result)
    {'x': 3.0, 'y': 0.0}
    """
    if eps <= 0:
        raise ValueError("Параметр eps должен быть положительным.")

    a, b = interval
    x_0 = (fn(a) - fn(b) + L * (a + b)) / (2 * L)
    p_0 = (fn(a) + fn(b) + L * (a - b)) / 2
    pairs = []

    # 1 step
    y_0 = fn(x_0)
    delta = (y_0 - p_0) / (2 * L)
    x_1 = x_0 - delta
    x_2 = x_0 + delta
    p = (y_0 + p_0) / 2
    pairs.append((x_1, p))
    x_0, p_0 = x_2, p

    # 2 step
    y_0 = fn(x_0)
    delta = (y_0 - p_0) / (2 * L)
    x_1 = x_0 - delta
    x_2 = x_0 + delta
    p = (y_0 + p_0) / 2
    pairs.append((x_1, p))
    pairs.append((x_2, p))
    x_0, p_0 = min(pairs, key=lambda pair: pair[1])
    pairs.remove((x_0, p_0))

    while True:
        y_0 = fn(x_0)
        delta = (y_0 - p_0) / (2 * L)
        if 2 * L * delta <= eps:
            return {"x": x_0, "y": y_0}
        x_1 = x_0 - delta
        x_2 = x_0 + delta
        p = (y_0 + p_0) / 2
        pairs.append((x_1, p))
        pairs.append((x_2, p))
        x_0, p_0 = min(pairs, key=lambda pair: pair[1])
        pairs.remove((x_0, p_0))


if __name__ == "__main__":
    fn = lambda x: np.cos(x) / x**2
    a, b = 9, 11
    eps = 10**-3
    L = lipschitz_constant(fn, interval=(a, b))
    res_1 = uniform_brute_force(fn, interval=(a, b), L=L, eps=eps)
    res_2 = broken_line(fn, interval=(a, b), L=L, eps=eps)
    print("Метод равномерного перебора:", end=" ")
    print(f"x: {res_1['x']}, y: {res_1['y']}")
    print("Метод ломанных:", end=" ")
    print(f"x: {res_2['x']}, y: {res_2['y']}")

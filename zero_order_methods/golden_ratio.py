from custom_types import Number, NumericalMethod, OptimizationFnReturnValue
from math import sqrt

def golden_ratio(fn: NumericalMethod, a: Number, b: Number, eps: Number) -> OptimizationFnReturnValue:
    """
    Находит минимум функции с помощью метода золотого сечения.

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
    ...     return (x - 2) ** 2
    >>> result = golden_ratio(f, 0, 4, 0.01)
    >>> print(result)
    {'x': 2.0, 'y': 0.0}
    """
    if eps <= 0:
        raise ValueError("Параметр eps должен быть положительным.")
    
    alpha_x = a + (3 - sqrt(5)) / 2 * (b - a)
    beta_x = a + (sqrt(5) - 1) / 2 * (b - a)
    alpha_y = fn(alpha_x)
    beta_y = fn(beta_x)
    l = b - a
    x = alpha_x
    while l > eps:
        if alpha_y <= beta_y:
            b = beta_x
            x = alpha_x
            beta_x = alpha_x
            beta_y = alpha_y
            alpha_x = a + b - alpha_x
            alpha_y = fn(alpha_x)
        else:
            a = alpha_x
            x = beta_x
            alpha_x = beta_x
            alpha_y = beta_y
            beta_x = a + b - beta_x
            beta_y = fn(beta_x)
        l = b - a
    else:
        x_min = x
        return {'x': x_min, 'y': fn(x_min)}


if __name__ == "__main__":
    input_fn = lambda x: x ** 2 - 2 * x + 16 / (x - 1) - 13
    a, b = 2, 5
    eps =  10 ** -3
    res = golden_ratio(input_fn, a, b, eps)
    print(f'x: {res['x']}, y: {res['y']}')
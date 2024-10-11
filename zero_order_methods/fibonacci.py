from custom_types import Number, NumericalMethod, OptimizationFnReturnValue
from math import sqrt

def fibonacci(fn: NumericalMethod, a: Number, b: Number, eps: Number) -> OptimizationFnReturnValue:
    """
    Находит минимум функции с помощью метода Фибоначчи.

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
    >>> result = fibonacci(f, 0, 4, 0.01)
    >>> print(result)
    {'x': 2.0, 'y': 0.0}
    """
    if eps <= 0:
        raise ValueError("Параметр eps должен быть положительным.")
    
    f_1 = f_2 = j = 1
    m = None

    while True:
        f_3 = f_2 + f_1
        if f_2 < (b - a) / eps <= f_3:
            m = j
            break
        else:
            f_1, f_2 = f_2, f_3
            j += 1
    
    alpha_x = a + f_1 / f_3 * (b - a)
    beta_x = a + b - alpha_x
    alpha_y = fn(alpha_x)
    beta_y = fn(beta_x)
    k = 1
    
    while k < m - 1:
        if alpha_y <= beta_y:
            b = beta_x
            beta_x = alpha_x
            beta_y = alpha_y
            alpha_x = a + b - alpha_x
            alpha_y = fn(alpha_x)
        else:
            a = alpha_x
            alpha_x = beta_x
            alpha_y = beta_y
            beta_x = a + b - beta_x
            beta_y = fn(beta_x)
        k += 1
    else:
        x_min = (a + b) / 2
        return {'x': x_min, 'y': fn(x_min)}


if __name__ == "__main__":
    input_fn = lambda x: x ** 2 - 2 * x + 16 / (x - 1) - 13
    a, b = 2, 5
    eps =  10 ** -3
    res = fibonacci(input_fn, a, b, eps)
    print(f'x: {res['x']}, y: {res['y']}')
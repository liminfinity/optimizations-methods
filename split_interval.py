from math import ceil, log2, log
from custom_types import Number, NumericalMethod
from typing import Dict

def split_interval(fn: NumericalMethod, a: Number, b: Number, eps: Number) -> Dict[str, Number]:
    """
    Находит минимум функции с помощью метода деления интервала.

    Параметры:\n
        fn (NumericalMethod): Функция, для которой необходимо найти минимум.\n
        a (Number): Левая граница интервала, в котором ищется минимум.\n
        b (Number): Правая граница интервала, в котором ищется минимум.\n
        eps (Number): Точность поиска (порог для завершения).\n

    Возвращает:\n
        Dict[str, Number]: Словарь с координатами минимума. 
                    Ключ 'x' — значение аргумента, при котором достигается минимум.
                    Ключ 'y' — значение функции в точке минимума.
                    Ключ 'n' — количество итераций, необходимых для достижения минимума.
                    Ключ 'N' — общее количество вызовов целевой функции.
                    Ключ 'a' — обновленная левая граница интервала.
                    Ключ 'b' — обновленная правая граница интервала.

    Исключения:\n
        ValueError: Если eps <= 0 (некорректное значение точности).

    Примеры:
    >>> def f(x):
    ...     return (x - 4) ** 2
    >>> result = split_interval(f, 0, 10, 0.01)
    >>> print(result)
    {'x': 4.0, 'y': 0.0, 'n': 10, 'N': 21, 'a': 3.75, 'b': 4.25}
    """

    if eps <= 0:
        raise ValueError("Параметр eps должен быть положительным.")
    
    k = 0
    N = 1
    avg_x = (a + b) / 2
    avg_y = fn(avg_x)
    while b - a > eps:
        alpha_x = a + (b - a) / 4
        beta_x = b - (b - a) / 4
        alpha_y = fn(alpha_x)
        beta_y = fn(beta_x)
        if alpha_y < avg_y:
            b = avg_x
            avg_x = alpha_x
            avg_y = alpha_y
        elif beta_y < avg_y:
            a = avg_x
            avg_x = beta_x
            avg_y = beta_y
        else:
            a = alpha_x
            b = beta_x
        N += 2
        k += 1
    else:
        x_min = (a + b) / 2
        return {'x': x_min, 'y': fn(x_min), 'n': k, 'N': N, 'a': a, 'b': b}


if __name__ == "__main__":
    input_fn = lambda x: x ** 2 - 2 * x + 16 / (x - 1) - 13
    a, b = 2, 5
    eps = 10 ** -3
    res = split_interval(input_fn, a, b, eps)
    print(f'x: {res['x']}\ty: {res['y']}')
    R = 1 / 2 ** ((res['N'] - 1) / 2)
    print(f'N: {res['N']}\tN(theory): {ceil(2 * log(R) / log(0.5))}')
    print(f'n: {res['n']}\tn(theory): {ceil(log2((b - a) / eps))}')
    print(f'R(N): {abs(res['b'] - res['a'])/abs(b - a)}\tR(N)(theory): {R}')

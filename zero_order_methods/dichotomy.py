from custom_types import Number, NumericalMethod, OptimizationFnReturnValue


def dichotomy(
    fn: NumericalMethod, a: Number, b: Number, eps: Number
) -> OptimizationFnReturnValue:
    """
    Находит минимум функции с помощью метода дихотомии.

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
    >>> result = dichotomy(f, 0, 4, 0.01)
    >>> print(result)
    {'x': 2.0, 'y': 0.0}
    """
    if eps <= 0:
        raise ValueError("Параметр eps должен быть положительным.")

    delta = eps / 4
    l = b - a
    while l > eps:
        alpha_x = (a + b) / 2 - delta
        beta_x = (a + b) / 2 + delta
        alpha_y = fn(alpha_x)
        beta_y = fn(beta_x)
        if alpha_y <= beta_y:
            b = beta_x
        else:
            a = alpha_x
        l = b - a
    else:
        x_min = (a + b) / 2
        return {"x": x_min, "y": fn(x_min)}


if __name__ == "__main__":
    input_fn = lambda x: x**2 - 2 * x + 16 / (x - 1) - 13
    a, b = 2, 5
    eps = 10**-3
    res = dichotomy(input_fn, a, b, eps)
    print(f"x: {res['x']}, y: {res['y']}")

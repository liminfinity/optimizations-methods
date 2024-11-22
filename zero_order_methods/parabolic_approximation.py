from custom_types import Number, NumericalMethod, OptimizationFnReturnValue
from random import uniform

def parabolic_approximation(
    fn: NumericalMethod, a: Number, b: Number, eps: Number, max_iterations = 100000
) -> OptimizationFnReturnValue:
    """
    Находит минимум функции с помощью метода параболлической апроксимации.

    Параметры:\n
        fn (NumericalMethod): Функция, для которой необходимо найти минимум.\n
        a (Number): Левая граница интервала, в котором ищется минимум.\n
        b (Number): Правая граница интервала, в котором ищется минимум.\n
        eps (Number): Точность поиска (порог для завершения).\n
        max_iterations (int): Максимальное количество итераций.

    Возвращает:\n
        OptimizationFnReturnValue: Словарь с координатами минимума.
                                Ключ 'x' — значение аргумента, при котором достигается минимум.
                                Ключ 'y' — значение функции в точке минимума.

    Исключения:\n
        ValueError: Если eps <= 0 (некорректное значение точности).

    Примеры:
    >>> def f(x):
    ...     return (x - 3) ** 2
    >>> result = parabolic_approximation(f, 0, 6, 0.01)
    >>> print(result)
    {'x': 3.0, 'y': 0.0}
    """
    if eps <= 0:
        raise ValueError("Параметр eps должен быть положительным.")
    x_1 = a
    x_2 = (a + b) / 2
    x_3 = b

    y_1 = fn(x_1)
    y_2 = fn(x_2)
    y_3 = fn(x_3)

    if not (x_1 < x_2 < x_3 and y_1 >= y_2 <= y_3):
        return print("Неверные входные данные, измените начальные точки")

    for _ in range(0, max_iterations):
        numerator = (y_1 * (x_2**2 - x_3**2) + 
                       y_2 * (x_3**2 - x_1**2) + 
                       y_3 * (x_1**2 - x_2**2))
        
        denominator = (2 * y_1 * (x_2 - x_3) + 
                   y_2 * (x_3 - x_1) + 
                   y_3 * (x_1 - x_2))

        if denominator == 0:
            x_tilda = uniform(x_1, x_3)
        else:
            x_tilda = numerator / denominator


        if x_tilda < x_1 or x_tilda > x_3:
            x_tilda = uniform(x_1, x_3)
        
            
        y_tilda = fn(x_tilda)

        if abs(x_1 - x_3) < eps:
            return {"x": x_tilda, "y": y_tilda}
        
        if x_2 <= x_tilda <= x_3:
            if y_tilda <= y_2:
                x_1, y_1 = x_2, y_2
                x_2, y_2 = x_tilda, y_tilda
            else:
                x_3, y_3 = x_tilda, y_tilda
        elif x_1 <= x_tilda <= x_2:
            if y_tilda <= y_2:
                x_3, y_3 = x_2, y_2
                x_2, y_2 = x_tilda, y_tilda
            else:
                x_1, y_1 = x_tilda, y_tilda
    else:
        return print('Метод не сошелся за заданное число операций')

if __name__ == "__main__":
    input_fn = lambda x: x**2 - 2 * x + 16 / (x - 1) - 13
    a, b = 2, 3.1
    eps = 1e-5
    res = parabolic_approximation(input_fn, a, b, eps)
    if (res):
        print(f"x: {res['x']}, y: {res['y']}")

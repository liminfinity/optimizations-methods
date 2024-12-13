import numpy as np

def objective_function(x):
    return (x[0] - 2 * x[1]) ** 2 + (x[1] - 9) ** 2

# Этап 1: Исследующий поиск с одинаковыми шагами для всех координат
def exploratory_search(x, h):
    n = len(x)
    best_x = np.copy(x)
    best_value = objective_function(best_x)

    for i in range(n):
        for step in [-h, h]: 
            x_new = np.copy(x)
            x_new[i] = x[i] + step
            if objective_function(x_new) < best_value:
                best_x = np.copy(x_new)
                best_value = objective_function(best_x)

    return best_x

# Этап 2: Поиск по образцу
def pattern_search(x1, x2, lambda_val=2):
    return x1 + lambda_val * (x2 - x1)

# Основная функция алгоритма Хука-Дживса
def hooke_jeeves(x0, h0, epsilon=0.001, lambda_val=2, h_decrease_factor=1.1):
    x1 = np.copy(x0)
    h = h0
    while True:
        x2 = exploratory_search(x1, h)
        if np.linalg.norm(x2 - x1) < epsilon:
            return x2

        x3 = pattern_search(x1, x2, lambda_val)
        x4 = exploratory_search(x3, h)

        if np.linalg.norm(x4 - x3) > epsilon:
            x1 = np.copy(x2)
            x2 = np.copy(x4)
        else:
            h = h / h_decrease_factor

x0 = np.array([-3, -12.3])
h0 = 3

minimum = hooke_jeeves(x0, h0)

print(f"Минимум найден в точке: x = {minimum[0]}, y = {minimum[1]}")
print(f"Значение функции в этой точке: {objective_function(minimum)}")

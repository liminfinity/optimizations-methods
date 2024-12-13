import numpy as np
from scipy.optimize import minimize_scalar

def f(x):
    x1, x2 = x
    return x1**4 + 2 * x2**4 + x1**2 * x2**2 + 2 * x1 + x2

def grad_f(x):
    x1, x2 = x
    df_dx1 = 4 * x1**3 + 2 * x1 * x2**2 + 2
    df_dx2 = 8 * x2**3 + 2 * x1**2 * x2 + 1
    return np.array([df_dx1, df_dx2])

# Метод сопряженных градиентов
def conjugate_gradient_method(f, grad_f, x0, epsilon=0.01, max_iter=10):
    x = x0
    grad = grad_f(x)
    p = -grad
    k = 0

    while np.linalg.norm(grad) > epsilon and k < max_iter:

        def f_alpha(alpha):
            return f(x + alpha * p)

        res = minimize_scalar(f_alpha)
        alpha = res.x 

        x = x + alpha * p

        grad_new = grad_f(x)

        if np.linalg.norm(grad_new) <= epsilon:
            break

        beta = np.dot(grad_new, grad_new) / np.dot(grad, grad)

        p = -grad_new + beta * p

        grad = grad_new
        k += 1

    return x, f(x), k

x0 = np.array([2.0, 3.0])
epsilon = 0.001

solution, f_min, iterations = conjugate_gradient_method(f, grad_f, x0, epsilon)

print("Решение:", solution)
print("Минимальное значение функции:", f_min)
print("Количество итераций:", iterations)

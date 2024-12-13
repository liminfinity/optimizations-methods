import numpy as np
from golden_ratio import golden_ratio

def f(x):
    return (x[0] - 2 * x[1]) ** 2 + (x[1] - 9) ** 2

def grad_f(x):
    grad = np.zeros_like(x)
    grad[0] = 2 * (x[0] - 2 * x[1])
    grad[1] = -4 * (x[0] - 2 * x[1]) + 2 * (x[1] - 9)
    return grad

H = np.array([
    [2, -4],
    [-4, 10]
])

def newton_method(f, grad_f, hessian, x0, epsilon1, epsilon2, M):
    x = x0
    k = 0

    hessian_inv = np.linalg.inv(hessian)

    while True:
        grad = grad_f(x)

        if np.linalg.norm(grad) < epsilon1:
            return x, f(x), k

        if k >= M:
            return x, f(x), k

        if np.all(np.linalg.eigvals(hessian_inv) > 0):
            dk = np.dot(-hessian_inv, grad)
            tk = 1
        else:
            dk = -grad
            tk = golden_ratio(lambda t: f(x - t * grad), 0, 1, 10**-3)

        x_new = x + tk * dk

        if np.linalg.norm(x_new - x) < epsilon2 and abs(f(x_new) - f(x)) < epsilon2:
            return x_new, f(x_new), k

        x = x_new
        k += 1

x0 = np.array([-1000.0, -1000.0])
epsilon1 = 0.15
epsilon2 = 0.15
M = 1000

x_star, f_min, iterations = newton_method(f, grad_f, H, x0, epsilon1, epsilon2, M)

print("Точка минимума:", x_star)
print("Значение функции в точке минимума:", f_min)
print("Количество итераций:", iterations)

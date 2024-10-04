def bit_search(fn, a, b, eps):
    h = (b - a) / 4
    x_0 = a
    y_0 = fn(x_0)
    while True:
        x_1 = x_0 + h
        y_1 = fn(x_1)
        if y_0 > y_1:
            x_0 = x_1
            y_0 = y_1
        if a < x_0 < b: continue
        elif x_0 >= b:
            x_0 = b
        elif x_0 <= a:
            x_0 = a
        if abs(h) <= eps:
            return {'x': x_0, 'y': fn(x_0)}
        else:
            x_0 = x_1
            y_0 = y_1
            h = -h / 4


if __name__ == "__main__":
    input_fn = lambda x: x ** 2 - 2 * x + 16 / (x - 1) - 13
    a, b = 2, 5
    eps = 10 ** -3
    res = bit_search(input_fn, a, b, eps)
    print(f'x: {res['x']}, y: {res['y']}')

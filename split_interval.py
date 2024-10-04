from math import ceil, log2, log

def split_interval(fn, a, b, eps):
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

from random import Random
import numpy as np

w = [-1, 0, 0]


def x(u, w):
    return sum([u[i] * w[i] for i in range(3)])


def y(x):
    if x > 0.0:
        return 1
    else:
        return 0


def d(u):
    if -u[1] + u[2] - 2 > 0:
        return 1
    else:
        return 0


def update_w(u, w, eta, err):
    for i in range(3):
        w[i] = w[i] + eta * err * u[i]


rand = Random()

print(w)
for _ in range(10000):
    u = [rand.randint(-3, 3), rand.randint(-3, 3), rand.randint(-3, 3)]
    x_ = x(u, w)
    y_ = y(x_)
    d_ = d(u)
    err = d_ - y_
    update_w(u, w, 0.1, err)
    print("u =", u, "w =", w)

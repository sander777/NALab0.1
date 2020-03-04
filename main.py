import pylab as plb
import matplotlib.pyplot as plt
import matplotlib.axes as axes
import numpy as np
from math import *

def f(x):
    return x**5 + x - 3

def f_prime(x):
    return 5 * x**4 - 1

def f_second(x):
    return 20 * x**3

fig1=plt.figure(1)
ax = fig1.add_subplot(1, 1, 1)
ax.axis('equal')
ax.set(xlim=(-10, 10), ylim=(-10, 10))
fr = 10

ax.plot(np.arange(-fr, fr, 0.01),list(map(f, np.arange(-fr, fr, 0.01))))
ax.plot(np.arange(-fr, fr, 0.01),list(map(f_prime, np.arange(-fr, fr, 0.01))))
ax.plot([-100, 100],[0, 0])

plt.ion()
plt.show()

def max_min_on_interval(a, b, f):
    min, max = f(a), f(b)
    for i in np.arange(a, b, (a-b) / 100):
        if min < f(i):
            min = f(i)
        if max > f(i):
            max = f(i)

    return max, min

def newton(f, f_prime, a, b, x_, f_second, eps=1e-7, imax=1e6, ):
    x0 = 0
    while True:
        x0 = float(input("Input x0: "))
        if x0 > b or x0 < a:
            print("Out of range")
            continue
        _, m1 = max_min_on_interval(x_ - eps, x_ + eps, lambda x: abs(f_prime(x)))
        M2, _ = max_min_on_interval(x_ - eps, x_ + eps, lambda x: abs(f_second(x)))

        q = (M2 * abs(x_ - x0)) / (2 * m1)
        print("q = {}".format(q))
        if q >= 1:
            print("q >= 1\nInput new [a, b] and x0")
            a, b = float(input("a: ")), float(input("b: ")) 
            continue

        n_ = floor(log2(1 + log(eps / (b - a)) / log(q))) + 1
        print("n >= {}".format(n_))
        print("Is it OK (1 - yes, 0 - no)")
        if int(input()) == 1:
            break

    x, x_prev, i = x0, x0 + 2 * eps, 1
    print("|{:>16}|{:>16}|{:>16}|{:>16}|".format('i', 'x', 'f(x)', 'f\'(x)'))
    print("---------------------------------------------------------------------")
    while abs(x - x_prev) >= eps and i < imax:
        print("|{:>16}|{:>16}|{:>16}|{:>16}|".format(i, round(x, 6), round(f(x), 6), round(f_prime(x), 6)))
        x, x_prev, i = x - f(x) / f_prime(x), x, i + 1

    print("|{:>16}|{:>16}|{:>16}|{:>16}|".format(i, round(x, 6), round(f(x), 6), round(f_prime(x), 6)))
    print("\nAnswer = " + str(x) + ";\t\tInterations - " + str(i))
    return x

def relaxetion(f, f_prime, a, b, eps=1e-7, imax=1e6):
    while True:
        x0 = float(input("Input x0: "))
        if x0 < a or x0 > b:
            print("Out of range")
            continue
        break
    M, m = max_min_on_interval(a, b, lambda x: abs(f_prime(x)))
    x, x_prev, tau, i = x0, x0 + 2 * eps, 2 / (M + m),1
    print("|{:>16}|{:>16}|{:>16}|{:>16}|".format('i', 'x', 'f(x)', 'f\'(x)'))
    print("---------------------------------------------------------------------")
    while abs(x - x_prev) >= eps and i < imax:
        print("|{:>16}|{:>16}|{:>16}|{:>16}|".format(i, round(x, 6), round(f(x), 6), round(f_prime(x), 6)))
        x, x_prev, i = x - f(x) * tau, x, i + 1

    print("|{:>16}|{:>16}|{:>16}|{:>16}|".format(i, round(x, 6), round(f(x), 6), round(f_prime(x), 6)))
    print("\nAnswer = " + str(x) + ";\t\tInterations - " + str(i))
    return x

print("Newton [a, b]")
a, b = float(input("a: ")), float(input("b: ")) 
newton(f, f_prime, a, b, 1.132997565885065267, f_second)
print("Relaxetion\n")
relaxetion(f, f_prime, a, b)
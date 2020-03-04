import pylab as plb
import matplotlib.pyplot as plt
import matplotlib.axes as axes
import numpy as np

def f(x):
    return x**5 + x - 3

def f_prime(x):
    return 5 * x**4 - 1

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

def newton(f, f_prime, x0, eps=1e-7, imax=1e6):
    x, x_prev, i = x0, x0 + 2 * eps, 1
    print("|{:>16}|{:>16}|{:>16}|{:>16}|".format('i', 'x', 'f(x)', 'f\'(x)'))
    print("---------------------------------------------------------------------")
    while abs(x - x_prev) >= eps and i < imax:
        print("|{:>16}|{:>16}|{:>16}|{:>16}|".format(i, round(x, 6), round(f(x), 6), round(f_prime(x), 6)))
        x, x_prev, i = x - f(x) / f_prime(x), x, i + 1

    print("|{:>16}|{:>16}|{:>16}|{:>16}|".format(i, round(x, 6), round(f(x), 6), round(f_prime(x), 6)))
    print("\nAnswer = " + str(x) + ";\t\tInterations - " + str(i))
    return x

def relaxetion(f, f_prime, x0, M, m, eps=1e-7, imax=1e6):
    x, x_prev, tau, i = x0, x0 + 2 * eps, 2 / (M + m),1
    print("|{:>16}|{:>16}|{:>16}|{:>16}|".format('i', 'x', 'f(x)', 'f\'(x)'))
    print("---------------------------------------------------------------------")
    while abs(x - x_prev) >= eps and i < imax:
        print("|{:>16}|{:>16}|{:>16}|{:>16}|".format(i, round(x, 6), round(f(x), 6), round(f_prime(x), 6)))
        x, x_prev, i = x - f(x) * tau, x, i + 1

    print("|{:>16}|{:>16}|{:>16}|{:>16}|".format(i, round(x, 6), round(f(x), 6), round(f_prime(x), 6)))
    print("\nAnswer = " + str(x) + ";\t\tInterations - " + str(i))
    return x

print("Newton")
x0 = float(input('Input x_0: '))
newton(f, f_prime, x0)
print("Relaxetion\n")
print("f(x*) = 0 and x* є [a, b]")
M, m = float(input("Max(|f'(x)|) x є (a, b): ")), float(input("Min(|f'(x)|) x є (a, b): "))
relaxetion(f, f_prime, x0, M, m)
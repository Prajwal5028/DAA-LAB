import time
import matplotlib.pyplot as plt


def fibonacci_recursive(n):
    if n == 1 or n == 0:
        return n

    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_iterative(n):
    a = 0
    b = 1
    c = 0
    n -= 2

    while n > 0:
        c = a + b
        a = b
        b = c
        n -= 1

    return c


def main():
    x = []
    y1 = []
    y2 = []
    for n in range(30):
        x.append(n)
        start = time.time()
        fibonacci_recursive(n)
        end = time.time()
        elapsed = end - start
        y1.append(elapsed)
        start = time.time()
        fibonacci_iterative(n)
        end = time.time()
        elapsed = end - start
        y2.append(elapsed)
    plt.plot(x, y1, 'r', label='Fibonacci Recursive')
    plt.plot(x, y2, 'b', label='Fibonacci Iterative')
    plt.xlabel('Input Size')
    plt.ylabel('Time(ms)')
    plt.legend(loc='upper left')
    plt.show()


main()
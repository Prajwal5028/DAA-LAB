import time
from random import randint
import matplotlib.pyplot as plt


def divide(a, low, high):
    if low < high:
        j = part(a, low, high)
        divide(a, low, j - 1)
        divide(a, j + 1, high)


def part(a, low, high):
    pivot = low
    i = low+1
    j = high
    while (i <= j):
        while (i <= high and a[i] <= a[pivot]):
            i += 1
        while (j >= 0 and a[j] > a[pivot]):
            j -= 1
        if (i <= j):
            a[i], a[j] = a[j], a[i]
    a[pivot], a[j] = a[j], a[pivot]
    return j


def main():
    x = []
    y = []
    for n in range(10, 101, 10):
        x.append(n)
        a = []
        for i in range(n):
            a.append(randint(1, n))

        start = time.time()
        divide(a, 0, len(a) - 1)
        end = time.time()
        elapsed = end - start
        y.append(elapsed)

    plt.plot(x, y, label="Quick Sort")
    plt.title("quick sort algorithm")
    plt.xlabel("Input Size")
    plt.ylabel("Time(ms)")
    plt.legend(loc="upper right")
    plt.show()


main()

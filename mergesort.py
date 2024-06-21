import time
from random import randint
import matplotlib.pyplot as plt


def divide(a, low, high):
    if low < high:
        mid = (low + high)//2
        divide(a, low, mid)
        divide(a, mid + 1, high)
        merge(a, low, mid, high)


def merge(a, low, mid, high):
    temp = []
    # Initialize temp array with all zeros and length equal to length of a.
    for i in range(len(a)):
        temp.append(0)

    i = low
    j = mid + 1
    k = low
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            temp[k] = a[i]
            k+=1
            i+=1
        else:
            temp[k] = a[j]
            k+=1
            j+=1

    while i <= mid:
        temp[k] = a[i]
        k+=1
        i+=1

    while j <= high:
        temp[k] = a[j]
        k+=1
        j+=1

    for k in range(low, high + 1):
        a[k] = temp[k]


def main():
    x = []
    y = []
    for n in range(10, 1001, 10):
        x.append(n)
        a = []
        for i in range(n):
            a.append(randint(1, 100))

        start = time.time()
        divide(a, 0, len(a) - 1)
        end = time.time()
        elapsed = end - start
        y.append(elapsed)

    plt.plot(x, y, label='Merge Sort')
    plt.xlabel("Input Size")
    plt.ylabel("Time(ms)")
    plt.legend(loc='upper left')
    plt.show()
main()
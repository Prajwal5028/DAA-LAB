
import time
import matplotlib.pyplot as plt
from random import random
def selsort(a,n):
  for i in range(n):
    min=i
    for j in range(i+1,n):
      if a[j]<a[min]:
        min=j
    a[i],a[min]=a[min],a[i]

def bubble_sort(arr,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

x=[]
y1=[]
y2=[]
for n in range(200):
  x.append(n)
  a=[random()%n + 1 for i in range(n)]
  start=time.time()
  selsort(a,n)
  end=time.time()
  elapsed=end - start
  y1.append(elapsed)
  start=time.time()
  bubble_sort(a,n)
  end=time.time()
  elapsed=end - start
  y2.append(elapsed)
plt.plot(x,y1,label="selection sort")
plt.plot(x,y2,label="bubble sort")
plt.xlabel('Input Size')
plt.ylabel('Time Taken (s)')
plt.title('Selection Sort vs Bubble sort')
plt.legend()
plt.grid(True)
plt.show()


import time
import matplotlib.pyplot as plt
from random import randint

def is_unique(a,n):
  for i in range(n-1):
    for j in range(i+1,n):
      if a[i]==a[j]:
        return False
  return True

def main():
  x=[]
  y=[]
  for n in range(10,101,10):
    a=[]
    x.append(n)
    for i in range(n):
      a.append(randint(1,n))

    start=time.time()
    is_unique(a,n)
    end=time.time()
    elapsed=end-start
    y.append(elapsed)
  plt.title("checking uniqueness of elements")
  plt.plot(x,y)
  plt.xlabel('input size')
  plt.ylabel('time(ms)')
  plt.grid()
  plt.show()
main()
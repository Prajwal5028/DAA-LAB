import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(3000)
def fact_rec(n):
  if n==1 or n==0:
    return 1
  return fact_rec(n-1)*n

def fact_itr(n):
  f=1
  while n!=0:
    f*=n
    n-=1
  return f

def main():
  x=[]
  y1=[]
  y2=[]
  for n in range(100,1001,100):
    x.append(n)
    start=time.time()
    fact_rec(n)
    end=time.time()
    time_taken=end-start
    y1.append(time_taken)
    start=time.time()
    fact_itr(n)
    end=time.time()
    time_taken=end-start
    y2.append(time_taken)
  fig,ax=plt.subplots()
  ax.plot(x,y1,'r',label='recursive factorial')
  ax.plot(x,y2,'b',label='iterative factorial')
  ax.set_xlabel('n')
  ax.set_ylabel('Time (seconds)')
  ax.set_title('Runtime Comparison of Recursive vs Iterative Factorial')
  ax.legend()
  ax.grid()
  plt.show()
main()

import time
import matplotlib.pyplot as plt
def count_dig_rec(n):
  if n==1:
    return 1
  return count_dig_rec(n//2)+1


def count_dig_itr(n):
  ans=1
  while n!=1:
    ans+=1
    n=n//2
  return ans


def main():
  x=[]
  y1=[]
  y2=[]
  for n in range(10,101,10):
    x.append(n)
    start=time.time()
    count_dig_rec(n)
    end=time.time()
    time_taken=end-start
    y1.append(time_taken)
    start=time.time()
    count_dig_itr(n)
    end=time.time()
    time_taken=end-start
    y2.append(time_taken)
  fig,ax=plt.subplots()
  ax.plot(x,y1,'r',label='recursive digit count')
  ax.plot(x,y2,'b',label='iterative digit count')
  ax.set_xlabel('n')
  ax.set_ylabel('Time (seconds)')
  ax.set_title('Runtime Comparison of Recursive vs Iterative digit count')
  ax.legend()
  ax.grid()
  plt.show()
main()
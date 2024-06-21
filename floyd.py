def floyd(dist,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
def main():
    dist=[[0,999,3,999],
          [2,0,999,999],
          [999,7,0,1],
          [6,999,999,0]]
    n=len(dist[0])
    print(".......weighted matrix........")
    print(dist)
    floyd(dist,n)
    print(".......all pair shortest path.......")
    print(dist)
main()
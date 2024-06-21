def warshall(a,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                a[i][j]=a[i][j] or (a[i][k] and a[k][j])
def main():
    a=[[0,1,0,0],
       [0,0,1,0],
       [0,0,0,1],
       [1,0,0,0]]
    n=len(a[0])
    print(".......adjacency matrix........")
    print(a)
    warshall(a,n)
    print(".......transitive closure.......")
    print(a)
main()
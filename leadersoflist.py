def leadersoflist(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]<=arr[j]:
                break
        if j==n-1:
            print(arr[i])
n=int(input())
arr=list(map(int,input().split()))
print(leadersoflist(arr,n))

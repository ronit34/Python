for t in range(int(input())):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))

 

    def sort(arr,n):
        for i in range(n-1):
            for j in range(0,n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr

    res = sort(arr,n)
    max_sum = 0
    min_sum = 0
    for i in range(n-1,m-1,-1):
        max_sum += res[i]

    for j in range(0,n-m):
        min_sum += res[j]
    diff = max_sum - min_sum
    print(diff)
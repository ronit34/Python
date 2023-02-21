def average(array):
    a = sum(set(array))
    b = len(set(array)) 
    ans = a/b
    return ans

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
def insertion_sort(n, arr):
    size = n
    for i in range(size):
        j = i - 1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
    

n = int(input())
arr = list(map(int, input().split()))
arr = insertion_sort(n, arr)
for i in range(n):
    print(arr[i], end=' ')
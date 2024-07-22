def bubble_sort(arr):
    for i in range(n):
        for j in range(n - 1 - i):
            if(arr[j] > arr[j+1]):
             arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

n = int(input())
arr = list(map(int, input().split()))
sorted_result = bubble_sort(arr)
for i in range(n):
    print(sorted_result[i], end=' ')
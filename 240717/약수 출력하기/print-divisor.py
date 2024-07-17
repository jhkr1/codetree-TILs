n = int(input())
result_list = []
for i in range(1, n+1):
    if(n % i == 0):
        result_list.append(i)

for i in result_list:
    print(i, end=' ')
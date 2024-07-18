dynamic_arr = []
n = int(input())
result = []

for i in range(n):
    temp = input().split()
    command = temp[0]
    if (command == 'push_back'):
        value = int(temp[1])
        dynamic_arr.append(value)
    elif(command == 'get'):
        value = int(temp[1])
        if (0 <= value <= len(dynamic_arr)):
            result.append(dynamic_arr[value-1])
    elif(command == 'size'):
        result.append(len(dynamic_arr))
    elif(command == 'pop_back'):
        dynamic_arr.pop()
for i in range(len(result)):
    print(result[i])
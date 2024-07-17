result = [0] * 10
a = int(input())
b = int(input())
c = int(input())

str_abc = str(a * b * c)

for i in range(len(str_abc)):
    n = int(str_abc[i])
    result[n] += 1

for i in range(10):
    print(result[i])
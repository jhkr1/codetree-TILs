import math

def print_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # i와 n // i가 다를 때만 추가
                divisors.append(n // i)
    divisors.sort()  # 정렬
    for divisor in divisors:
        print(divisor, end=' ')

# 정수 n 입력 받기
n = int(input())
print_divisors(n)
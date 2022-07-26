N = 12

def conv(n,i,v,x):
    result = ""
    if n==9:
        result += i + x
    elif n == 4:
        result += i + v
    else:
        for _ in range(n//5):
            result += v
        n = n % 5
        for _ in range(n):
            result += i
    return result

def roman(n):
    m = n//1000
    n %= 1000
    c = n//100
    n %= 100
    x = n//10
    n %= 10
    result = "M"*m
    result += conv(c, 'C', 'D', 'M')
    result += conv(x, 'X', 'L', 'C')
    result += conv(n, 'I', 'V', 'X')
    return result

from collections import defaultdict
cnt =defaultdict(int)

for i in range(4000):
    l = len(roman(i))
    cnt[l] += 1

print(cnt[N])
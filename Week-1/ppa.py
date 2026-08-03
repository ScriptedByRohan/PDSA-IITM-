#find the twin prime numbers between n and m (n < m) 
from grpa2 import isPrime
def TwinPrime(n,m):
    result = []
    for i in range(n,m-1):
        if isPrime(i) and isPrime(i+2) and (i+2) <= m:
            result.append((i,i+2))
    return result

print(TwinPrime(12,45))
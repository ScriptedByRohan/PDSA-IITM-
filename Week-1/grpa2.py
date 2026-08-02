#Goldbach's conjective example 26 = 13 + 13 , 23 +3 etc . Every even number greater than 2 is the sum of two prime number
def isPrime(num):
    if num < 2:
        return Falseṇṇṇ
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False 
    return True

def Goldbach(n):
    result = [] #because there could me many numbers
    for a in range(2,(n//2) + 1): #The pair n//2 so sumber dont repeat like 3,23 and 23,3 
        b = n-a 
        if isPrime(a) and isPrime(b):
            result.append((a,b))
    return result


print(Goldbach(26))




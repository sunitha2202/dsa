def sumOfDigits(n):
    if n==0:
        return 0
    ld=n%10
    return ld + sumOfDigits(n//10)
print(sumOfDigits(563))
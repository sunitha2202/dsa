def countDigits(n):
    if n==0:
        return 0
    else:
        return 1 +  countDigits(n//10)
print(countDigits(563257))
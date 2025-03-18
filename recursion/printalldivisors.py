def printAllDivisors(n,i=1):
    if i>n:
        return
    if n%i==0:
        print(i)
    printAllDivisors(n,i+1)
printAllDivisors(6)
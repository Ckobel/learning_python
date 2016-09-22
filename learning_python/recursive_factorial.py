def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

n = int(input("enter a number: "))
if n >= 2 and n <=12:
    print factorial(n)
else:
    print "n not within constraints 2 <= n <= 12"

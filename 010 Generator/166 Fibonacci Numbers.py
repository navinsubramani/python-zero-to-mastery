# Create fibonacci using the def

def fib(number):
    num1 = 0
    num2 = 1
    for i in range(number+1):
        yield num1
        n1 = num1
        n2 = num2
        num1 = n2
        num2 = n1+n2


print(list(fib(20)))

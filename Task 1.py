print("Enter a number :")
num = int(input())
def factorial(n):
    mult=1
    for i in range(1, n + 1):
        mult = mult * i
    return mult    
result = factorial(num)
print("The factorial of", num, "is", result)    
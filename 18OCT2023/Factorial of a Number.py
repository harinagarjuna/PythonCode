num = int(input("Please enter a number"))
factorial = 1
for i in range(1,num+1):
    factorial = factorial*i
print("Factorial for",num,"is",factorial)
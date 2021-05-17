import time
print("Text based caculator")
print("Enter two numbers when asked")
time.sleep(3)
n1 = int(input("Enter your first number : "))
n2 = int(input("Enter your second number : "))
opr = str(input("Enter the operation that you want to do in text (add, subtract, multiply and divide) : "))
if opr == "add":
    n3 = n1 + n2
    print(n3)
elif opr == "subtract":
    n3 = n1 - n2
    print(n3)
elif opr == "multiply":
    n3 = n1 * n2
    print(n3)
elif opr == "divide":
    n3 = n1 / n2
    print(n3)
else:
    print("Enter a valid operation")

welcome = "Hello and welcome to C to F and F to C convertor"
C = 0
F = 0
print(welcome)
mode = str(input("What do you wanna do (FTC) or (CTF)? "))
print(mode)

if mode == "FTC":
    F = float(input("Enter temperature in F:"))
    C = (F - 32) / 1.8
    print(C,"C")
    
if mode == "CTF":
    C = float(input("Enter temperature in C:"))
    F = (C * 1.8) + 32
    print(F,"F")
    
else:
    print("Enter a valid option.")
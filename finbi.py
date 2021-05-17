print("Fininacci Series")
i = 0
n = 0
f1 = -1
f2 = 1
f3 = 0
n = int(input("How many numbers? : "))
for i in range(n):
    f3 = f1 + f2
    print(f3)
    f1 = f2
    f2 = f3

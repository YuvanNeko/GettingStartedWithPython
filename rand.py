import random, time
r = random.randint(1, 10)
print("Welcome to the game of random")
time.sleep(3)
print("Computer is guessing the number now")
time.sleep(3)
print("Enter your guess : ")
n = int(input())
if r == n:
    print("You guessed the number correctly")
    print(r)
else:
    print("Try again")
    print(r)
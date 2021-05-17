import time
print("Welcome to Voter Verfification Program")
time.sleep(5)
print("Enter your age :")
age = int(input());
if age >= 100:
    print("Enter a valid age")
elif age >= 18:
    print("You can vote")
else:
        print("You cannot vote")
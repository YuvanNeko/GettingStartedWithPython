n = str(input("Enter a string to check if it is a palindrome or not : "))
na = n [:: -1]
if na == n:
    print("The given string : " + n + " is a palindrome")
else:
    print("The given string : " + n + " is not a palindrome")
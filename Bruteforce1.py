import random
number = int(input("Input a number that is a password: "))
guess = 0
while (guess != number):
    print(guess)
    guess +=1
print("Your password is " + str(number))

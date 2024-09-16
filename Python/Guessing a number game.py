import random
#to ceate a range of random numbers between 1-20
n = random.randrange(1,20)
guess_value = int(input("Enter any Number : "))
while n != guess_value:
    if guess_value < n:
        print("Guess Value is too small then number")
        guess_value = int(input("Enter any other Number : "))
    elif guess_value > n:
        print("Guess Value is too far then number")
        guess_value = int(input("Enter any other Number : "))
    else:
        break

print("Hurray!! You get the correct value ")

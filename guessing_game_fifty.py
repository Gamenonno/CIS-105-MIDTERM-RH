import random
n = random.randrange(1,50)
guess = int(input("Enter any number: "))
while n!= guess:
    if guess < n:
        print("too low")
        guess = int(input("try again: "))
    elif guess > n:
        print("too high")
        guess = int(input("try again: "))
    else:
      break
print("correct")
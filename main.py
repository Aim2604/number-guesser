import random

number = random.randint(1, 50)

for i in range(5):
  guess = int(input("Think of a number between 1 and 50: "))
  if guess == number:
    print("Your answer is correct, good job!")
  elif guess < number:
    print("Your answer is too low, try again!")
  elif guess > number:
    print("Your answer is too high, try again!")

else:
  print("The answer was " + str(number) + ", try again next time!")



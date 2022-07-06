import sys
import random

# program to guess the number
# number start and end is recieved via terminal using argv

first = int(sys.argv[1])
last = int(sys.argv[2])

number = random.randint(first, last)

while True:
    try:
        guess = int(input("Guess the number: "))

    except ValueError:
        print('Enter valid number...')

    else:
        if guess == number:
            print("CORRECT")
            break

        else:
            print("TRY AGAIN")

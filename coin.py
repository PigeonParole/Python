import time
import random

choice = input("Welcome to the coin flipper! Do you want to flip a coin? (Y/N): ")
if choice.upper() == "N":
    print("Ok")
elif choice.upper() == "Y":
    print("Flipping...")
    time.sleep(1)
    number = random.randint(1, 2)

    if number == 2:
        print("Heads")
    else:
        print("Tails")

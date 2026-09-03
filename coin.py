import time
import random
#asks the user if they wanna flip the coin
choice = input("Welcome to the coin flipper! Do you want to flip a coin? (Y/N): ")
if choice.upper() == "N":
    print("Ok")
#flips the coin if user says yes
elif choice.upper() == "Y":
    print("Flipping...")
    time.sleep(1)
    number = random.randint(1, 2)
#Gives final result
    if number == 2:
        print("Heads")
    else:
        print("Tails")

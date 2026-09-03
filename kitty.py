while True:
    num = int(input("How many times do you want to meow?: "))

    if num < 0:
        print("You cant pick a negative numberm try picking a normal positive one! <3")
        continue
    break


for _ in range(num):
    print("meow")

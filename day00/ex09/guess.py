import random
import sys

print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.")
magic_num = random.randint(0, 99)
count = 0
while True:
    try:
        str = input("You have to enter a number between 1 and 99 to find out the secret number.:\n")
        count += 1
        if str == "exit":
            print("Good luck!")
            sys.exit(0)
        guess_num = int(str)
        if guess_num > magic_num:
            print("Too high!")
        elif guess_num < magic_num:
            print("Too low!")
        elif guess_num == magic_num:
            if guess_num == 42 and count == 1:
                print("The answer to the ultimate question of life, the universe and everything is 42.\nCongratulations! You got it on your first try")
            else:
                print(f"Congratulations, you've got\nYou won in {count} attempts!")
            count = 0
            magic_num = random.randint(0, 99)
    except Exception as e:
        print(e)

import random
import os
def play(name):
    chances = 5
    correct_number = random.randrange(1, 51)
    print("Guess the number between 1 to 50 :")
    while chances:
        ans = int(input("Your Guess(Chances left {} ) : ".format(chances)))
        if ans == correct_number:
            print("{} ! you guess the correct number . The number is {}".format(name, correct_number))
            return True
        elif ans > correct_number:
            print("HINTS : Correct ans is smaller than your number ! Try Again !")
        else:
            print("HINTS : Correct ans is greater than your number ! Try Again !")
        chances -= 1
    os.system('cls')
    print("The correct number is {}".format(correct_number))
    return False
name = input("Player Name : ")
while True:
    result = play(name)
    if result:
        print("{} ! You win the game .".format(name))
    else :
        print("{} ! You lose the game .".format(name))
    re_start = input("Want to restart the game? (Y/N) Ans : ")
    if re_start.upper() == 'N':
        break
    os.system('cls')
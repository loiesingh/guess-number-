import random
def play_game():
    number = random.randint(1,100)
    attempts = 7
    score = 0

    print("\n welcome to number guessing game ! ")
    print(" I have selected a number between 1 and 100")
    print("you have attempts ", {attempts})
    while attempts > 0:
        try :
            guess = int(input("Enter your guess:"))
        except valueError:
            print("no wrong , plese enter a valid number !:")
            continue
        if guess == number:
            score = attempts * 10
            print("correct!, you won with score:",{score})
            break
        elif guess >number:
            print("\too high")
        else:
             print("too low")
             attempts == 1
             print("attempts left :",{attempts})

    else:
        print(" game over ! the number was :" , {number})
def main():
    while True :
        play_game()
        choice = input ("\n play again ? (yes/no):").lower()
        if choice != "yes":
            print("thanks for playing")
            break

main()

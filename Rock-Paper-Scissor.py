# Rock-Paper-Scissor
import random


def rps():
    print("Welcome to the game:")

    print("Rock\nPaper\nScissor\nQuit")

    while True:
        x = input("Enter your choice: ").strip().lower()
        if (x == '4' or x == 'quit'):
            print("Thanks For Playing!")
            break
        if x not in ('1', '2', '3', 'rock', 'paper', 'scissor'):
            print("Enter Valid Choice")
            continue

        choi = ['rock', 'paper', 'scissor']
        sec_coice = random.choice(choi)

        print(f"You Choose: {x}")
        print(f"Computer Choose: {sec_coice}")

        if x == sec_coice:
            print("It's a Tie!")
            break
        elif x == 'rock' and sec_coice == 'paper' or x == 'paper' and sec_coice == 'scissor' or x == 'scissor' and sec_coice == 'rock':
            print("You Lose!")
            break
        else:
            print("Congrats!, You Won.")
            break


if __name__ == "__main__":
    rps()

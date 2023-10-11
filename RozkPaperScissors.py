import random

class Choice:
    def __init__(self, choice):
        self.choice = choice
        rps = None
        if choice == 1:
            rps = "Rock"
        elif choice == 2:
            rps = "Paper"
        elif choice == 3:
            rps = "Scissors"
        else:
            rps = "Please choose a viable option"
        self.rps = rps


def winner(player, cpu):
    if (player == 1 and cpu == 2) or (player == 3 and cpu == 1) or (player == 2 and cpu == 3):
        print("CPU wins!")
    elif player == cpu:
        print("It's a tie!")
    else:
        print("Player wins!")

def main():
    try:
        while True:
            cpu = random.randint(1,3)
            player = int(input("Please choose an option:\n1. Rock\n2. Paper\n3. Scissors\n4. Exit the program\n: "))
            if player > 0 and player < 4:
                cpu_choice = Choice(cpu)
                player_choice = Choice(player)

                print("Player's : {}   VS   CPU's: {}".format(player_choice.rps, cpu_choice.rps))
                winner(player, cpu)
            elif player == 4:
                break
            else:
                print("Please choose a viable option\n")
                pass
    except ValueError as e:
        print(e, "\nPlease only use integers")
    except Exception as e:
        print(e, "\nSomething went wrong")

while __name__ == "__main__":
    main()
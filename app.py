import random

MOVES = ("rock", "paper", "scissors")


def get_user_move():
    """Prompt the user for a move until a valid choice is made.

    The comparison is case-insensitive so that inputs like "Rock" or "ROCK"
    are accepted. Without normalizing the case, these inputs would be rejected
    as invalid.
    """
    move = input("Choose rock, paper, or scissors: ").strip().lower()
    while move not in MOVES:
        print("Invalid move. Try again.")
        move = input("Choose rock, paper, or scissors: ").strip().lower()
    return move


def play_round():
    user_move = get_user_move()
    computer_move = random.choice(MOVES)
    print(f"Computer chose {computer_move}.")

    if user_move == computer_move:
        print("It's a tie!")
    elif (
        (user_move == "rock" and computer_move == "scissors")
        or (user_move == "paper" and computer_move == "rock")
        or (user_move == "scissors" and computer_move == "paper")
    ):
        print("You win!")
    else:
        print("You lose!")


if __name__ == "__main__":
    play_round()

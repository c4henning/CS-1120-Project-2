# import library
from random import randint


def guess_the_number():
    """
    This is a game that has the player try to guess a number.
    The number is randomly generated each play through.


    """

    def validate_guess(guess: str) -> int | None:
        """
        Verifies that the player's guess is an integer and converts
        type from str to int if valid. Else, guess is set to None.
        """

        if guess.isnumeric():
            return int(guess)
        else:
            print('You did not type a valid number, try again.')
            return None

    def check_answer(guess: int, secret: int) -> bool:
        """
        Check if the guess is larger than, is smaller than, or matches
        the secret number.
        """

        if guess > secret:
            print(guess, "is larger than the number.")
            return False

        elif guess < secret:
            print(guess, "is smaller than the number.")
            return False

        else:
            print("You guessed the secret number!")
            return True

    # secret number parameters
    min_secret = 1
    max_secret = 100
    # generate a secret number
    secret = randint(min_secret, max_secret)

    # initialize a guess count
    n_guesses = 0

    # run the game loop
    game_over = False
    while not game_over:
        # take a guess from the player
        # Write your code below
        guess = input(f"Guess a number between {min_secret} and {max_secret}: ")
        n_guesses += 1

        # check if the guess is valid
        guess = validate_guess(guess)

        if guess is not None:
            # check the guess against the secret
            # and update game_over
            game_over = check_answer(guess, secret)

    # print number of guesses made
    print(f"It took {n_guesses} tries to guess the number ({secret}).")


if __name__ == "__main__":
    guess_the_number()

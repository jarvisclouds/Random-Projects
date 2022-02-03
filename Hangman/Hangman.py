import random
from words import word_list
name = input("Enter your name: ")
print("Hello", name + "! Let's play Hangman!!")

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    full_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    limit = 6
    print(display_hangman(limit))
    print(full_word)
    print("\n")

    while not guessed and limit > 0:
        guess = input("Guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already tried" , guess +"!")
            elif guess not in word:
                print(guess , "isn't in the word :(")
                limit -= 1
                guessed_letters.append(guess)
            else:
                print("Good Guess" , guess, "is in the word")
                guessed_letters.append(guess)
                word_list = list(full_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_list[index] = guess
                full_word = "".join(word_list)
                if "_" not in full_word:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already tried" , guess +"!")
            elif guess not in word:
                print(guess, "isn't the word :(")
                limit -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                full_word = word
        else:
            print("Not a valid guess.")
        print(display_hangman(limit))
        print(full_word)
        print("\n")
    if guessed:
        print("Congratulation!!")
    else:
        print("The word was", word + ". Sorry, better luck next time :/")

def main_part():
    word = get_word()
    play(word)
    while input("Play again? (y/n) ").lower() == "y":
        word = get_word()
        play(word)


def display_hangman(limit):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[limit]

main_part()
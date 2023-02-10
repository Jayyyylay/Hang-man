import random
from words import word_list
from arts import logo,stages

word = random.choice(word_list)


def main(word):
    word_length = len(word)
    print(logo)
    print("\nHELLO PLAYER!, GUESS THE RIGHT WORD AND FREE THE MAN, GOODLUCK!")
    display = []
    guessed_letters = []
    letters_in_list = list(word)
    lives = 6

    for _ in range(word_length):
        display += "_"
    a = True
    while a:
        b = True
        while b:
            guess = input("Guess a Letter: ").lower()
            guess_length = len(guess)
            if guess_length >= 2:
                print("PLEASE ENTER ONLY 1 LETTER!")
            else:
                b = False


        if guess in display:
            print("You already guessed this letter!")

        for position in range(word_length):
            letter = word[position]
            if letter == guess:
               display[position] = letter

        print(display)

        if guess not in letters_in_list:
            if guess in guessed_letters:
                print("You already guessed this letter!")
            else:
                print("You guessed the wrong letter! Try again")
                lives -= 1

        if guess in letters_in_list:
            if display == letters_in_list:
                print("CONGRATULATIONS, YOU WON THE GAME!")
                a = False
            else:
                print("You guessed the right letter, Awesome!")
        elif lives == 0:

            print(f"\nTHE MAN DIED!, YOU LOSE!, the word is {word}")
            a = False
        guessed_letters.append(guess)
        print(stages[lives])
    play_again()

def welcome(word):

    c = True
    while c:
        print("\nWELCOME TO THE GAME HANGMAN")
        hit = input("Please hit ENTER to start or press X to exit the game: ").lower()
        if hit != "" and hit != "x":
            print("Please only hit enter nothing else to Start the game!")
        elif hit == "x":
            c = False
        else:
            main(word)


def play_again():
    again = True
    while again:
        play_again = input("\nDO YOU WANT TO PLAY HANGMAN AGAIN? YES OR NO: ").lower()
        if play_again != "yes" and play_again != "no":
            print("PLEASE INPUT YES or NO ONLY!")
        elif play_again == "yes":
            word = random.choice(word_list)
            main(word)
        elif play_again == "no":
            print("THANK YOU FOR PLAYING HANGMAN!")
            again = False

welcome(word)




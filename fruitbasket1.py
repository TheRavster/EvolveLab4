import sys
basket = ['apple', 'pear', 'cherry', 'banana', 'apricot']
def guess_check(guess):
    if guess in basket:
        print("You guessed RIGHT!")
    else:
        print("Sorry! I don't have that fruit.")

def main():
    guess = ""
    response = ""
    print("Welcome to the ruit basket guessing game.\n")
    while True:
        try:
            guess = raw_input("Guess the name of a fruit in my basket\n")
            print("You guessed: %s" % guess)
            guess_check(guess)
            response = raw_input("Want to play again? y/n \n")
            if response == "y":
                continue
            else:
                sys.exit()
        except ValueError:
            print("Sorry! Invalid Input")
            sys.exit()
main()

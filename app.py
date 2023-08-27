import random
from words import words
from hangman_art import hangman_logo, hangman

class HangmanGame:
    def __init__(self, max_attempts):
        self.secret_word = ''
        self.max_attempts = max_attempts
        self.guessed_letters = set()
        self.current_attempts = 0

    def start_new_game(self):
        self.guessed_letters = set()
        self.current_attempts = 0
        category = random.choice(list(words.keys()))
        self.secret_word = random.choice(words[category])

        print(f"Your word is from category: {category}")
        print(hangman[0])
        print(f"secret word {self.secret_word}")



    def make_guess(self, guess):
        if len(guess) == 1 and guess.isalpha():
            if guess in self.guessed_letters:
                print('You have already guessed this letter.')
            else:
                self.guessed_letters.add(guess)
                if guess not in self.secret_word:
                    self.current_attempts += 1
        elif len(guess) > 1 and guess.isalpha():
            if guess == self.secret_word.lower():
                self.guessed_letters = set(self.secret_word)
            else:
                self.current_attempts = self.max_attempts  
        else:
            print('Invalid guess. Please enter alphabet character or the full word.')

    def check_game_status(self):
        if all(letter in self.guessed_letters for letter in self.secret_word):
            return 'win'
        elif self.current_attempts >= self.max_attempts:
            return 'lose'
        else:
            return 'continue'

    def get_current_guesses(self):
        filled_word_letters = [letter if letter in self.guessed_letters else '-' for letter in self.secret_word]
        incorrect_letters = [letter for letter in self.guessed_letters if letter not in self.secret_word]
        return filled_word_letters, self.max_attempts - self.current_attempts, incorrect_letters
    
    def visualize_hangman(self):
        hangman_stage = hangman[self.current_attempts - self.max_attempts-1]
        return hangman_stage


def get_player_name():
    player_name = input("Hello sir/madad. \nPlease enter your name: ")
    return player_name

def ask_to_play():
    while True:
        play_choice = input("Would you like to play Hangman? (yes/no): ").lower()

        if play_choice == "no":
            print("Thank you for considering! Have a great day!")
            return False
        elif play_choice == "yes":
            return True
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

def game():
    guess_attempts = 10

    player_name = get_player_name()
    print(f"Hello, {player_name}!")

    while True:
        if not ask_to_play():
            break
        
        print("Welcome to Hangman Game!")
        print(hangman_logo[0])
        game = HangmanGame(guess_attempts)
        game.start_new_game()
        while True:
            guess = input("\nEnter your guess(letter or even full word): ").lower()
            game.make_guess(guess)

            status = game.check_game_status()

            if status == 'continue':
                filled_word_letters, attempts_left, incorrect_letters = game.get_current_guesses()
                print(f"\nCurrent guessed letters: {filled_word_letters}")
                print(f'\nAttempts left: {attempts_left}')
                # print(f"secret word {game.secret_word}")
                print(f"\nIncorrect Letters: {' '.join(incorrect_letters)}")
                print(game.visualize_hangman())

            elif status == 'win':
                print("Congratulations! You've won the game!")
                print(f"You guessed the word: {game.secret_word}")
                break
            elif status == 'lose':
                print("You've lost the game. Better luck next time!")
                print(game.visualize_hangman())
                print(f"The correct word was: {game.secret_word}")
                break

if __name__ == '__main__':
    game()
import random
from typing import Set, List
from words import words
import pyfiglet
from hangman_art import hangman

class HangmanGame:
    def __init__(self, max_attempts: int):
        self.secret_word: str = ''
        self.max_attempts: int = max_attempts
        self.guessed_letters: Set[str] = set()
        self.current_attempts: int = 0

    def start_new_game(self):
        self.guessed_letters = set()
        self.current_attempts = 0
        category = random.choice(list(words.keys()))
        self.secret_word = random.choice(words[category])

    def make_guess(self, guess: str):
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

    def check_game_status(self) -> str:
        if all(letter in self.guessed_letters for letter in self.secret_word):
            return 'win'
        elif self.current_attempts >= self.max_attempts:
            return 'lose'
        else:
            return 'continue'

    def get_current_state(self) -> List[str]:
        current_state = [letter if letter in self.guessed_letters else ' _ ' for letter in self.secret_word]
        return current_state
    
    def visualize_hangman(self) -> str:
        hangman_stage = hangman[self.current_attempts - self.max_attempts - 1]
        return hangman_stage
    
    
    def get_available_letters(self) -> List[str]:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        available_letters = [letter for letter in alphabet if letter not in self.guessed_letters]
        return available_letters
    
    def get_incorrect_letters(self) -> List[str]:
        incorrect_letters = [letter for letter in self.guessed_letters if letter not in self.secret_word]
        return incorrect_letters

class Personalization:
    def __init__(self):
        self.player_name: str = ""

    def get_player_name(self) -> None:
        self.player_name = input("Please enter your name: ")

    def ask_to_play(self) -> bool:
        while True:
            play_choice = input("Would you like to play Hangman? (yes/no): ").lower()
            if play_choice == "yes":
                return True
            elif play_choice == "no":
                return False
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    def choose_word_category(self) -> str:
        categories = list(words.keys())
        print("Choose a word category:")
        for index, category in enumerate(categories, start=1):
            print(f"{index}. {category.capitalize()}")
        while True:
            try:
                category_choice = input("Enter the number of your choice (or leave empty for random selection): ")
                if not category_choice:
                    return random.choice(categories)
                category_choice = int(category_choice) - 1
                if 0 <= category_choice < len(categories):
                    return categories[category_choice]
                else:
                    print("Invalid category number. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")


def game() -> None:
    guess_attempts: int = 10
    welcome = pyfiglet.figlet_format("Hello sir/madam. \n Welcome to: ")
    hangman_game_logo = pyfiglet.figlet_format("Hangman game!")
    print(welcome)
    print(hangman_game_logo)
    personalization = Personalization()
    personalization.get_player_name()
    player_name: str = personalization.player_name
    name_visualization = pyfiglet.figlet_format(f"Hello {player_name}")
    print(name_visualization)

    while personalization.ask_to_play():
        hangman_game_logo = pyfiglet.figlet_format("Hangman!")
        print(hangman_game_logo)
        print(hangman[0])

        while True:
            game = HangmanGame(guess_attempts)
            game.start_new_game()

            word_category = personalization.choose_word_category()
            if word_category != "":
                game.secret_word = random.choice(words[word_category])

            print(f"Your word is from category: {word_category}")
            print(hangman[0])
            print(f'Available letters: {", ".join(game.get_available_letters())}')

            while True:
                guess = input("\nEnter your guess (letter or even the full word): ").lower()

                game.make_guess(guess)

                status = game.check_game_status()
                correct_word = pyfiglet.figlet_format(game.secret_word)
                if status == 'continue':
                    current_state = "".join(game.get_current_state())
                    available_letters = ", ".join(game.get_available_letters())
                    incorrect_letters = ", ".join(game.get_incorrect_letters())
                    visualize_current_state = pyfiglet.figlet_format(current_state)
                    print(game.visualize_hangman())
                    print(visualize_current_state)
                    print(f'Available letters: {available_letters}')
                    print(f'Incorrect letters: {incorrect_letters}')
                    print(f'\nAttempts left: {game.max_attempts - game.current_attempts}')
                elif status == 'win':
                    print(game.visualize_hangman())
                    win = pyfiglet.figlet_format("Congratulations!")
                    print(win)
                    print("You guessed the word:")
                    print(correct_word)
                    break
                elif status == 'lose':
                    print(game.visualize_hangman())
                    lost = pyfiglet.figlet_format("You've Lost")
                    print(lost)
                    print("The correct word was:")
                    print(correct_word)
                    
                    break

            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                print("Thank you for playing Hangman!")
                goodbye = pyfiglet.figlet_format("Goodbye!")
                print(goodbye)
                return

if __name__ == '__main__':
    game()

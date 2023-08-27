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

    def get_current_state(self):
        current_state = [letter if letter in self.guessed_letters else '-' for letter in self.secret_word]
        return current_state
    
    def visualize_hangman(self):
        hangman_stage = hangman[self.current_attempts - self.max_attempts-1]
        return hangman_stage
    
    def get_available_letters(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        available_letters = [letter for letter in alphabet if letter not in self.guessed_letters]
        return available_letters
    
    def get_incorrect_letters(self):
        incorrect_letters = [letter for letter in self.guessed_letters if letter not in self.secret_word]
        return incorrect_letters

class Personalization:
    def __init__(self):
        self.player_name = ""

    def get_player_name(self):
        self.player_name = input("Hello sir/madam. Welcome to the Hangman game app.\nPlease enter your name: ")

    def ask_to_play(self):
        play_choice = input("Would you like to play Hangman? (yes/no): ").lower()
        return play_choice == "yes"

    def choose_word_category(self):
        categories = list(words.keys())
        print("Choose a word category:")
        for index, category in enumerate(categories, start=1):
            print(f"{index}. {category}")
        category_choice = int(input("Enter the number of your choice: ")) - 1
        if 0 <= category_choice < len(categories):
            return categories[category_choice]
        else:
            print("Invalid category choice. Random category will be selected.")
            return random.choice(categories)

def game():
    guess_attempts = 10
    personalization = Personalization()
    personalization.get_player_name()
    player_name = personalization.player_name
    print(f"Hello, {player_name}!")

    while personalization.ask_to_play():
        print("Welcome to Hangman Game!")
        print(hangman_logo[0])
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

                if status == 'continue':
                    print(game.visualize_hangman())
                    print(f"\nCurrent stage: {game.get_current_state()}")
                    print(f'Available letters: {", ".join(game.get_available_letters())}')
                    print(f'Incorrect letters: {", ".join(game.get_incorrect_letters())}')
                    print(f'\nAttempts left: {game.max_attempts-game.current_attempts}')
                elif status == 'win':
                    print(game.visualize_hangman())
                    print("Congratulations! You've won the game!")
                    print(f"You guessed the word: {game.secret_word}")
                    break
                elif status == 'lose':
                    print("You've lost the game. Better luck next time!")
                    print(game.visualize_hangman())
                    print(f"The correct word was: {game.secret_word}")
                    break

            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                print("Thank you for playing Hangman! Goodbye.")
                return

if __name__ == '__main__':
    game()
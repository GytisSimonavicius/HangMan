import random
from words import words

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
                self.current_attempts = self.max_attempts  # Set attempts to maximum (lose)
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

def game():
    guess_attempts = 10
    game = HangmanGame(guess_attempts)
    game.start_new_game()

    while True:
        guess = input("Enter your guess: ").lower()
        game.make_guess(guess)

        status = game.check_game_status()

        if status == 'continue':
            filled_word_letters, attempts_left, incorrect_letters = game.get_current_guesses()
            print(f"Current guessed letters: {filled_word_letters}")
            print(f'Attempts left: {attempts_left}')
            print(f"Incorrect Letters: {' '.join(incorrect_letters)}")
        elif status == 'win':
            print("Congratulations! You've won the game!")
            print(f"You guessed the word: {game.secret_word}")
            break
        elif status == 'lose':
            print("You've lost the game. Better luck next time!")
            print(f"The correct word was: {game.secret_word}")
            break

if __name__ == '__main__':
    game()

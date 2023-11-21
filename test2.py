import re
from words import word_list
class WordleSolver:
    def __init__(self, word_list):
        self.word_list = word_list
        self.word_length = len(word_list[0])
        self.possible_words = [word for word in word_list if len(word) == self.word_length]
        self.used_words = set()

    def update_possible_words(self, guess, correct_positions):
        pattern = self.create_pattern(guess)
        self.possible_words = [word for word in self.possible_words if pattern.fullmatch(word)]
        self.used_words.add(guess)
        return [word for word in self.possible_words if self.match_positions(word, guess) == correct_positions]

    def create_pattern(self, guess):
        pattern_str = "^" + guess.replace(".", "[a-z]") + "$"
        return re.compile(pattern_str)

    def match_positions(self, word, guess):
        return sum(1 for i, j in zip(word, guess) if i == j)

    def get_letter_frequency(self, words):
        letter_count = {}
        for word in words:
            for letter in word:
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1

        sorted_frequency = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
        return [letter for letter, _ in sorted_frequency]

    def make_guess(self):
        letter_frequency = self.get_letter_frequency(self.possible_words)
        for word in self.possible_words:
            for position in range(self.word_length):
                guess = self.replace_letter(word, letter_frequency[position], position)
                if guess not in self.used_words:
                    return guess

    def replace_letter(self, word, letter, position):
        return word[:position] + letter + word[position + 1:]

    def solve_wordle(self, max_attempts=5):
        for attempt in range(max_attempts):
            guess = self.make_guess()
            print(f"Attempt {attempt + 1}: Guessing {guess}")
            correct_positions = int(input("Enter the number of correct positions: "))
            if correct_positions == self.word_length:
                print(f"Success! The correct word is {guess}")
                break
            else:
                self.possible_words = self.update_possible_words(guess, correct_positions)
                print(f"Remaining possible words: {len(self.possible_words)}")

if __name__ == "__main__":
    word_l = word_list
    solver = WordleSolver(word_l)
    solver.solve_wordle()

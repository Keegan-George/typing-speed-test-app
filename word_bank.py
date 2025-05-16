from random import choice
from config import WORD_FILE_PATH


class WordBank:
    """
    Class for generating and accessing the words.
    """

    def __init__(self):
        self.words = self.create_word_list()
        self.current_word = None
        self.get_random_word()

    def create_word_list(self) -> list[str]:
        """
        Initialize the list of words.
        """
        with open(WORD_FILE_PATH) as words_file:
            return words_file.read().split()

    def get_random_word(self) -> str:
        """
        Get and return a random word from the word list.
        """
        self.current_word = choice(self.words)
        return self.current_word

    def get_current_word(self):
        """
        Return the current word.
        """
        return self.current_word

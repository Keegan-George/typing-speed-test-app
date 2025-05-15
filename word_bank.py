from random import choice
from config import WORD_FILE_PATH


class WordBank:
    """
    Class for generating and accessing the words. 
    """

    def __init__(self):
        self.words = self.create_word_list()
        self.current_word = None
        self.get_word()

    def create_word_list(self) -> list[str]:
        """
        Return the list of words.
        """
        with open(WORD_FILE_PATH) as words_file:
            return words_file.read().split()

    def get_word(self) -> str:
        """
        Return a random word from the word list.
        """
        self.current_word = choice(self.words)
        return self.current_word

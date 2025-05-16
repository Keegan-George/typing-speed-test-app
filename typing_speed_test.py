from config import *
from tkinter import *
from word_bank import WordBank
from typing_test_ui import TypingTestUI
from countdown_timer import CountdownTimer


class TypingSpeedTest:
    def __init__(self):
        self.window = Tk()
        self.word_bank = WordBank()
        self.ui = TypingTestUI(self.window)
        self.timer = CountdownTimer(self.window, self.ui.update_timer)

        # key bindings
        self.window.bind("<Key>", self.timer.start)
        self.window.bind("<space>", self.update_score_and_get_next_word)

        self.correct_words = 0

        self.next_word()

        self.window.mainloop()

    def next_word(self, _event=None):
        """
        Call the ui function to display the next word. 
        """
        self.ui.display_word(self.word_bank.get_random_word())
        self.ui.clear_input()

    def update_score(self, _event=None):
        """
        Call the ui functions to update the score and wpm. 
        """
        if self.word_bank.get_current_word() == self.ui.get_input_text():
            self.correct_words += 1
            self.ui.display_success()

        else:
            self.ui.display_fail()

        self.ui.update_wpm(self.correct_words, self.timer.elapsed_time)

    def update_score_and_get_next_word(self, _event=None):
        """
        Combine updating the score and getting the next word into a single call. 
        """
        self.update_score()
        self.next_word()

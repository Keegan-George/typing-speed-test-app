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
        self.timer = CountdownTimer(self.window, self.ui.timer_label)

        # key bindings
        self.window.bind("<Key>", self.timer.start)
        self.window.bind("<space>", self.update_status_and_get_next_word)

        self.correct_words = 0

        self.next_word()

        self.window.mainloop()

    def next_word(self, _event=None):
        self.ui.display_word(self.word_bank.get_word())
        self.ui.clear_input()

    def update_status(self, _event=None):
        if self.word_bank.current_word == self.ui.input.get()[:-1]:
            self.correct_words += 1
            self.ui.display_success()

        else:
            self.ui.display_fail()

        # if self.timer.elapsed_time:
        #     self.ui.wpm_label.config(
        #         text=f"wpm: {int(self.correct_words/self.timer.elapsed_time * 60)}"
        #     )

        self.ui.update_wpm(self.correct_words, self.timer.elapsed_time)

    def update_status_and_get_next_word(self, _event=None):
        self.update_status()
        self.next_word()

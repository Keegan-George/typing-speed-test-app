from config import *
from tkinter import *
from random import choice
from countdown_timer import CountdownTimer


class TypingSpeedTest:
    def __init__(self):
        self.window = Tk()
        self.window.title("Typing Speed Test")
        self.window.config(padx=10, pady=10)
        self.current_word = None
        self.timer = None
        self.correct_words = 0
        self.elapsed_time = 0

        # create a list of words
        with open("words.txt") as words_file:
            self.words = words_file.read().split()

        self.current_word = choice(self.words)

        # ui widgets
        self.timer_label = Label(text="00:00")
        self.wpm_label = Label(text="wpm: 0")
        self.status_label = Label()
        self.canvas = Canvas(
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
            borderwidth=1,
            highlightbackground="black",
        )
        self.input = Entry(width=50)

        # images
        self.green_check = PhotoImage(file="icons/green_check.png")
        self.red_X = PhotoImage(file="icons/red_X.png")

        # grid positions
        self.wpm_label.grid(row=0, column=0)
        self.status_label.grid(row=0, column=1)
        self.timer_label.grid(row=0, column=2)
        self.canvas.grid(row=1, column=0, pady=10, columnspan=3)
        self.input.grid(row=2, column=0, columnspan=3)

        ##new##
        self.new_timer = CountdownTimer(TEST_DURATION, self.window, self.timer_label)

        # key bindings
        # self.window.bind("<Key>", lambda event: self.countdown_timer(TEST_DURATION))
        self.window.bind("<Key>", self.new_timer.start)
        self.window.bind("<space>", self.update_status_and_get_next_word)

        self.canvas_text = self.canvas.create_text(
            CANVAS_WIDTH // 2,
            CANVAS_HEIGHT // 2,
            text=f"{self.current_word}",
            font=WORD_FONT,
        )

        self.input.focus()

        self.window.mainloop()

    def next_word(self, event):
        self.current_word = choice(self.words)
        self.canvas.itemconfig(self.canvas_text, text=self.current_word)
        self.input.delete(0, END)

    def update_status(self, event):
        if self.current_word == self.input.get()[:-1]:
            self.correct_words += 1
            self.status_label.config(image=self.green_check)
            # reference to image to prevent garbage collection
            self.status_label.iamge = self.green_check

        else:
            self.status_label.config(image=self.red_X)
            # reference to image to prevent garbage collection
            self.status_label.image = self.red_X

        # if self.elapsed_time:
        if self.new_timer.elapsed_time:
            self.wpm_label.config(
                text=f"wpm: {int(self.correct_words/self.new_timer.elapsed_time * 60)}"
            )

    def update_status_and_get_next_word(self, event):
        self.update_status(event)
        self.next_word(event)

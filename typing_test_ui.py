from tkinter import *
from config import WINDOW_PADDING, WINDOW_TITLE, CANVAS_WIDTH, CANVAS_HEIGHT, WORD_FONT


class TypingTestUI:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title(WINDOW_TITLE)
        self.root.config(padx=WINDOW_PADDING, pady=WINDOW_PADDING)

        # timer display
        self.timer_label = Label(text="00:00")
        self.timer_label.grid(row=0, column=2)

        # wpm display
        self.wpm_label = Label(text="wpm: 0")
        self.wpm_label.grid(row=0, column=0)

        # status display
        self.status_label = Label()
        self.status_label.grid(row=0, column=1)

        # user input
        self.input = Entry(width=50)
        self.input.grid(row=2, column=0, columnspan=3)
        self.input.focus()

        # canvas to display word
        self.canvas = Canvas(
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
            borderwidth=1,
            highlightbackground="black",
        )
        self.canvas_text = self.canvas.create_text(
            CANVAS_WIDTH // 2,
            CANVAS_HEIGHT // 2,
            font=WORD_FONT,
        )
        self.canvas.grid(row=1, column=0, pady=10, columnspan=3)

        # status icons
        self.green_check = PhotoImage(file="icons/green_check.png")
        self.red_X = PhotoImage(file="icons/red_X.png")

    def display_word(self, word: str):
        self.canvas.itemconfig(self.canvas_text, text=word)

    def clear_input(self):
        self.input.delete(0, END)

    def display_success(self):
        self.status_label.config(image=self.green_check)

    def display_fail(self):
        self.status_label.config(image=self.red_X)

    def update_wpm(self, score: int, elapsed_time: int):
        if not score or not elapsed_time:
            self.wpm_label.config(text=f"wpm: 0")

        else:
            self.wpm_label.config(text=f"wpm: {score/elapsed_time * 60}")

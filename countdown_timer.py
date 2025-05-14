from config import TEST_DURATION
from tkinter import Tk, Label


class CountdownTimer:
    def __init__(self, count: int, window: Tk, timer_label: Label):
        self.count = count
        self.window = window
        self.timer_label = timer_label
        self.time_remaining = None
        self.elapsed_time = None
        self.after_id = None
        

    def tick(self):
        if self.count < 0:
            self.window.unbind("<space>")
            self.window.after_cancel(self.after_id)

        else:
            self.min = self.count // 60
            self.sec = self.count % 60
            self.timer_label.config(text=f"{self.min:02d}:{self.sec:02d}")
            self.count -= 1
            self.elapsed_time = TEST_DURATION - self.count
            self.after_id = self.window.after(1000, self.tick)

    def start(self, _event=None):
        self.window.unbind("<Key>")
        self.tick()

from config import TEST_DURATION
from tkinter import Tk


class CountdownTimer:
    """
    Class for managing the typing test countdown timer. 
    """

    def __init__(self, root: Tk, update_timer_callback):
        self.count = TEST_DURATION
        self.root = root
        self.update_timer_callback = update_timer_callback
        self.elapsed_time = 0
        self.after_id = None

    def tick(self):
        """
        Decrements the timer by 1 each second.
        """
        if self.count < 0:
            self.root.unbind("<space>")
            self.root.after_cancel(self.after_id)

        else:
            self.min = self.count // 60
            self.sec = self.count % 60
            self.update_timer_callback(self.min, self.sec)
            self.count -= 1
            self.elapsed_time = TEST_DURATION - self.count
            self.after_id = self.root.after(1000, self.tick)

    def start(self, _event=None):
        """
        Start the timer.
        """
        self.root.unbind("<Key>")
        self.tick()

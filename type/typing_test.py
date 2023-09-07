import tkinter as tk
from tkinter import font
import time
import random

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("500x300")

        self.text = tk.StringVar()
        self.start_time = None
        self.total_words = 0

        self.sentences = [
            "This is a typing speed test. Type this sentence as fast as you can!",
            "The quick brown fox jumps over the lazy dog.",
            "Programming is fun when you're good at it!",
            "Practice makes perfect. Keep typing!",
        ]

        self.setup_ui()

    def setup_ui(self):
        title_font = font.Font(family="Helvetica", size=16, weight="bold")
        label_font = font.Font(family="Helvetica", size=12)

        title_label = tk.Label(self.root, text="Typing Speed Test", font=title_font)
        title_label.pack(pady=10)

        self.get_random_sentence()
        text_label = tk.Label(self.root, textvariable=self.text, wraplength=450, justify="center", font=label_font)
        text_label.pack()

        self.entry = tk.Entry(self.root, font=label_font)
        self.entry.pack(pady=10)
        self.entry.bind("<KeyRelease>", self.check_text)

        result_label = tk.Label(self.root, text="Typing speed:", font=label_font)
        result_label.pack()

        self.result_display = tk.Label(self.root, text="", font=label_font)
        self.result_display.pack()

        reset_button = tk.Button(self.root, text="Reset Test", command=self.reset_test)
        reset_button.pack(pady=10)

    def get_random_sentence(self):
        self.current_sentence = random.choice(self.sentences)
        self.text.set(self.current_sentence)

    def check_text(self, event):
        typed_text = self.entry.get()
        if not self.start_time:
            self.start_time = time.time()

        if typed_text == self.current_sentence:
            elapsed_time = time.time() - self.start_time
            words_per_minute = int((len(self.current_sentence) / 5) / (elapsed_time / 60))
            self.result_display.config(text=f"Typing speed: {words_per_minute} WPM", fg="green")
            self.entry.config(state="disabled")
        else:
            self.total_words = len(typed_text.split())
            self.result_display.config(text=f"Words typed: {self.total_words} / {len(self.current_sentence.split())}", fg="black")

    def reset_test(self):
        self.entry.delete(0, "end")
        self.entry.config(state="normal")
        self.get_random_sentence()
        self.result_display.config(text="")
        self.start_time = None

def main():
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import os
import pygame
from tkinter import Tk, filedialog, Label, Button
from tkinter import ttk  # Import themed widgets module

class MP3Player:
    def __init__(self, master):
        self.master = master
        self.master.title("Colorful MP3 Player")
        self.master.geometry("400x200")

        # Use a themed Label for a colorful display
        self.track_var = ttk.Label(self.master, text="No Track Selected", font=("Helvetica", 12), foreground="blue")
        self.track_var.pack(pady=10)

        # Use themed buttons for a colorful interface
        style = ttk.Style()
        style.configure("TButton", foreground="green", background="black", padding=5, font=("Helvetica", 10))

        self.play_button = ttk.Button(self.master, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)

        self.pause_button = ttk.Button(self.master, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=10)

        self.stop_button = ttk.Button(self.master, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=10)

        self.select_button = ttk.Button(self.master, text="Select MP3", command=self.select_music)
        self.select_button.pack(pady=10)

        self.music_file = None
        self.paused = False

    def play_music(self):
        if self.music_file:
            if self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
            else:
                pygame.mixer.init()
                pygame.mixer.music.load(self.music_file)
                pygame.mixer.music.play()

    def pause_music(self):
        if self.music_file:
            pygame.mixer.music.pause()
            self.paused = True

    def stop_music(self):
        if self.music_file:
            pygame.mixer.music.stop()

    def select_music(self):
        self.music_file = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if self.music_file:
            self.track_var.config(text=os.path.basename(self.music_file))

if __name__ == "__main__":
    root = Tk()
    mp3_player = MP3Player(root)
    root.mainloop()

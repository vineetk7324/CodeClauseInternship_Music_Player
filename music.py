import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        
        self.playlist = []
        self.current_track = 0
        
        pygame.init()
        pygame.mixer.init()
        
        self.create_widgets()

    def create_widgets(self):
        # Create UI elements
        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack()

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.pause_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack()

        self.next_button = tk.Button(self.root, text="Next", command=self.next_track)
        self.next_button.pack()

        self.prev_button = tk.Button(self.root, text="Previous", command=self.prev_track)
        self.prev_button.pack()

        self.add_button = tk.Button(self.root, text="Add Music", command=self.add_music)
        self.add_button.pack()

    def add_music(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
        if file_path:
            self.playlist.append(file_path)

    def play_music(self):
        if not self.playlist:
            return

        pygame.mixer.music.load(self.playlist[self.current_track])
        pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def next_track(self):
        self.stop_music()
        self.current_track = (self.current_track + 1) % len(self.playlist)
        self.play_music()

    def prev_track(self):
        self.stop_music()
        self.current_track = (self.current_track - 1) % len(self.playlist)
        self.play_music()

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()

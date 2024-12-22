import tkinter
import customtkinter
import pygame
from threading import Thread
from launch import ToplevelWindow

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Colors
navy_blue = "#000080"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{580}")

        self.music_playing = False  # Variable to track if music is playing

        button = customtkinter.CTkButton(self, text="CTkButton", command=self.button_event_1)
        button.pack(padx=10, pady=10)

        self.switch_var = customtkinter.StringVar(value="off")
        button_switch = customtkinter.CTkSwitch(self, text="Muzika", command=self.switch_event_1,
                                                variable=self.switch_var, offvalue="off", onvalue="on")
        button_switch.pack(padx=20, pady=20)

        self.toplevel_window = None
        
        entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        entry.pack(padx = 20, pady = 20)

        pygame.mixer.init()


    def button_event_1(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)
        else:
            self.toplevel_window.focus()

    def switch_event_1(self):
        if not self.music_playing:
            self.music_playing = True
            def play_sound():
                pygame.mixer.music.load("Music/bells.mp3")
                pygame.mixer.music.play(-1)

            Thread(target=play_sound).start()
        else:
            pygame.mixer.music.stop()
            self.music_playing = False


if __name__ == "__main__":
    app = App()
    app.mainloop()
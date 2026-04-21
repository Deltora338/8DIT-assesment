import tkinter as tk


class Team():
    def __init__(self, players: list[str], venue: str, colour1: str, colour2: str) -> None:
        self.players = players
        self.venue = venue
        self.main_colour = colour1
        self.secondary = colour2


class GUI():
    def __init__(self, parent: tk.Tk):
        self.parent = parent

        self.frame_season = tk.Frame(parent)
        self.frame_season.grid()
        self.frame_options = tk.Frame(self.frame_season)
        self.frame_options.grid()
        self.frame_table = tk.Frame(self.frame_options)
        self.frame_table.grid()

        self.button_2425_season = tk.Button(self.frame_season, text="2024/2025", command=lambda: self.display_season("2024/2025"))
        self.button_2425_season.grid(row=0, column=0)
        self.button_2526_season = tk.Button(self.frame_season, text="2025/2026", command=lambda: self.display_season("2025/2026"))
        self.button_2526_season.grid(row=0, column=1)
        self.button_custom_season_create = tk.Button(self.frame_season, text="Custom", command=lambda: self.display_season("Custom"))
        self.button_custom_season_create.grid(row=0, column=2)

    def display_season(self, season: str):
        print(season)


if (__name__ == "__main__"):
    root: tk.Tk = tk.Tk()
    window: GUI = GUI(root)
    root.mainloop()

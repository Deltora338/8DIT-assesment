import tkinter as tk


class Team():
    def __init__(self, name: str, players: list[str], venue: str, colour1: str, colour2: str, isBye: bool = False) -> None:
        self.name = name
        self.players = players
        self.venue = venue
        self.main_colour = colour1
        self.secondary = colour2
        self.isBye = isBye  # false by default


class Season():
    '''
    stores information about a season, its name (usually something like 2023/2024) whether or
    not it is active (can have results added to it), and its teams
    '''
    def __init__(self, name: str, isActive: bool, teams: list[Team]):
        self.name = name
        self.isActive = isActive
        if (self.nteams % 2 != 0):  # adds a bye option as a team if there is an odd number of teams
            self.teams = teams + [Team(name="bye", players=[], venue="", colour1="", colour2="", isBye=True)]
        else:
            self.teams = teams
        self.teams = teams
        self.nteams = len(teams)

    def generate_schedule(self, teams_list: list[str]) -> list[list[tuple[str, str]]]:
        '''
        this method returns a schedule of all the matches to be played
        '''
        schedule: list[list[tuple[str, str]]] = []
        round: list[tuple[str, str]] = []
        for _ in range(len(teams_list) - 1):
            for j in range(len(teams_list) // 2):
                round.append((teams_list[j], teams_list[len(teams_list) - 1 - j]))
            schedule.append(round)
            round = []
            teams_list.insert(1, teams_list.pop())
        return schedule


class GUI():
    def __init__(self, parent: tk.Tk):
        self.parent = parent

        self.frame_season = tk.Frame(parent)  # frame for choosing season
        self.frame_season.grid()
        self.frame_options = tk.Frame(self.frame_season)  # frame for options within season
        self.frame_options.grid()
        self.frame_table = tk.Frame(self.frame_options)  # frame for table
        self.frame_table.grid()

        self.button_2425_season = tk.Button(self.frame_season, text="2024/2025", command=lambda: self.display_season("2024/2025"))
        self.button_2425_season.grid(row=0, column=0)
        self.button_2526_season = tk.Button(self.frame_season, text="2025/2026", command=lambda: self.display_season("2025/2026"))
        self.button_2526_season.grid(row=0, column=1)
        self.button_custom_season_create = tk.Button(self.frame_season, text="Custom", command=lambda: self.display_season("Custom"))
        self.button_custom_season_create.grid(row=0, column=2)

    def display_season(self, season: str):
        self.button_table = tk.Button(self.frame_options, text="Table", command=lambda: self.display_table(season))
        self.button_matches = tk.Button(self.frame_options, text="Matches", command=lambda: self.display_matches(season))
        self.button_add_game = tk.Button(self.frame_options, text="Enter result", command=lambda: self.add_game(season))

    def display_table(self, season: str):
        pass

    def display_matches(self, season: str):
        pass

    def add_game(self, season: str):
        pass


if (__name__ == "__main__"):
    root: tk.Tk = tk.Tk()
    window: GUI = GUI(root)
    root.mainloop()

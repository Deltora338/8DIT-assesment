import tkinter as tk
import json


class Season():
    '''
    stores information about a season, its name (usually something like 2023/2024) whether or
    not it is active (can have results added to it), and its teams
    '''
    def __init__(self, name: str, teams: list[str], isActive: bool = False):
        self.name = name
        self.isActive = isActive
        self.nteams = len(teams)
        if (self.nteams % 2 != 0):  # adds a bye option as a team if there is an odd number of teams
            self.teams = teams
            self.teams = self.teams.append("bye")
        else:
            self.teams = teams

    def generate_schedule(self, teams_list: list[str], format: int = 2) -> list[list[tuple[str, str]]]:  # default is double header round robin
        '''
        this method returns a schedule of all the matches to be played from a list of teams and
        a format (number of times each team plays each other)
        returns a list of rounds, where each round is a list of matches, and each match is a tuple of the two teams playing
        '''
        use_team_list: list[str] = teams_list
        schedule: list[list[tuple[str, str]]] = []
        round: list[tuple[str, str]] = []
        for i in range(format):  # allows for single/double/triple round robin formats
            for _ in range(len(use_team_list) - 1):
                for j in range(len(use_team_list) // 2):
                    round.append((use_team_list[j], use_team_list[len(use_team_list) - 1 - j]))
                schedule.append(round)
                round = []
                use_team_list.insert(1, use_team_list.pop())
            if i % 2 == 0:  # alternates home and away teams for each round robin
                use_team_list.reverse()

        return schedule

#                                            name,points,mp,   w,   d,   l,   gd,  gf,  ga
    def table(self, season: str) -> list[tuple[str, int, int, int, int, int, int, int, int]] | None:
        with open("data.json", 'r') as file:
            all_data: dict[str, dict[str, dict[str, int | str | list[str]]]] = json.load(file)
            try:
                assert all_data[season]
                data: dict[str, dict[str, int | str | list[str]]] = all_data[season]
            except Exception as e:
                print(f"Error loading season data {season}\nExeption: {e}")
                file.close()
                print("Error loading data")
                return

            table_rows: object = []  # is also annoying to type

            for i in range(len(data)):
                row: object = (  # is annoying to type
                    data[str(i)]["team name"],
                    data[str(i)]["points"],
                    data[str(i)]["matches played"],
                    data[str(i)]["wins"],
                    data[str(i)]["draws"],
                    data[str(i)]["losses"],
                    data[str(i)]["gd"],
                    data[str(i)]["gf"],
                    data[str(i)]["ga"])
                table_rows.append(row)

            print(table_rows)
            file.close()
            return table_rows


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

    seas = Season("2024/2025", ["test"])
    seas.table("seas.name")

import tkinter as tk
import json
import UI_colours as UI_colours


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
    def table(self):
        '''
        gets data for a season if associated data exists and returns it in
        a usable form for displaying data
        '''
        with open("data.json", 'r') as file:  # json file
            all_data: dict[str, dict[str, dict[str, int | str | list[str]]]] = json.load(file)
            try:
                assert all_data[self.name]
                data: dict[str, dict[str, int | str | list[str]]] = all_data[self.name]
            except Exception as e:
                print(f"Error loading season data {self.name}\nExeption: {e}")
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

            file.close()
            return table_rows


class GUI():
    def __init__(self, parent: tk.Tk):
        self.parent = parent
        self.visible_widgets: list[tk.Label | tk.Button] = []

        self.frame_buttons = tk.Frame(parent, bg=UI_colours.WHITE)  # frame for choosing season
        self.frame_buttons.grid(row=0)
        self.frame_display = tk.Frame(parent, bg=UI_colours.WHITE)  # frame for table
        self.frame_display.grid(row=1)

        self.season_names = ["2024/2025", "2025/2026", "Custom"]
        self.season_buttons: list[tk.Button] = []

        for i, buttonName in enumerate(self.season_names):
            if buttonName != "Custom":
                b = tk.Button(self.frame_buttons, text=buttonName, command=lambda: self.display_season(buttonName))
            else:
                b = tk.Button(self.frame_buttons, text=buttonName, command=lambda: self.createCustomSeason())
            b.grid(row=0, column=i)
            self.season_buttons.append(b)

        self.button_2425_season = tk.Button(self.frame_buttons, text="2024/2025", command=lambda: self.display_season("2024/2025"))
        self.button_2425_season.grid(row=0, column=0)
        self.button_2526_season = tk.Button(self.frame_buttons, text="2025/2026", command=lambda: self.display_season("2025/2026"))
        self.button_2526_season.grid(row=0, column=1)
        self.button_custom_season_create = tk.Button(self.frame_buttons, text="Custom", command=lambda: self.display_season("Custom"))
        self.button_custom_season_create.grid(row=0, column=2)

        self.selected_season: Season

        with open("data.json", 'r') as file:
            data = json.load(file)
            teams: list[str] = []
            for team in data["2024/2025"]:
                teams.append(data["2024/2025"][team]["team name"])
            self.selected_season = Season("2024/2025", teams)
            file.close()

    def remove_widgets(self):
        for widget in self.visible_widgets:
            try:
                widget.destroy()
            except Exception as e:
                print(f"Error destorying widget: {widget}")
                print(e)
                self.reset()

    def display_season(self, season: str):
        self.button_table = tk.Button(self.frame_buttons, text="Table", command=lambda: self.display_table(self.selected_season))
        self.button_table.grid(row=1, column=0)
        self.button_matches = tk.Button(self.frame_buttons, text="Matches", command=self.display_matches)
        self.button_matches.grid(row=1, column=1)

        if (self.selected_season.isActive):
            self.button_add_game = tk.Button(self.frame_buttons, text="Enter result", command=self.add_game)
            self.button_add_game.grid(row=1, column=2)

    def display_table(self, season_: Season):
        self.frame_table = tk.Frame(self.frame_display, bg=UI_colours.WHITE)
        self.frame_table.grid(row=0, column=1)
        self.frame_table_icons = tk.Frame(self.frame_display)
        self.frame_table_icons.grid(row=0, column=0)

        table = season_.table()
        try:
            assert table
        except Exception as e:
            print(f"Error loading season table for {season_.name}\nExeption: {e}")
            print("Error loading data")
            return

        max_team_name_length = max(len(row[0]) for row in table)
        team_col_width = max_team_name_length + 5

        labels: list[tk.Label] = []

        header_text = ("  Team                             Pts    MP    W    D     L    GD    GF   GA")

        header_label = tk.Label(self.frame_table,
                                text=header_text,
                                justify=tk.LEFT,
                                font=("Courier New", 8),
                                bg=UI_colours.DARKGRAY,
                                fg=UI_colours.WHITE,)

        labels.append(header_label)

        for i, row in enumerate(table):
            team_name = f'{i + 1}. {row[0]:10}'
            row_text = (
                f'{team_name:<{team_col_width}} '
                f'{row[1]:>4} {row[2]:>4} {row[3]:>4} {row[4]:>4} '
                f'{row[5]:>4} {row[6]:>4} {row[7]:>4} {row[8]:>4}'
            )
            label = tk.Label(
                self.frame_table,
                text=row_text,
                justify=tk.LEFT,
                font=("Courier New", 10),
                bg=UI_colours.WHITE,
                fg=UI_colours.BLACK
            )
            labels.append(label)

        for i, object in enumerate(labels):
            if i == 0:
                object.grid(row=i + 1, column=0, pady=5)
            else:
                object.grid(row=i + 1, column=0, padx=5)
            self.visible_widgets.append(object)

        '''icon_labels: list[tk.Label] = []

        for i, row in enumerate(table):
            icon_image = tk.PhotoImage(file='Team Icon/row[0]')
            image_label = tk.Label(self.frame_table_icons, image=icon_image)
            icon_labels.append(image_label)

        for i, label in enumerate(icon_labels):
            label.grid(row=i + 1, column=0)'''

    def display_matches(self):
        pass

    def add_game(self):
        pass

    def createCustomSeason(self):
        pass


if (__name__ == "__main__"):
    root: tk.Tk = tk.Tk()
    root.configure(bg=UI_colours.WHITE)
    window: GUI = GUI(root)
    root.mainloop()

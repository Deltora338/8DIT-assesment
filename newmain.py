import tkinter as tk
import json

from UI_colours import WHITE
from UI_colours import DARKGRAY
from UI_colours import DEFAULT
from UI_colours import LIGHTBLUE
from UI_colours import OTHERBLUE
from UI_colours import LIGHTGRAY
from UI_colours import LIGHTERGREY


class Season():
    def __init__(self, name: str, filename='new.json'):
        self.filename = filename
        self.name = name
        self.isActive: bool
        self.teams: list[str] = []
        self.nteams: int
        self.teams_info: dict[str, dict[str, list[str] | str | int]] = {}
        self.matches_data: dict[str, list[list[str | int | list[str]]]]

        if self.name != "custom":
            with open(self.filename, 'r') as file:
                # get data and simplify to the parts that each instance will need
                data = json.load(file)
                file.close()  # close file once data is obtained
                data = data[self.name]

                if data:
                    # asign value to isActive
                    self.isActive = data["isActive"]
                    self.isActive = False if self.isActive == 0 else True

                    # create list of teams and asign to self.teams
                    for team in data["teams"]:
                        self.teams.append(team)
                    self.nteams = len(self.teams)

                    # copy each team dictionary from data over to self.teams_info
                    # this includes players, venue, table info and colours
                    for team_name, team_info in data["teams"].items():
                        self.teams_info[team_name] = team_info

            with open('matches.json', 'r') as file:
                data = json.load(file)
                file.close()
                self.matches_data = data[self.name]

    def table(self):
        '''
        is used to make the information from a season ready to be turned into tkinter widgets
        returns a formatted list of relevant data and is called every time rather than making a self.table as data might have changed (in active seasons)
        '''
        table_rows = []
        # for each team in the season, create a list with the wanted information
        for team in self.teams:
            row = [
                team,
                self.teams_info[team]["points"],
                self.teams_info[team]["matches played"],
                self.teams_info[team]["wins"],
                self.teams_info[team]["draws"],
                self.teams_info[team]["losses"],
                self.teams_info[team]["gd"],
                self.teams_info[team]["gf"],
                self.teams_info[team]["ga"]]
            table_rows.append(row)

        # sort list by points in case data is not ordered in json file
        table_rows.sort(key=lambda x: x[1])
        table_rows.reverse()
        return table_rows

    def matches(self):
        matches = []
        MATCHES_PER_SCREEN = 9
        screen = []
        for i, match_info in enumerate(self.matches_data.values()):
            if i % MATCHES_PER_SCREEN == 0:
                matches.append(screen)
                screen = []
            screen.append(match_info)
        if screen:
            matches.append(screen)
        matches.pop(0)

        return matches


class GUI():
    def __init__(self, parent) -> None:
        self.parent = parent

        # top, middle and bottem frames
        self.frame_upper = tk.Frame(parent, bg=LIGHTERGREY)
        self.frame_upper.grid(row=0, column=0, sticky='nsew')

        self.frame_middle = tk.Frame(parent, bg=LIGHTERGREY)
        self.frame_middle.grid(row=1, column=0, sticky='nsew')

        self.frame_lower = tk.Frame(parent, bg=LIGHTERGREY)
        self.frame_lower.grid(row=2, column=0, sticky='nsew')

        self.seasons: list[Season] = []

        # create season objects
        with open('new.json', 'r') as file:
            data = json.load(file)
            for season in data:
                self.seasons.append(Season(season))
            file.close()

        self.selected_season = self.seasons[0]

        # create a corresponding button for each season
        for i, season in enumerate(self.seasons):
            if season == self.selected_season:
                button = tk.Button(self.frame_upper, text=season.name, command=lambda s=season: self.update_middle(s), bg=DEFAULT)
                button.grid(row=0, column=i, pady=5, padx=4)
            else:
                button = tk.Button(self.frame_upper, text=season.name, command=lambda s=season: self.update_middle(s), bg=DEFAULT)
                button.grid(row=0, column=i, pady=5, padx=1)

    def update_upper(self):
        '''
        destroys and recreates buttons in upper frame
        is called when update middle is called as update middle is called when a button (in upper) is pressed in order
        to change the selected button's colour
        '''
        # destroy and recreate frame
        self.frame_upper.destroy()
        self.frame_upper = tk.Frame(self.parent, bg=LIGHTERGREY)
        self.frame_upper.grid(row=0, column=0, sticky='nsew')

        # create a button for each season
        for i, season in enumerate(self.seasons):
            if season == self.selected_season:
                button = tk.Button(self.frame_upper, text=season.name, command=lambda s=season: self.update_middle(s), bg=LIGHTBLUE)
                button.grid(row=0, column=i, pady=5, padx=4)
            else:
                button = tk.Button(self.frame_upper, text=season.name, command=lambda s=season: self.update_middle(s), bg=DEFAULT)
                button.grid(row=0, column=i, pady=5, padx=1)

    def update_middle(self, season: Season):
        '''
        updates middle buttons based on which is selected and whether or not the selected season is active
        called when a season button is hit
        '''
        # update selected season
        self.selected_season = season
        # clear screen and update
        self.update_upper()
        self.reset_lower()

        # destroy and recreate frame
        self.frame_middle.destroy()
        self.frame_middle = tk.Frame(self.parent, bg=LIGHTERGREY)
        self.frame_middle.grid(row=1, column=0, sticky='nsew')

        # create buttons
        self.button_table = tk.Button(self.frame_middle, text="Table", command=lambda: self.display_table(season), bg=DEFAULT)
        self.button_table.grid(row=0, column=0, padx=4, pady=5)

        self.button_matches = tk.Button(self.frame_middle, text="Matches", command=lambda: self.display_matches(season), bg=DEFAULT)
        self.button_matches.grid(row=0, column=1, padx=4, pady=5)

        if season.isActive:
            self.button_add = tk.Button(self.frame_middle, text="Add result", command=lambda: self.add_result(season), bg=DEFAULT)
            self.button_add.grid(row=0, column=3, padx=4, pady=5)

    def reset_lower(self):
        '''
        removes everything in the lower frame by destorying it and recreating it
        '''
        # destroy and recreate frame
        self.frame_lower.destroy()
        self.frame_lower = tk.Frame(self.parent, bg=LIGHTERGREY)
        self.frame_lower.grid(row=2, column=0, sticky='nsew')

    def display_table(self, season: Season):
        '''
        is called when table button is clicked
        takes a season and uses season.table to get table data
        '''
        # first resets the lower frame to clear it
        self.reset_lower()
        self.button_table.configure(bg=OTHERBLUE)
        self.button_matches.configure(bg=DEFAULT)
        # use try except because the add button does not necesarily exist (season inactive)
        try:
            self.button_add.configure(bg=DEFAULT)
        except Exception:
            pass

        # table
        table_rows = season.table()
        # add header row
        table_rows.insert(0, ["Team", "Pts", "MP", "W", "D", "L", "GD", "GF", "GA"])

        for i, row in enumerate(table_rows):
            for j, info in enumerate(row):
                if i == 0:
                    label = tk.Label(self.frame_lower, text=info, bg=DARKGRAY, fg=WHITE, font=("Courier New", 8))
                    label.grid(row=i, column=j, padx=5, pady=5, sticky='w')
                else:
                    if j == 0:
                        label = tk.Label(self.frame_lower, text=f'{i}. {info}', font=("Courier New", 10), bg=LIGHTERGREY)
                        label.grid(row=i, column=j, padx=5, pady=5, sticky='w')
                    else:
                        label = tk.Label(self.frame_lower, text=info, font=("Courier New", 10), bg=LIGHTERGREY)
                        label.grid(row=i, column=j, padx=5, pady=5, sticky='w')

    def display_matches(self, season: Season, index: int = 0):
        '''
        called when matches button is clicked
        '''
        self.reset_lower()
        self.button_matches.configure(bg=OTHERBLUE)
        self.button_table.configure(bg=DEFAULT)
        try:
            self.button_add.configure(bg=DEFAULT)
        except Exception:
            pass

        matches = season.matches()
        nScreens = len(matches)

        # make sure index is in range
        if index > nScreens - 1:
            index = 0
        if index < 0:
            index = nScreens - 1

        # create page number label and previous / next buttons
        self.button_previous = tk.Button(self.frame_lower, text="Previous", command=lambda: self.display_matches(season, index - 1))
        self.button_previous.grid(row=1, column=0, padx=10, pady=5)
        self.button_next = tk.Button(self.frame_lower, text="Next", command=lambda: self.display_matches(season, index + 1))
        self.button_next.grid(row=1, column=4, padx=10, pady=5)
        self.label_page = tk.Label(self.frame_lower, text=f'Page {index + 1}', bg=LIGHTERGREY)
        self.label_page.grid(row=0, column=0)

        c = 0  # column index
        r = 0  # row index

        # create a grid of frames for matches
        for i, item in enumerate(matches[index]):
            r += 1
            if i % 3 == 0:
                c += 1
                r = 0
            frame = tk.Frame(self.frame_lower, bg=LIGHTGRAY)
            frame.grid(row=r, column=c, padx=7, pady=7, sticky='nsew')

            # header label
            print(season.name)
            vs_label = tk.Label(frame, text=f'{item[0][0]} vs {item[1][0]} at {season.teams_info[item[0][0]]["venue"]}', bg=LIGHTGRAY)
            vs_label.grid(row=0, column=0, padx=3, pady=3, columnspan=2)

            row_index = 2
            # team name, score and scoring players beneath
            team_1_label = tk.Label(frame, text=item[0][0], bg=LIGHTGRAY)
            team_1_score_label = tk.Label(frame, text=item[0][1], bg=LIGHTGRAY)
            team_1_label.grid(row=1, column=0, sticky='w')
            team_1_score_label.grid(row=1, column=1, sticky='w')

            if item[0][1] != 0:
                for player in item[0][2]:
                    player_label = tk.Label(frame, text=f'  -{player}', bg=LIGHTGRAY)
                    player_label.grid(row=row_index, column=0, padx=7)
                    row_index += 1

            team_2_label = tk.Label(frame, text=item[1][0], bg=LIGHTGRAY)
            team_2_score_label = tk.Label(frame, text=item[1][1], bg=LIGHTGRAY)
            team_2_label.grid(row=row_index + 1, column=0, sticky='w')
            team_2_score_label.grid(row=row_index + 1, column=1, sticky='w')
            row_index += 2

            if item[1][1] != 0:
                for player in item[1][2]:
                    player_label = tk.Label(frame, text=f'  -{player}', bg=LIGHTGRAY)
                    player_label.grid(row=row_index, column=0, padx=7)
                    row_index += 1

    def add_result(self, season: Season):
        self.reset_lower()
        self.button_add.configure(bg=OTHERBLUE)
        self.button_table.configure(bg=DEFAULT)
        self.button_matches.configure(bg=DEFAULT)


if (__name__ == "__main__"):
    root: tk.Tk = tk.Tk()
    root.configure(bg=WHITE)
    window: GUI = GUI(root)
    root.title("Premier League Application")
    root.mainloop()

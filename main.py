import tkinter as tk
import json
from tkinter import messagebox as msg

from colours_def import *


class Season():
    def __init__(self, name: str, filename: str='data.json'):
        self.filename = filename
        self.name = name
        self.isActive: bool
        self.teams: list[str] = []
        self.nteams: int
        self.teams_info: dict[str, dict[str, list[str] | str | int]] = {}
        self.matches_data: dict[str, list[list[str | int | list[str]]]]

        if self.name != "custom":  # redundant
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

            # get matches history data
            with open('matches.json', 'r') as file:
                data = json.load(file)
                file.close()
                self.matches_data = data[self.name]

    def table(self) -> list[list[str | int | list[str]]]:
        '''
        is used to make the information from a season ready to be turned into tkinter widgets
        returns a formatted list of relevant data and is called every time rather than making a self.table as data might have changed (in active seasons)
        '''
        table_rows: list[list[str | int | list[str]]] = []
        # for each team in the season, create a list with the wanted information
        for team in self.teams:
            row: list[str | int | list[str]] = [
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

    def matches(self) -> list[list[list[list[str | int | list[str]]]]]:
        '''
        takes the self.matches_data and returns a list of X items to be turned into a grid
        '''
        self.update_matches()
        matches: list[list[list[list[str | int | list[str]]]]] = []
        MATCHES_PER_SCREEN = 9  # number of things per page
        screen: list[list[list[str | int | list[str]]]] = []  # variable is used to represent each screen that will be shown when cycling through matches

        for i, match_info in enumerate(self.matches_data.values()):
            if i % MATCHES_PER_SCREEN == 0:  # cut off at designated value
                matches.append(screen)
                screen = []  # reset
            screen.append(match_info)  # idk why pylance doesnt like this
        if screen:  # if number of matches does not divide to the number wanted, simply append whatever is leftover
            matches.append(screen)
        matches.pop(0)  # empty list from 0 division i think

        return matches
    
    # updates self.matches data when new data is added
    def update_matches(self) -> None:
        with open('matches.json', 'r') as file:
            data = json.load(file)
            file.close()
            self.matches_data = data[self.name]
        return


class GUI():
    def __init__(self, parent: tk.Tk) -> None:
        self.parent = parent

        # top, middle and bottom frames
        self.frame_upper = tk.Frame(parent, bg=LIGHTERGREY)
        self.frame_upper.grid(row=0, column=0, sticky='nsew')

        self.frame_middle = tk.Frame(parent, bg=LIGHTERGREY)
        self.frame_middle.grid(row=1, column=0, sticky='nsew')

        self.frame_lower = tk.Frame(parent, bg=LIGHTERGREY)
        self.frame_lower.grid(row=2, column=0, sticky='nsew')

        self.seasons: list[Season] = []

        # create season objects
        with open('data.json', 'r') as file:
            data = json.load(file)
            for season in data:
                self.seasons.append(Season(season))
            file.close()

        self.selected_season = self.seasons[0]

        # create a corresponding button for each season in the data
        for i, season in enumerate(self.seasons):
            if season == self.selected_season:
                button = tk.Button(self.frame_upper, text=season.name, command=lambda s=season: self.update_middle(s), bg=DEFAULT)
                button.grid(row=0, column=i, pady=5, padx=5)
            else:
                button = tk.Button(self.frame_upper, text=season.name, command=lambda s=season: self.update_middle(s), bg=DEFAULT)
                button.grid(row=0, column=i, pady=5, padx=5)

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
                button.grid(row=0, column=i, pady=5, padx=5)
            else:
                button = tk.Button(self.frame_upper, text=season.name, command=lambda s=season: self.update_middle(s), bg=DEFAULT)
                button.grid(row=0, column=i, pady=5, padx=5)

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
        removes everything in the lower frame by destorying it before recreating it for new use
        '''
        # destroy and recreate frame
        self.frame_lower.destroy()
        self.frame_lower = tk.Frame(self.parent, bg=LIGHTERGREY)
        self.frame_lower.grid(row=2, column=0, sticky='nsew')

    def display_table(self, season: Season):
        '''
        is called when table button is clicked
        takes a season and uses season.table to get table data
        works by calling Season.table and then adding in a header row, before looping through each row and creating a label
        '''
        # first resets the lower frame to clear it
        self.reset_lower()
        self.button_table.configure(bg=OTHERBLUE)
        self.button_matches.configure(bg=DEFAULT)
        # use try except because the add button does not necesarily exist (season inactive)
        if season.isActive:
            self.button_add.configure(bg=DEFAULT)

        # table
        table_rows = season.table()

        # add header row
        table_rows.insert(0, ["Team", "Pts", "MP", "W", "D", "L", "GD", "GF", "GA"])

        # loop through each row in descending order, note season.table returns correctly ordered teams
        for i, row in enumerate(table_rows):
            for j, info in enumerate(row):
                if i == 0:  # header is exempt
                    label = tk.Label(self.frame_lower, text=info, bg=DARKGRAY, fg=WHITE, font=("Courier New", 8))  # type: ignore
                    label.grid(row=i, column=j, padx=5, pady=5, sticky='w')
                else:  # regular rows
                    if j == 0:
                        label = tk.Label(self.frame_lower, text=f'{i}. {info}', font=("Courier New", 10), bg=LIGHTERGREY)
                        label.grid(row=i, column=j, padx=5, pady=5, sticky='w')
                    else:
                        label = tk.Label(self.frame_lower, text=info, font=("Courier New", 10), bg=LIGHTERGREY)  # type: ignore
                        label.grid(row=i, column=j, padx=5, pady=5, sticky='w')

    def display_matches(self, season: Season, index: int = 0):
        '''
        called when matches button is clicked
        Creates and displays a grid of matches that has a max width alongside next/previous buttons
        and a page number
        Resets screen, then calls season.matches, checks page index and makes the buttons that are always
        there, then makes n * m grid of frames and puts eachs' information inside of them
        '''
        # start by resetting lower and reconfiuring buttons
        self.reset_lower()
        self.button_matches.configure(bg=OTHERBLUE)
        self.button_table.configure(bg=DEFAULT)

        # add matches button will not be present in inactive seasons
        if season.isActive:
            self.button_add.configure(bg=DEFAULT)

        # Season class method that returns matches data from the asoc json file
        matches = season.matches()
        # because .matches() returns a list of n length lists where each list has 1 screen worth of matches
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
        GRIDWIDTH = 3  # max number of squares accross

        # create a grid of frames for matches
        for i, item in enumerate(matches[index]):
            r += 1
            # each time the iteration reaches a multiple of GRIDWIDTH it moves to the next column and resets row value
            if i % GRIDWIDTH == 0:
                c += 1
                r = 0
            # create a new frame for each location in the grid
            frame = tk.Frame(self.frame_lower, bg=LIGHTGRAY)
            frame.grid(row=r, column=c, padx=7, pady=7, sticky='nsew')

            # header label
            vs_label = tk.Label(frame, text=f'{item[0][0]} vs {item[1][0]} at {season.teams_info[item[0][0]]["venue"]}', bg=LIGHTGRAY)  # type: ignore
            vs_label.grid(row=0, column=0, padx=3, pady=3, columnspan=2)

            # variale to keep track of variable rows
            row_index = 2

            # team name, score and scoring players beneath
            team_1_label = tk.Label(frame, text=item[0][0], bg=LIGHTGRAY)  # type: ignore
            team_1_score_label = tk.Label(frame, text=item[0][1], bg=LIGHTGRAY)  # type: ignore
            team_1_label.grid(row=1, column=0, sticky='w')
            team_1_score_label.grid(row=1, column=1, sticky='w')

            # will only run if the team has scored at least one goal
            if item[0][1] != 0:
                for player in item[0][2]:  # type: ignore
                    player_label = tk.Label(frame, text=f'  -{player}', bg=LIGHTGRAY)
                    player_label.grid(row=row_index, column=0, padx=7)
                    row_index += 1

            # team 2 info display labels
            team_2_label = tk.Label(frame, text=item[1][0], bg=LIGHTGRAY)  # type: ignore
            team_2_score_label = tk.Label(frame, text=item[1][1], bg=LIGHTGRAY)  # type: ignore
            team_2_label.grid(row=row_index + 1, column=0, sticky='w')
            team_2_score_label.grid(row=row_index + 1, column=1, sticky='w')
            row_index += 2

            # will only run if the team has scored at least one goal
            if item[1][1] != 0:
                for player in item[1][2]:  # type: ignore
                    player_label = tk.Label(frame, text=f'  -{player}', bg=LIGHTGRAY)
                    player_label.grid(row=row_index, column=0, padx=7)
                    row_index += 1

    def add_result(self, season: Season, state: int = 0, ) -> None:
        '''
        option to add a match result and update data. This is only place where files get written to
        '''
        # start by clearing any existing widgets if state == 0
        if state == 0:
            self.reset_lower()
            self.button_add.configure(bg=OTHERBLUE)
            self.button_table.configure(bg=DEFAULT)
            self.button_matches.configure(bg=DEFAULT)

            # only reset selected teams when all is reset
            self.team1 = tk.StringVar()
            self.team1.set("Home Team")
            self.team2 = tk.StringVar()
            self.team2.set("Away Team")
            self.team1_score = tk.Variable()
            self.team1_score.set(0)  # type: ignore
            self.team2_score = tk.Variable()
            self.team2_score.set(0)  # type: ignore

            # option menu 1 vars
            team_list = season.teams
            self.option_menu_1 = tk.OptionMenu(self.frame_lower, self.team1, *team_list, command=lambda selection: self.add_result(season, 1))
            self.option_menu_1.grid(row=1, column=0)

            # home header above option menu
            self.label_home = tk.Label(self.frame_lower, text="Home Team", bg=LIGHTERGREY)
            self.label_home.grid(row=0, column=0)
            return

        if state == 1:
            # away header above option menu
            self.label_away = tk.Label(self.frame_lower, text="Away Team", bg=LIGHTERGREY)
            self.label_away.grid(row=0, column=2)

            # vs label
            self.vs_label = tk.Label(self.frame_lower, text=" vs ", bg=LIGHTERGREY)
            self.vs_label.grid(row=1, column=1)

            # option menu 2 vars
            team_list_2 = season.teams.copy()
            team_list_2.remove(self.team1.get())

            # away team option menu
            self.option_menu_2 = tk.OptionMenu(self.frame_lower, self.team2, *team_list_2, command=lambda selection: self.add_result(season, 2))
            self.option_menu_2.grid(row=1, column=2)
            return

        if state == 2:
            # remove used widgets
            self.option_menu_1.destroy()
            self.option_menu_2.destroy()
            self.label_away.destroy()
            self.label_home.destroy()

            # update to new header
            self.vs_label.configure(text=f'{self.team1.get()} vs {self.team2.get()}')
            self.vs_label.grid_forget()
            self.vs_label.grid(row=0, column=0, padx=7, pady=5, sticky='s')

            # create new widgets

            # team1 score entry
            self.entry_1 = tk.Entry(self.frame_lower, textvariable=self.team1_score)
            self.entry_1.grid(row=1, column=0, sticky='ew', padx=10)
            # label that displays vs
            self.vs = tk.Label(self.frame_lower, text=" vs ", bg=LIGHTERGREY)
            self.vs.grid(row=1, column=1, padx=10, pady=7)
            # team2 score entry
            self.entry_2 = tk.Entry(self.frame_lower, textvariable=self.team2_score)
            self.entry_2.grid(row=1, column=2, sticky='ew', padx=10)
            # check button that makes sure integers are entered
            self.next_button = tk.Button(self.frame_lower, text="Check", command=lambda: self.add_result(season, 3), bg=LIGHTGRAY)
            self.next_button.grid(row=2, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)
            # create cancel button
            self.cancel_button = tk.Button(self.frame_lower, text="Cancel", command=lambda: self.add_result(season, 0), bg=LIGHTGRAY)
            self.cancel_button.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)
            return

        if state == 3:
            try:
                # if either of the int() statements fail that means that a non int-able number has been entered
                self.score1 = int(self.entry_1.get())
                self.score2 = int(self.entry_2.get())
                # if there is no error then continue on
                self.entry_1.destroy()
                self.entry_2.destroy()
                self.vs.destroy()
                # change check button to continue
                self.next_button.configure(command=lambda: self.add_result(season, 4), text="Continue")
                # update x vs y label
                self.vs_label.configure(text=f'{self.team1.get()} ({self.score1}) vs ({self.score2}) {self.team2.get()}')
            except Exception:
                msg.showerror("Invalid Score", "Please enter an integer as a score")
                return

        if state == 4:
            # remove next button
            self.next_button.destroy()
            # load players
            self.team_1_players = season.teams_info[self.team1.get()]["players"]
            self.team_2_players = season.teams_info[self.team2.get()]["players"]

            # list of the scoring players
            self.team_1_scoring_players: list[tk.StringVar] = []
            self.team_2_scoring_players: list[tk.StringVar] = []

            row_index = 0 # for keeping track of most recent used row
            if self.score1 != 0:
                for i in range(self.score1):
                    row_index += 1

                    # create a player for each goal
                    player = tk.StringVar()
                    # add it to the list of players 
                    self.team_1_scoring_players.append(player)

                    # label
                    self.team1_scorer_label = tk.Label(self.frame_lower, text=f'{self.team1.get()} scorers:', bg=DARKGRAY)
                    self.team1_scorer_label.grid(row=3, column=0, padx=5, pady=5)

                    # create an option menu for each goal
                    optionmenu = tk.OptionMenu(self.frame_lower, player, *self.team_1_players)  # type: ignore
                    optionmenu.grid(row=i+4, column=0, pady=5)

            if self.score2 != 0:
                for i in range(self.score2):
                    # make player variable for each goal and add to list of players
                    player = tk.StringVar()
                    self.team_2_scoring_players.append(player)

                    # label for team 2 scorers
                    self.team2_scorer_label = tk.Label(self.frame_lower, text=f'{self.team2.get()} scorers:', bg=DARKGRAY)
                    self.team2_scorer_label.grid(row=3, column=1, pady=5, padx=5)

                    # create an option menu for each goal
                    optionmenu = tk.OptionMenu(self.frame_lower, player, *self.team_2_players)  # type: ignore
                    optionmenu.grid(row=i+4, column=1, pady=5)

            # finish button for once all option menus have been filled
            self.button_finish = tk.Button(self.frame_lower, text="Finish", command=lambda: self.add_result(season, 5))
            # use row=6 + row_index to ensure it is below all of the option menus
            self.button_finish.grid(row=6+row_index, column=0, columnspan=2)

            # update position of cancel button so that it remains at the bottem of the screen
            self.cancel_button.grid(row=7+row_index)

        if state == 5:
            # check to make sure all players have been selected and that they are valid (in the team)
            for player in self.team_1_scoring_players:
                if player.get() not in self.team_1_players:  # type: ignore
                    msg.showerror("Invalid Player", f"Please select a player for {self.team1.get()}")
                    return

            # check to make sure all players have been selected and that they are valid (in the team)
            for player in self.team_2_scoring_players:
                if player.get() not in self.team_2_players:  # type: ignore
                    msg.showerror("Invalid Player", f"Please select a player for {self.team2.get()}")
                    return
            # if score is 0-0 then make empty
            if self.score1 == 0 and self.score2 == 0:
                self.new_match: list[list[str | int | list[str]]] = [
                    [self.team1.get(), 0, []],
                    [self.team2.get(), 0, []]
                ]
            else:
                # score is not 0-0 so make new match with scores and players
                self.new_match = [
                    [self.team1.get(), self.score1, [player.get() for player in self.team_1_scoring_players]],
                    [self.team2.get(), self.score2, [player.get() for player in self.team_2_scoring_players]]
                ]
            
            # get existing data
            with open('matches.json', 'r') as file:
                data = json.load(file)
                file.close()
            
            # find new key value for new match
            new_key = str(len(data[season.name].keys()) + 1)

            # update data
            data[season.name][new_key] = self.new_match

            # write new data to file
            with open('matches.json', 'w') as file:
                json_str = json.dumps(data, indent=4)
                file.write(json_str)
                file.close()
            
            # confirmation message and update screen
            msg.showinfo("Result Added", "The result has been added to the season's matches")
            self.display_matches(season) # go to display matches to show new game
            return



if (__name__ == "__main__"):
    root: tk.Tk = tk.Tk()
    root.configure(bg=WHITE)
    window: GUI = GUI(root)
    root.title("Premier League Application")
    root.mainloop()

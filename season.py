"""
class for individual seasons
"""

import json

class Season():
    def __init__(self, name: str, filename='new.json'):
        self.filename = filename
        self.name = name
        self.isActive: bool
        self.teams: list[str] = []
        self.nteams: int
        self.teams_info: dict[str, dict[str, list[str] | str | int]] = {}

        with open(self.filename, 'r') as file:
            # get data and simplify to the parts that each instance will need
            data = json.load(file)
            file.close() # close file once data is obtained
            data = data[self.name]

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
        return table_rows


if __name__ == "__main__":
    test = Season("2024/2025")
    test.table()

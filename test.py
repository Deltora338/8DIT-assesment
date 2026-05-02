import json

with open('data.json', 'r') as file:
    data = json.load(file)
    new_data = {}
    for key in data:
        new_data[key] = {
            "isActive": 0,
            "teams": {}
        }
    for outer_key, inner_dict in data.items():
        for inner_key, values in inner_dict.items():
            new_data["2024/2025"]["teams"][values["team name"]] = {
                "players": values["players"],
                "venue": values["venue"],
                "points": values["points"],
                "matches played": values["matches played"],
                "wins": values["wins"],
                "draws": values["draws"],
                "losses": values["losses"],
                "gd": values["gd"],
                "gf": values["gf"],
                "ga": values["ga"]
                }
    file.close()

with open('team_colours.json', 'r') as file:
    data = json.load(file)
    for team in new_data["2024/2025"]["teams"]:
        for team2 in data:
            if team == team2:
                new_data["2024/2025"]["teams"][team]["1st colour"] = data[team2]["1st"]
                new_data["2024/2025"]["teams"][team]["2nd colour"] = data[team2]["2nd"]
    file.close()

if __name__ == "will overwite file": ##
    with open('new.json', "w") as file:
        json_str = json.dumps(new_data, indent=4)
        file.write(json_str)
        file.close()
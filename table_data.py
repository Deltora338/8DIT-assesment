'''
file contains information and code about the teams to make the data.json file
'''

# import json

stadiums = {
    "Arsenal": "Emirates Stadium",
    "Aston Villa": "Villa Park",
    "Bournemouth": "Vitality Stadium (Dean Court)",
    "Brentford": "Gtech Community Stadium",
    "Brighton & Hove Albion": "American Express Stadium (Falmer Stadium)",
    "Chelsea": "Stamford Bridge",
    "Crystal Palace": "Selhurst Park",
    "Everton": "Goodison Park",
    "Fulham": "Craven Cottage",
    "Ipswich Town": "Portman Road",
    "Leicester City": "King Power Stadium",
    "Liverpool": "Anfield",
    "Manchester City": "Etihad Stadium",
    "Manchester United": "Old Trafford",
    "Newcastle United": "St James' Park",
    "Nottingham Forest": "The City Ground",
    "Southampton": "St Mary's Stadium",
    "Tottenham Hotspur": "Tottenham Hotspur Stadium",
    "West Ham United": "London Stadium",
    "Wolverhampton Wanderers": "Molineux Stadium"
}

players = {
    "Arsenal": ["David Raya", "William Saliba", "Gabriel Magalhães", "Ben White", "Jurrien Timber", "Declan Rice", "Martin Ødegaard", "Mikel Merino", "Bukayo Saka", "Kai Havertz", "Gabriel Martinelli", "Leandro Trossard", "Riccardo Calafiori"],
    "Aston Villa": ["Emiliano Martínez", "Ezri Konsa", "Pau Torres", "Lucas Digne", "Ian Maatsen", "Amadou Onana", "Youri Tielemans", "John McGinn", "Morgan Rogers", "Leon Bailey", "Ollie Watkins", "Jhon Durán", "Ross Barkley"],
    "Bournemouth": ["Kepa Arrizabalaga", "Illia Zabarnyi", "Marcos Senesi", "Milos Kerkez", "Lewis Cook", "Ryan Christie", "Marcus Tavernier", "Antoine Semenyo", "Justin Kluivert", "Evanilson", "Enes Ünal"],
    "Brentford": ["Mark Flekken", "Nathan Collins", "Ethan Pinnock", "Sepp van den Berg", "Vitaly Janelt", "Christian Nørgaard", "Mathias Jensen", "Mikkel Damsgaard", "Bryan Mbeumo", "Yoane Wissa", "Kevin Schade"],
    "Brighton & Hove Albion": ["Bart Verbruggen", "Lewis Dunk", "Jan Paul van Hecke", "Pervis Estupiñán", "Jack Hinshelwood", "Carlos Baleba", "Mats Wieffer", "Kaoru Mitoma", "Georginio Rutter", "Danny Welbeck", "João Pedro"],
    "Chelsea": ["Robert Sánchez", "Levi Colwill", "Wesley Fofana", "Marc Cucurella", "Malo Gusto", "Moisés Caicedo", "Enzo Fernández", "Cole Palmer", "Noni Madueke", "Jadon Sancho", "Nicolas Jackson", "Pedro Neto"],
    "Crystal Palace": ["Dean Henderson", "Marc Guéhi", "Maxence Lacroix", "Trevoh Chalobah", "Tyrick Mitchell", "Daniel Muñoz", "Adam Wharton", "Cheick Doucouré", "Eberechi Eze", "Jean-Philippe Mateta", "Ismaïla Sarr"],
    "Everton": ["Jordan Pickford", "James Tarkowski", "Jarrad Branthwaite", "Vitaliy Mykolenko", "Abdoulaye Doucouré", "Idrissa Gueye", "Orel Mangala", "Dwight McNeil", "Jack Harrison", "Dominic Calvert-Lewin", "Iliman Ndiaye"],
    "Fulham": ["Bernd Leno", "Joachim Andersen", "Calvin Bassey", "Antonee Robinson", "Kenny Tete", "Sander Berge", "Andreas Pereira", "Emile Smith Rowe", "Alex Iwobi", "Adama Traoré", "Raúl Jiménez"],
    "Ipswich Town": ["Arijanet Muric", "Jacob Greaves", "Dara O'Shea", "Leif Davis", "Sam Morsy", "Kalvin Phillips", "Jack Taylor", "Omari Hutchinson", "Sammie Szmodics", "Liam Delap", "Wes Burns"],
    "Leicester City": ["Mads Hermansen", "Wout Faes", "Jannik Vestergaard", "James Justin", "Harry Winks", "Wilfred Ndidi", "Oliver Skipp", "Facundo Buonanotte", "Stephy Mavididi", "Jordan Ayew", "Jamie Vardy"],
    "Liverpool": ["Alisson Becker", "Virgil van Dijk", "Ibrahima Konaté", "Trent Alexander-Arnold", "Andy Robertson", "Ryan Gravenberch", "Alexis Mac Allister", "Dominik Szoboszlai", "Mohamed Salah", "Luis Díaz", "Darwin Núñez", "Diogo Jota"],
    "Manchester City": ["Ederson", "Rúben Dias", "Manuel Akanji", "Josko Gvardiol", "Kyle Walker", "Mateo Kovacic", "Ilkay Gündogan", "Kevin De Bruyne", "Phil Foden", "Bernardo Silva", "Erling Haaland", "Jack Grealish"],
    "Manchester United": ["André Onana", "Lisandro Martínez", "Matthijs de Ligt", "Diogo Dalot", "Noussair Mazraoui", "Kobbie Mainoo", "Manuel Ugarte", "Bruno Fernandes", "Marcus Rashford", "Alejandro Garnacho", "Rasmus Højlund"],
    "Newcastle United": ["Nick Pope", "Fabian Schär", "Sven Botman", "Dan Burn", "Bruno Guimarães", "Sandro Tonali", "Joelinton", "Anthony Gordon", "Harvey Barnes", "Alexander Isak", "Jacob Murphy"],
    "Nottingham Forest": ["Matz Sels", "Murillo", "Nikola Milenkovic", "Ola Aina", "Alex Moreno", "Elliot Anderson", "Ryan Yates", "Morgan Gibbs-White", "Anthony Elanga", "Callum Hudson-Odoi", "Chris Wood"],
    "Southampton": ["Aaron Ramsdale", "Jan Bednarek", "Taylor Harwood-Bellis", "Kyle Walker-Peters", "Flynn Downes", "Joe Aribo", "Mateus Fernandes", "Tyler Dibling", "Adam Armstrong", "Cameron Archer"],
    "Tottenham Hotspur": ["Guglielmo Vicario", "Cristian Romero", "Micky van de Ven", "Destiny Udogie", "Pedro Porro", "Rodrigo Bentancur", "James Maddison", "Dejan Kulusevski", "Brennan Johnson", "Heung-min Son", "Dominic Solanke"],
    "West Ham United": ["Alphonse Areola", "Max Kilman", "Jean-Clair Todibo", "Emerson", "Aaron Wan-Bissaka", "Guido Rodríguez", "Tomas Soucek", "Lucas Paquetá", "Jarrod Bowen", "Mohammed Kudus", "Michail Antonio"],
    "Wolverhampton Wanderers": ["José Sá", "Toti Gomes", "Santiago Bueno", "Rayan Aït-Nouri", "Nélson Semedo", "André", "João Gomes", "Mario Lemina", "Matheus Cunha", "Jean-Ricner Bellegarde", "Jørgen Strand Larsen"]
}

# Format: (Team Name, Points, Wins, Draws, Losses, GD, GF, GA)
table: list[tuple[str, int, int, int, int, int, int, int]] = [
    ("Liverpool", 84, 25, 9, 4, 45, 86, 41),
    ("Arsenal", 74, 20, 14, 4, 35, 69, 34),
    ("Manchester City", 71, 21, 8, 9, 28, 72, 44),
    ("Chelsea", 69, 20, 9, 9, 21, 64, 43),
    ("Newcastle United", 66, 20, 6, 12, 21, 68, 47),
    ("Aston Villa", 66, 19, 9, 10, 7, 58, 51),
    ("Nottingham Forest", 65, 19, 8, 11, 12, 58, 46),
    ("Brighton & Hove Albion", 61, 16, 13, 9, 7, 66, 59),
    ("Bournemouth", 56, 15, 11, 12, 12, 58, 46),
    ("Brentford", 56, 16, 8, 14, 9, 66, 57),
    ("Fulham", 54, 15, 9, 14, 0, 54, 54),
    ("Crystal Palace", 53, 13, 14, 11, 0, 51, 51),
    ("Everton", 48, 11, 15, 12, -2, 42, 44),
    ("West Ham United", 43, 11, 10, 17, -16, 46, 62),
    ("Manchester United", 42, 11, 9, 18, -10, 44, 54),
    ("Wolverhampton Wanderers", 42, 12, 6, 20, -15, 54, 69),
    ("Tottenham Hotspur", 38, 11, 5, 22, -1, 64, 65),
    ("Leicester City", 25, 6, 7, 25, -47, 33, 80),
    ("Ipswich Town", 22, 4, 10, 24, -46, 36, 82),
    ("Southampton", 12, 2, 6, 30, -60, 26, 86)
]

data2: dict[str, dict[int, dict[str, int | str | list[str]]]] = {
    "2024/2025": {

    }
}

for i, team in enumerate(table):
    data2["2024/2025"][i] = {}
    data2["2024/2025"][i]["team name"] = table[i][0]
    data2["2024/2025"][i]["players"] = players[table[i][0]]
    data2["2024/2025"][i]["venue"] = stadiums[table[i][0]]
    data2["2024/2025"][i]["points"] = table[i][1]
    data2["2024/2025"][i]["matches played"] = table[i][2] + table[i][3] + table[i][4]
    data2["2024/2025"][i]["wins"] = table[i][2]
    data2["2024/2025"][i]["draws"] = table[i][3]
    data2["2024/2025"][i]["losses"] = table[i][4]
    data2["2024/2025"][i]["gd"] = table[i][5]
    data2["2024/2025"][i]["gf"] = table[i][6]
    data2["2024/2025"][i]["ga"] = table[i][7]


'''if __name__ == "__main__":

    with open('data.json', 'w') as file:
        json_str = json.dumps(data2, indent=4)
        file.write(json_str)
        file.close()'''

'''
DO NOT run may overwrite data.json
only restores 2024/2025 season data and I can provide no garuntee that the format that 
this file uses is still compatible with main functionality
'''

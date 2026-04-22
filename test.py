teams = ["Team A", "Team B", "Team C", "Team D", "Team E", "Team F", "Team G", "Bye"]


def schedule_generation(teams_list: list[str], format: int = 1) -> list[list[tuple[str, str]]]:
    schedule: list[list[tuple[str, str]]] = []
    round: list[tuple[str, str]] = []
    for _ in range(format):
        for _ in range(len(teams_list) - 1):
            for j in range(len(teams_list) // 2):
                round.append((teams_list[j], teams_list[len(teams_list) - 1 - j]))
            schedule.append(round)
            round = []
            teams_list.insert(1, teams_list.pop())
    return schedule


new_schedule = schedule_generation(teams, 2)
for round in new_schedule:
    print(round)

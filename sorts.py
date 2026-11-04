import files

def get_sorted_teams():
    teams = files.get_file_content(files.TEAMS)
    return sorted(teams, key=lambda t: (t["points"], t["goals_for"] - t["goals_against"], t["goals_for"], t["name"]), reverse=True)


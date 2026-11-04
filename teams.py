import files
import inputs


def get_team(key, value):
    teams = files.get_file_content(files.TEAMS)
    for team in teams:
            if team[key] == value:
                return team
    

def get_team_by_id(team_id):
    return get_team("id", team_id)


def get_team_by_name(team_name):
    return get_team("name", team_name)


def is_valid_team(key, value):
    if get_team(key, value) is None:
        return False
    return True



def create_team_object():
    team = {
    "id": inputs.get_number("Enter team ID:"),
    "name": inputs.get_string("Enter team name:").lower(),
    "played": 0,
    "wins": 0, "draws": 0, "losses": 0,
    "goals_for": 0, "goals_against": 0, "points": 0
}
    return team


def add_new_team():
    team = create_team_object()
    if not (is_valid_team("id", team["id"]) or is_valid_team("name", team["name"])):
        teams = files.get_file_content(files.TEAMS)
        teams.append(team)
        files.write_to_file(files.TEAMS, teams)
    else:
        print("already exist")
        

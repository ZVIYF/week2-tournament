from files import write_to_file, get_file_content, TEAMS
import inputs


def get_team(key, value):
    teams = get_file_content(TEAMS)
    for team in teams:
            if team[key] == value:
                return team
    


def get_team_by_id(team_id):
    return get_team("id", team_id)

def get_team_by_name(team_name):
    return get_team("name", team_name)


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
    if not (get_team_by_id(team["id"]) or get_team_by_name(team["name"])):
        teams = get_file_content(TEAMS)
        teams.append(team)
        write_to_file(TEAMS, teams)
        

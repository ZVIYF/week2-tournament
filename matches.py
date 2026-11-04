from teams import *


def get_team(key, value):
    matches = get_file_content(MATCHES)
    for match in matches:
            if match[key] == value:
                return match


def create_match_object():
    a_match = {
    "home_team_id": inputs.get_number("Enter home team ID:"),
    "away_team_id": inputs.get_number("Enter away team ID:"),
    "home_goals": inputs.get_number("Enter home team goals:"),
    "away_goals": inputs.get_number("Enter away team goals:")
}
    return a_match

def is_match_exist(match):
    new_teams = [match["home_team_id"], match["away_team_id"]]
    matches = get_file_content(MATCHES)
    for m in matches:
        old_teams = [m["home_team_id"], m["away_team_id"]]
        if old_teams[0] in new_teams and old_teams[1] in new_teams:
            return True
    return False
        


def is_valid_match(match):
    not_same = match["home_team_id"] != match["away_team_id"]
    home = is_valid_team(match["home_team_id"])
    away = is_valid_team(match["away_team_id"])
    home_goals = match["home_goals"] >= 0
    away_goals = match["away_goals"] >= 0
    return not_same and home and away and home_goals and away_goals


def add_new_match():
    match = create_match_object()
    if is_valid_match(match):
        if is_match_exist(match):
            matches = get_file_content(MATCHES)
            matches.append(match)
            write_to_file(MATCHES, matches)
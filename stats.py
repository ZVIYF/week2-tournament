import matches

def is_draw(match):
    return match["home_team_goals"] == match["away_team_goals"]


def is_winner(location, match):
    if location == "home":
        return match["home_team_goals"] > match["away_team_goals"]

        

def update_teams_info(match):
    teams = matches.get_file_content(matches.TEAMS)
    for t in teams:
        if match["home_team_id"] == t["id"]:
            t["played"] += 1
            t["goals_for"] += match["home_team_goals"]
            t["goals_against"] += match["away_team_goals"]
            if is_draw():
                t["draws"] += 1

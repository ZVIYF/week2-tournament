from files import write_to_file, get_file_content, MATCHES
import inputs


def get_team(key, value):
    matches = get_file_content(MATCHES)
    for team in teams:
            if team[key] == value:
                return team

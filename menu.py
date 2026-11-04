import inputs, prints, stats, matches, teams
from files import write_to_file, get_file_content, TEAMS, MATCHES

def want_exit_program():
    while True:
        try:    
            choice = inputs.get_string("Exit?  y/n").lower()
            match choice:
                case "y":
                    return True
                case "n":
                    return False
                case _:
                    raise ValueError("choice must be y/n")
        except ValueError as error:
            print(f"error: {error}")

def main_menu():
    exit = False
    while not exit:
            try:
                prints.print_main_menu()
                choice = inputs.get_number("Choose an option:")
                match choice:
                    case 1:
                        teams.add_new_team()
                        exit = want_exit_program()                            
                    case 2:
                        prints.print_teams(get_file_content(TEAMS))
                        exit = want_exit_program()
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        pass
                    case 6:
                        pass
                    case 7:
                        pass
                    case 8:
                        pass
                    case 9:
                        pass
                    case 10:
                        pass
                    case 0:
                        exit = want_exit_program()
                    case _:
                        raise ValueError("Choice must be a number between 0-10")
            except ValueError as error:
                print(f"error: {error}")

        

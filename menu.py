import inputs, prints, stats, matches, teams, files, sorts

def want_exit_program():
    while True:
        choice = inputs.get_string("Exit?  y/n").lower()
        try:    
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
                    case 2:
                        prints.print_teams(files.get_file_content(files.TEAMS))
                    case 3:
                        matches.add_new_match()
                    case 4:
                        prints.print_teams(sorts.get_sorted_teams)
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
                        break
                    case _:
                        raise ValueError("Choice must be a number between 0-10")
            except ValueError as error:
                print(f"error: {error}")
            exit = want_exit_program()
            

if __name__ == "__main__":
    main_menu()
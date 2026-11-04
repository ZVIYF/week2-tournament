

def print_main_menu():
        print(
"========== TOURNAMENT MANAGER ==========",
"1. Add team",
"2. Show all teams",
"3. Add match result",
"4. Show standings",
"5. Show leading team",
"6. Show best attacking team",
"7. Show team success rate",
"8. Show teams without wins",
"9. Show tournament summary",
"10. Check championship potential",
"0. Exit",
sep="\n\t"
)


     

def print_team_info(team:dict):
    print("",
        "Team id:".ljust(10), team["id"],"\n",
        "Team name:".ljust(10), team["name"],"\n",
        "Played:".ljust(10), team["played"],"\n",
        "Points:".ljust(10), team["points"],"\n\n"
        )

def print_teams(teams:list):
    if not teams:
        print("No teams to show")
    else:
         for t in teams:
              print_team_info(t)
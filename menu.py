import inputs

def get_menu_choice(num_limit):
    while True:
        choice = inputs.get_number("Choose an option:")
        if choice < num_limit:
                return choice
        print(f"Choice must be lower then {num_limit}")
             
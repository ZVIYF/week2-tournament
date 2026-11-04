import inputs

def get_menu_choice(num_limit):
    while True:
        choice = inputs.get_number("Choose an option:")
        try:
            if choice < num_limit:
                    return choice
            raise ValueError(f"Choice must be lower then {num_limit}")
        except ValueError as error:
             
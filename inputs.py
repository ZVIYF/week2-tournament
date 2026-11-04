def get_string(message):
    while True:
        user_input = input(message).strip()
        if user_input:
            return user_input
        raise ValueError

def get_number(message):
    while True:
        user_input = get_string(message)
        try:
            return int(user_input)
        except ValueError as error:
            
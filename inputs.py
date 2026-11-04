def get_string(message):
    while True:
        user_input = input(message).strip()
        if user_input:
            return user_input
        print("must be a string")

def get_number(message):
    while True:
        user_input = get_string(message)
        if user_input.is_digit():
             return int(user_input)
        print("must be a number")
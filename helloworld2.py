# Get user name

get_user_name = str(input("Enter your name\n>>> "))


# Print: say "hello" && username
if get_user_name == "":
    print("Hello, user") # for default input
else:
    print(f"Hello, {get_user_name.capitalize()}")
    
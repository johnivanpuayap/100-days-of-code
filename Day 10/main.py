# Functions with Outputs

def format_name(f_name, l_name):
    if f_name == "" and l_name == "":
        return "You didn't provide valid inputs"

    name = f_name.title() + " " + l_name.title()
    return name

print(format_name(input("What is your first name?: "), input("What is your last name?: "),))
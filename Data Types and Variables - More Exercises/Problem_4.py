# 4. Balanced Brackets

# I will need to fix it :(

def check_brackets(input_string):
    stack = []
    for char in input_string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            last_bracket = stack.pop()
            if last_bracket != "(":
                return False
    return not stack


user_input = input("Enter a string with brackets: ")

if check_brackets(user_input):
    print("Brackets are closed correctly.")
else:
    print("Brackets are not closed correctly.")

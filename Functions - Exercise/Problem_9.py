# 9. Password Validator

def password_valid_check(password):
    banned_symbols = [",", ".", "!", "?", ";", "@", "#",
                      "$", "%", "^", "&", "*", "-", "_",
                      "(", ")", "[", "]", "{", "}", "<", ">"]

    digit_count = 0
    valid = True

    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        valid = False

    for symbol in password:

        if symbol in banned_symbols:
            print("Password must consist only of letters and digits")
            valid = False
            break
        else:
            pass

        if digit_count < 2:
            if symbol.isdigit():
                digit_count += 1

    if digit_count < 2:
        print("Password must have at least 2 digits")
        valid = False

    if valid:
        print("Password is valid")


password = input()


password_valid_check(password)

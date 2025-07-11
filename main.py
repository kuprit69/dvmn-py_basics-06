def has_letters(password):
    return any(i.isalpha() for i in password)


def has_upper_letters(password):
    return any(i.isupper() for i in password)


def has_lower_letters(password):
    return any(i.islower() for i in password)


def has_symbols(password):
    return any(not i.isdigit() and not i.isalpha() for i in password)


def has_digit(password):
    return any(i.isdigit() for i in password)


def is_very_long(password):
    return len(password) > 12


password = input("Введите пароль: ")

score = 0
if is_very_long(password):
    score += 2
if has_digit(password):
    score += 2
if has_letters(password):
    score += 2
if has_upper_letters(password):
    score += 2
if has_symbols(password):
    score += 2

print("Рейтинг пароля:", score, "из 10")


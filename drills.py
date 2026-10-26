def first_and_last(value):
    if not value:
        return {
            "first": "",
            "last": ""
        }
    first_character = value[0]
    last_character = value[-1]
    first_and_last = {
        "first": first_character,
        "last": last_character
    }
    return first_and_last
print(first_and_last("python"))
print(first_and_last(""))
print(first_and_last("a"))


def cleanUsername(value):
    stripped_value = value.strip()
    lowered_value = stripped_value.lower()
    underscores_added = lowered_value.replace(" ", "_")
    return underscores_added
print(cleanUsername("  Reggie Gold   "))



def str_len(value):
    count = 0
    for char in value:
        count += 1
    return count
print(str_len("regina"))
print(str_len("regina is a girl"))
print(str_len(""))


def reverse_string(value):
    reversed_string = ""
    for char in value:
        add_character = char + reversed_string 
        reversed_string = add_character
    return reversed_string
print(reverse_string("cat"))
print(reverse_string("a"))


def censor_words(text, banned_word):
    replaced_text = text.replace(banned_word, "***")
    return replaced_text
print(censor_words("Goddey is a bad boy", "bad"))
print(censor_words("Goddey is a Bad boy", "bad"))
print(censor_words("bad bad bad", "bad"))

def solution(celsius):
    converted_celsius = float(celsius)
    fahrenheit = (converted_celsius * 9 / 5) + 32
    rounded_fahrenheit = round(fahrenheit, 2)
    return rounded_fahrenheit
print(solution(25))


def solution(meters):
    converted_meters = float(meters)
    centimeters = converted_meters * 100
    millimeters = converted_meters * 1000
    return f"Centimeters: {centimeters}\n" f"Millimeters: {millimeters}"
    
print(solution(3))

def solution(kilograms):
    converted_kilogram = float(kilograms)
    grams = converted_kilogram * 1000
    pounds = converted_kilogram * 2.20462
    rounded_pounds = round(pounds, 2)
    return f"Kilograms: {converted_kilogram}\n" f"Grams: {grams}\n" f"Pounds: {rounded_pounds}"
print(solution(5))


def solution(value):
    try:
        converted_value = float(value)
        doubled_number = converted_value * 2
        rounded = round(doubled_number, 2)
        return rounded
    except ValueError:
        return "Invalid number"
print(solution(3))


def arithmetic_engine(a, b):
    Sum = a + b
    product = a * b
    power = a ** b

    result = {
        "sum": Sum,
        "product": product,
        "power": power
    }
    return result 
print(arithmetic_engine(5, 5))

def division(a, b):
    true_division = round(a /b, 2)
    floor_division = a // b
    remainder = a % b

    result = {
        "true_division": true_division,
        "floor_division": floor_division,
        "remainder": remainder
    }
    return result
print(division(10, 3))

def eligibility_logic(score, attendance, completed_drill):
    if score >= 70 and attendance >= 80 and completed_drill is True:
        return "Eligible"
    else:
        return "Not eligible"
print(eligibility_logic(80, 90, False))

def safe_calculator(a, operator, b):
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        if b == 0:
            return "Cannot divide by zero"
        result = round((a / b), 2)
    elif operator == "%":
        if b == 0:
            return "Cannot divide by zero"
        result = a % b
    elif operator == "**":
        result = a ** b
    else:
        return "Invalid operator"
    return result
print(safe_calculator(10, "/", 0))
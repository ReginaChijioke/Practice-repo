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
        reversed_string.append(char)
    return reversed_string
print(reverse_string("cat"))

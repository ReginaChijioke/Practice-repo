def is_even(n):
    even = n % 2
    if even == 0:
        return True
    else:
        return False
print(is_even(81))
def make_profile(name, age=None, city="Unknown"):
    return f"{name} is {age} and she lives in {city}"
print(make_profile("Ada", 30, "Lagos"))
print(make_profile(name="Ada", age=30, city="Lagos"))
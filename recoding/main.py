def find_largest_number(numbers):

    if not numbers:
        return None
    
    highest = numbers[0]
    for number in numbers:
        if number > highest:
            highest = number
    return highest
print(find_largest_number([3, 41, 56, 21, 76, 9]))
print(find_largest_number([-10, -5, -2, -18]))
print(find_largest_number([]))



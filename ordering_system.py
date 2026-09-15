foods = ["jollof rice", "chicken", "plantain", "fish"]
prices = [2500, 3000, 1000, 3500]
total = 0
count = 0
ordered_food = None
ordered_price = None

system_prompt = input("what food do you want: ")
low_input = system_prompt.lower().strip()
for index, food in enumerate(foods):
    if food in low_input:
        ordered_food = food
        price = prices[index]
        ordered_price = price
        total = total + price
        count = count + 1


if count == 0:
    print("Sorry, that food is unavailable")
elif count == 1:
    print(f"{ordered_food} cost {ordered_price}")
else:
    print(f"your total cost is {total}")
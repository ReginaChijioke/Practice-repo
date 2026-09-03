ask = int(input("input first number: "))
ask2 = input("what operator: ")
operator = ["+", "-", "/", "*"]
if ask2 in operator:
    say = int(input("input second number: "))
else:
    print("Invalid OPerator")
if ask2 == operator[0]:
    print(ask + say)
elif ask2 == operator[1]:
    print(ask - say)
elif ask2 == operator[3]:
    print(ask * say)
elif ask2 == operator[2] and say == 0:
    print("Not divisible by zero")
elif ask2 == operator[2]:
    print(ask / say)


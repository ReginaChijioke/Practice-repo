def ticket_total(price, quantity):
    total = price * quantity
    print(total)
amount = ticket_total("7", 3)
print(amount)


#The * operator does string repetition because Python
#operators are overloaded — their behavior depends on 
#the type of the operands (str vs int), and Python defines str * int as "repeat".
#amount is None because the function never has an explicit return statement,
#so Python implicitly returns None when execution reaches the end 
#— printing inside the function has no effect on what gets handed back to the caller.

def ticket_total(price, quantity):
    total = price * quantity
    return total
amount = ticket_total(7, 3)
print(amount)
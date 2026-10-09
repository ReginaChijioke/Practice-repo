# B1
items = [2, 4, 6]
result = []

for item in items:
    if item % 4 == 0:
        continue
    result.append(item * 2)

print(result)


#B2
def borrow(resource):
    requested_quantity = input("input requested quantity: ")
    try:
        convert_quantity = int(requested_quantity)
    except ValueError:
        print("quantity must be an integer")
        return
    
    
    if convert_quantity <= 0:
        print("quantity must be greater than 0")
        return 
    if convert_quantity > resource["available"]:
        print("Not enough stock")
        return
    resource["available"] -= convert_quantity 
    return "Success"


transactions = [
    {"fellow": "Ada", "quantity": 2},
    {"fellow": "John", "quantity": 4},
    {"fellow": "Ada", "quantity": 3},
    {"fellow": "Grace", "quantity": 1},
    {"fellow": "John", "quantity": 2}
]


#B3
def calculate_totals(transactions):
    totals = {}
    for transaction in transactions:
        fellows = transaction["fellow"]
        transaction_quantity = transaction["quantity"]
        if fellows not in totals:
            totals[fellows] = 0
        totals[fellows] += transaction_quantity 
    return totals
calculate_totals()


#B4
def mutate_list():

    resources = [
        {"name": "Laptop", "available": 0},
        {"name": "Mouse", "available": 0},
        {"name": "Keyboard", "available": 3}
    ]
    available_resources = []
    for resource in resources:
        if resource["available"] > 0:
            available_resources.append(resource)
    return available_resources

    #B5
    """
    A race condition can occur when two fellows attempt to borrow resources simultaneously.
    To prevent this, I would use a lock to ensure that checking the available stock and updating the inventory happen as one protected operation. 
    The second fellow must wait until the first operation finishes, then check the updated stock. This prevents the system from approving requests when insufficient stock remains.
    """

    #B6
    """
    If my system needed to support 500 fellows, I would introduce a database to store fellows' details, resources, and borrowing records. Unlike an ordinary Python dictionary, a database can preserve information when the program closes. 
    It would also make managing and retrieving records easier as the system grows.
    """
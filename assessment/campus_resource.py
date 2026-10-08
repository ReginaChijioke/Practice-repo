resources = [
  {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
  {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
  {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]

fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
borrow_records = []

def find_resource(resource_id):
    for resource in resources:
        if resource["id"] == resource_id:
            return resource
    return None



def borrow_resource():
    fellow_id = input("input fellow id: ").upper()
    if fellow_id not in fellows:
            print("Fellow id not found")
            return
    
    resource_id = input("input resource id: ").upper()
    found_resource = find_resource(resource_id)
    if found_resource is None:
        print("Resource id not found")
        return

    quantity = input("input quantity: ")
    try:
        converted_quantity = int(quantity)
    except ValueError:
        print("Quantity must be a whole number.")
        return
    
    if converted_quantity <= 0:
        print("Quantity must be greater than 0")
        return

    available_resource = found_resource["available"]
    requested_quantity = converted_quantity
    if requested_quantity > available_resource:
        print("Not enough stock available")
        return
        
    found_resource["available"] = available_resource - requested_quantity
    for record in borrow_records:
        if record["fellow_id"] == fellow_id and record["resource_id"] == resource_id:
            record["quantity"] += requested_quantity
            print("Borrowed", requested_quantity, found_resource["name"])
            return
    borrow_records.append({
        "fellow_id": fellow_id,
        "resource_id": resource_id,
        "quantity": requested_quantity
    })
    print(f"You have successfully Borrowed {requested_quantity} {found_resource['name']}(s)")



def return_resource():
    fellow_id = input("input fellow id: ").upper()
    if fellow_id not in fellows:
            print("Fellow id not found")
            return
    
    resource_id = input("input resource id: ").upper()
    found_resource = find_resource(resource_id)
    if found_resource is None:
        print("Resource id not found")
        return
    
    return_quantity = input("input return quantity: ")
    try:
        converted_quantity = int(return_quantity)
    except ValueError:
        print("Quantity must be a whole number.")
        return

    if converted_quantity <= 0:
        print("Quantity must be greater than 0")
        return
        
    for record in borrow_records:
        if record["fellow_id"] == fellow_id and record["resource_id"] == resource_id:
            if converted_quantity > record["quantity"]:
                print("You cannot return more than you borrowed")
                return

            record["quantity"] -= converted_quantity 
            found_resource["available"] += converted_quantity
            print("Return successful")
            return
    print("This fellow has no loan for this resource")


def add_resource():
    resource_id = input("input resource id: ").upper()
    found_resource = find_resource(resource_id)
    if found_resource:
        print("Resource id already exists")
        return
    resource_name = input("input resource name: ") 
    resource_category = input("input resource category: ")
    total = input("input total units: ")
    try:
        total_units = int(total)
    except ValueError:
        print("total_units must be a whole number.")
        return

    if total_units <= 0:
        print("total_units must be greater than 0")
        return
    
    resource = {"id": resource_id, "name": resource_name, "category": resource_category, "total": total_units, "available": total_units}
    resources.append(resource)
    print("Resource successfully added.")


def list_resources():
    for resource in resources:
        print(f"{resource['id']} | {resource['name']} | {resource['category']} | {resource['total']} | {resource['available']}")
    return

def search_resources():
    search_name = input("input search term: ").lower()
    found = False
    for resource in resources:
        if search_name == resource["name"].lower():
            print(resource)
            found = True
    if found is False:
        print("no resources not found")
    
def filter_by_category():
    search_category = input("input search term: ").lower()
    found = False
    for resource in resources:
        if search_category == resource["category"].lower():
            print(resource)
            found = True
    if found is False:
        print("no resources not found in this category")

def generate_report():
    total_units = sum(resource["total"] for resource in resources)
    total_available = sum(resource["available"] for resource in resources)
    borrowed = total_units - total_available
    print(f"Total units: {total_units}")
    print(f"Available units: {total_available}")
    print(f"Borrowed units: {borrowed}")
    found = False
    for resource in resources:
        if resource["available"] < 3:
            print(resource)
            found = True
    if found is False:
        print("No low-stock resources")
    
    highest_borrowed = 0
    for resource in resources:
        borrowed_for_resources = resource["total"] - resource["available"]
        if borrowed_for_resources > highest_borrowed:
            highest_borrowed = borrowed_for_resources
    for resource in resources:
        borrowed_for_resources = resource["total"] - resource["available"]
        if borrowed_for_resources == highest_borrowed:
            print(resource)

running = True
while running:
    print("1. Add resource")
    print("2. List resources")
    print("3. Borrow resource")
    print("4. Return resource")
    print("5. Search resources")
    print("6. Filter by category")
    print("7. Generate report")
    print("8. Exit")
    user_choice = input("Enter your choice (1-8): ")
    if user_choice == "1":
        add_resource()
    elif user_choice == "2":
        list_resources()
    elif user_choice == "3":
        borrow_resource()
    elif user_choice == "4":
        return_resource()
    elif user_choice == "5":
        search_resources()
    elif user_choice == "6":
        filter_by_category()
    elif user_choice == "7":
        generate_report()
    elif user_choice == "8":
        running = False
        print("Goodbye")
    else:
        print("Invalid choice")
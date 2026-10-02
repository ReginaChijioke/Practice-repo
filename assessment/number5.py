def reserve_stock(stock, order):
    remaining =  stock.copy()
    for item, quantity in order:
        if quantity > stock[item]:
            raise ValueError("Insufficient stock")
            remaining[item] = stock[item] - quantity
    return remaining 

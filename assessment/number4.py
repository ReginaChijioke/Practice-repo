def summarise_amounts(raw_values):
    total = 0 
    rejected = 0
    for raw in raw_values:
        try:
            amount = int(raw)
            if amount >= 0:
                total += amount
            else:
                rejected += 1
        except ValueError:
            rejected += 1
    return {"total": total, "rejected": rejected}
print(summarise_amounts(["10", "5", "bad", "-3", "0", ""]))
inventory = {"apple": 5, "banana": 12, "orange": 0}

def get_stock(inventory, item):
    return inventory.get(item, 0)


def add_stock(inventory, item, amount):
    if item in inventory:
        total = inventory[item]
        inventory[item] = total + amount
    else:
        inventory[item] = amount


def in_stock_items(inventory):
    final = []
    for item in inventory:
        if inventory[item] > 0:
            final.append(item)
    return final



def total_items(inventory):
    total = 0
    for item in inventory:
        total = total + inventory[item]
    return total

print(get_stock(inventory, "banana"))   # 12
print(get_stock(inventory, "grape"))    # 0
add_stock(inventory, "apple", 3)
add_stock(inventory, "grape", 7)
print(inventory)                        # {'apple': 8, 'banana': 12, 'orange': 0, 'grape': 7}
print(in_stock_items(inventory))        # ['apple', 'banana', 'grape']
print(total_items(inventory))           # 27


votes = ["pizza", "tacos", "pizza", "sushi", "tacos", "pizza"]

def count_votes(votes):
    total = {}
    
    for i in votes:
        if i in total:
            total[i] += 1 
        else:
            total[i] = 1
    return total

print(count_votes(votes))
counts = count_votes(votes)

def winners(counts):
    if len(counts) == 0:
        return []

    best_count = 0
    for name in counts:
        if counts[name] > best_count:
            best_count = counts[name]

    top = []
    for name in counts:
        if counts[name] == best_count:
            top.append(name)
    return top


print(winners(counts))
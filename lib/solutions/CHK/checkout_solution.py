

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # items = ["A", "B", "C", "D"]
    # total = 0
    
    # for item in skus:
    #     if item not in items:
    #         return -1
    
    # for item in items:
    #     count = skus.count(item)
    #     if item == "A":
    #         if (count - count % 3) % 3 == 0:
    #             total += (count // 3) * 130
    #         total += (count % 3) * 50
        
    #     if item == "B":
    #         if (count - count % 2) % 2 == 0:
    #             total += (count // 2) * 45
    #         total += (count % 2) * 30

    #     if item == "C":
    #         total += count * 20

    #     if item == "D":
    #         total += count * 15

    # return total

    items = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
    total = 0

    for item in skus:
        if item not in items.keys():
            return -1
    
    for key in items.keys():
        items[key] = skus.count(key)

    if (items["F"] - items["F"] % 2) % 2 == 0:
        items["F"] -= items["F"] // 2

    if (items["E"] - items["E"] % 2) % 2 == 0 and items["B"] >= 1:
        items["B"] -= items["E"] // 2

    if items["A"] >= 5:
        total += (items["A"] // 5) * 200
        items["A"] = items["A"] % 5

    if items["A"] >= 3:
        total += (items["A"] // 3) * 130
        items["A"] = items["A"] % 3
    
    total += items["A"] * 50

    if items["B"] >= 2:
        total += (items["B"] // 2) * 45
        items["B"] = items["B"] % 2
    
    total += items["B"] * 30

    total += items["C"] * 20

    total += items["D"] * 15

    total += items["E"] * 40

    total += items["F"] * 10

    return total
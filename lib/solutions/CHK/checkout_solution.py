

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items = {
        "A": {"count": 0, "value": 50}, "B": {"count": 0, "value": 30}, 
        "C": {"count": 0, "value": 20}, "D": {"count": 0, "value": 15}, 
        "E": {"count": 0, "value": 40}, "F": {"count": 0, "value": 10},
        "G": {"count": 0, "value": 20}, "H": {"count": 0, "value": 10},
        "I": {"count": 0, "value": 35}, "J": {"count": 0, "value": 60},
        "K": {"count": 0, "value": 80}, "L": {"count": 0, "value": 90},
        "M": {"count": 0, "value": 15}, "N": {"count": 0, "value": 40},
        "O": {"count": 0, "value": 10}, "P": {"count": 0, "value": 50},
        "Q": {"count": 0, "value": 30}, "R": {"count": 0, "value": 50},
        "S": {"count": 0, "value": 30}, "T": {"count": 0, "value": 20},
        "U": {"count": 0, "value": 40}, "V": {"count": 0, "value": 50},
        "W": {"count": 0, "value": 20}, "X": {"count": 0, "value": 90},
        "Y": {"count": 0, "value": 10}, "Z": {"count": 0, "value": 50},
        }
    
    total = 0

    for item in skus:
        if item not in items.keys():
            return -1
    
    for key in items.keys():
        items[key] = skus.count(key)

    if (items["F"] - items["F"] % 2) % 2 == 0 and items["F"] >= 2:
        if items["F"] % 2 == 0:
            items["F"] -= (items["F"] // 2)-1
        else:
            items["F"] -= items["F"] // 2

    if (items["U"] - items["U"] % 3) % 3 == 0 and items["U"] >= 3:
        if items["U"] % 3 == 0:
            items["U"] -= (items["U"] // 3)-1
        else:
            items["U"] -= items["U"] // 3

    if (items["E"] - items["E"] % 2) % 2 == 0 and items["B"] >= 1:
        items["B"] -= items["E"] // 2

    if (items["N"] - items["N"] % 3) % 3 == 0 and items["M"] >= 1:
        items["M"] -= items["N"] // 3

    if (items["R"] - items["R"] % 3) % 3 == 0 and items["Q"] >= 1:
        items["Q"] -= items["R"] // 3

    if items["A"] >= 5:
        total += (items["A"] // 5) * 200
        items["A"] = items["A"] % 5

    if items["A"] >= 3:
        total += (items["A"] // 3) * 130
        items["A"] = items["A"] % 3

    if items["H"] >= 10:
        total += (items["H"] // 10) * 80
        items["H"] = items["H"] % 10

    if items["H"] >= 5:
        total += (items["H"] // 5) * 45
        items["H"] = items["H"] % 5

    if items["V"] >= 3:
        total += (items["V"] // 3) * 130
        items["V"] = items["V"] % 3

    if items["V"] >= 2:
        total += (items["V"] // 2) * 90
        items["V"] = items["V"] % 2

    if items["B"] >= 2:
        total += (items["B"] // 2) * 45
        items["B"] = items["B"] % 2

    if items["K"] >= 2:
        total += (items["K"] // 2) * 150
        items["K"] = items["K"] % 2

    if items["P"] >= 5:
        total += (items["P"] // 5) * 200
        items["P"] = items["P"] % 5

    if items["Q"] >= 3:
        total += (items["Q"] // 3) * 80
        items["Q"] = items["Q"] % 3

    for item in items.values():
        total += item["count"] * item["value"]

    return total

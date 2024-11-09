

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items = {
        "A": {"count": 0, "value": 50}, "B": {"count": 0, "value": 30}, 
        "C": {"count": 0, "value": 20}, "D": {"count": 0, "value": 15}, 
        "E": {"count": 0, "value": 40}, "F": {"count": 0, "value": 10},
        "G": {"count": 0, "value": 20}, "H": {"count": 0, "value": 10},
        "I": {"count": 0, "value": 35}, "J": {"count": 0, "value": 60},
        "K": {"count": 0, "value": 70}, "L": {"count": 0, "value": 90},
        "M": {"count": 0, "value": 15}, "N": {"count": 0, "value": 40},
        "O": {"count": 0, "value": 10}, "P": {"count": 0, "value": 50},
        "Q": {"count": 0, "value": 30}, "R": {"count": 0, "value": 50},
        "S": {"count": 0, "value": 20}, "T": {"count": 0, "value": 20},
        "U": {"count": 0, "value": 40}, "V": {"count": 0, "value": 50},
        "W": {"count": 0, "value": 20}, "X": {"count": 0, "value": 17},
        "Y": {"count": 0, "value": 20}, "Z": {"count": 0, "value": 21},
        }
    
    total = 0

    for item in skus:
        if item not in items.keys():
            return -1
    
    for key in items.keys():
        items[key]["count"] = skus.count(key)

    if (items["F"]["count"] - items["F"]["count"] % 2) % 2 == 0 and items["F"]["count"] >= 2:
        if items["F"]["count"] % 2 == 0:
            items["F"]["count"] -= (items["F"]["count"] // 2)-1
        else:
            items["F"]["count"] -= items["F"]["count"] // 2

    if (items["U"]["count"] - items["U"]["count"] % 3) % 3 == 0 and items["U"]["count"] >= 3:
        if items["U"]["count"] % 3 == 0:
            items["U"]["count"] -= (items["U"]["count"] // 3)-1
        else:
            items["U"]["count"] -= items["U"]["count"] // 3

    if (items["E"]["count"] - items["E"]["count"] % 2) % 2 == 0 and items["B"]["count"] >= 1:
        items["B"]["count"] -= items["E"]["count"] // 2

    if (items["N"]["count"] - items["N"]["count"] % 3) % 3 == 0 and items["M"]["count"] >= 1:
        items["M"]["count"] -= items["N"]["count"] // 3

    if (items["R"]["count"] - items["R"]["count"] % 3) % 3 == 0 and items["Q"]["count"] >= 1:
        items["Q"]["count"] -= items["R"]["count"] // 3

    if items["A"]["count"] >= 5:
        total += (items["A"]["count"] // 5) * 200
        items["A"]["count"] = items["A"]["count"] % 5

    if items["A"]["count"] >= 3:
        total += (items["A"]["count"] // 3) * 130
        items["A"]["count"] = items["A"]["count"] % 3

    if items["H"]["count"] >= 10:
        total += (items["H"]["count"] // 10) * 80
        items["H"]["count"] = items["H"]["count"] % 10

    if items["H"]["count"] >= 5:
        total += (items["H"]["count"] // 5) * 45
        items["H"]["count"] = items["H"]["count"] % 5

    if items["V"]["count"] >= 3:
        total += (items["V"]["count"] // 3) * 130
        items["V"]["count"] = items["V"]["count"] % 3

    if items["V"]["count"] >= 2:
        total += (items["V"]["count"] // 2) * 90
        items["V"]["count"] = items["V"]["count"] % 2

    if items["B"]["count"] >= 2:
        total += (items["B"]["count"] // 2) * 45
        items["B"]["count"] = items["B"]["count"] % 2

    if items["K"]["count"] >= 2:
        total += (items["K"]["count"] // 2) * 120
        items["K"]["count"] = items["K"]["count"] % 2

    if items["P"]["count"] >= 5:
        total += (items["P"]["count"] // 5) * 200
        items["P"]["count"] = items["P"]["count"] % 5

    if items["Q"]["count"] >= 3:
        total += (items["Q"]["count"] // 3) * 80
        items["Q"]["count"] = items["Q"]["count"] % 3

    bulkDiscount = items["S"]["count"] + items["T"]["count"] + items["X"]["count"] + items["Y"]["count"] + items["Z"]["count"]

    if bulkDiscount >= 3:
        total += (bulkDiscount // 3) * 45
        bulkDiscount -= bulkDiscount // 3

        if items["X"]["count"] != 0:
            if bulkDiscount > items["X"]["count"]:
                total += items["X"]["count"] * items["X"]["value"]
                bulkDiscount -= items["X"]["count"]
            else:
                total += bulkDiscount * items["X"]["value"]
        elif items["S"]["count"] != 0:
            if bulkDiscount > items["S"]["count"]:
                total += items["S"]["count"] * items["S"]["value"]
                bulkDiscount -= items["S"]["count"]
            else:
                total += bulkDiscount * items["S"]["value"]
        elif items["T"]["count"] != 0:
            if bulkDiscount > items["T"]["count"]:
                total += items["T"]["count"] * items["T"]["value"]
                bulkDiscount -= items["T"]["count"]
            else:
                total += bulkDiscount * items["T"]["value"]
        elif items["Y"]["count"] != 0:
            if bulkDiscount > items["Y"]["count"]:
                total += items["Y"]["count"] * items["Y"]["value"]
                bulkDiscount -= items["Y"]["count"]
            else:
                total += bulkDiscount * items["Y"]["value"]
        else:
            if bulkDiscount > items["Z"]["count"]:
                total += items["Z"]["count"] * items["Z"]["value"]
                bulkDiscount -= items["Z"]["count"]
            else:
                total += bulkDiscount * items["Z"]["value"]

        for item in ["S", "T", "X", "Y", "Z"]:
            items[item]["count"] = 0

    for item in items.values():
        total += item["count"] * item["value"]

    return total
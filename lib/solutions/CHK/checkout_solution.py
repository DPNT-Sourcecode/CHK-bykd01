

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items = ["A", "B", "C", "D"]
    total = 0
    
    for item in skus:
        if item not in items:
            return -1
    
    for item in items:
        count = skus.count(item)
        if item == "A":
            if (count - count % 3) % 3 == 0:
                total += (count // 3) * 130
            total += (count % 3) * 50
        
        if item == "B":
            if (count - count % 2) % 2 == 0:
                total += (count // 2) * 45
            total += (count % 2) * 30

        if item == "C":
            total += count * 20

        if item == "D":
            total += count * 15

    return total
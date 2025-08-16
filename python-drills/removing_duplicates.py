# removes duplicates in a list

list = ["blue","red","black","red","yellow"]
items = []

for item in list:
    if item not in items:
        items.append(item)

print(items)
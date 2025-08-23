shopping_list = {"price": "item",
                 4.90: "apples",
                 5.69: "milk",
                 7.00: "waffle mix",
                 3.40: "butter",
                 8.50: "bread" }
inverted_list = {v:k for k,v in shopping_list.items()}
'''
from collections import defaultdict # for dicts with duplicate items
inverted_grouped = defaultdict(list)
for k, v in shopping_list.items():
    inverted_grouped[v].append(k)
'''
print(inverted_list)
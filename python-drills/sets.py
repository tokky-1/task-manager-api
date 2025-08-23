set1 = {'1','3', '4','5', '10'}
set2 = {'2','4', '6 ','8', '10'}
common =[]
for a in set1:
    for b in set2:
        if a ==b :
            common.append(a)
print (f"{common} is in both sets")


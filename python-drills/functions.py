# def prime(num):
#     count = 0
    
#     for x in range(1,num+1):
#         value = num % x
#         if value == 0:
#             count += 1
#     if count == 2:
#         print("its prime")
#     else:
#         print("its not")
#     print (count)

# prime(6)

vowels = ("a","e","i","o","u")
def count_vowels(string):
    count = 0
    for item in list(string):
        if item in vowels:
            count += 1
    print(f"they are {count} vowels")


string = str(input("Enter a random statement:"))
count_vowels(string.lower())


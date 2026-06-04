lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

lst2 = []

for items in lst1:
    if type(items) == str:
        lst2.append(items)
        print(f"Item: {items} | Type: {type(items)}" )
        
print(lst2)
    
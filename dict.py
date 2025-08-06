names = ['jim', 'john', 'jane','monica', 'ali', 'susan', 'robert']
people= {
    'jim': {'age':30, 'height':180, 'weight':70},
    'john': {'age':20, 'height':170, 'weight':60},
    'jane': {'age':25, 'height':160, 'weight':50},
    'ali': {'age':35, 'height':190, 'weight':80},
    'susan': {'age':30, 'height':175, 'weight':65}
    }

print("\n---------------------------------")
print("|", end='')
print('name', end="\t|")
print('age', end="\t|")
print('height', end="\t|")
print('weight', end="\t|")
print("\n---------------------------------")
for name in names:
    if name in people:
        print("|", end='')
        print(name, end="\t|")
        print(people[name]['age'], end="\t|")
        print(people[name]['height'], end="\t|")
        print(people[name]['weight'], end="\t|")
        print("\n---------------------------------")
    '''else:
        print(f'no data was found for {name}')
'''



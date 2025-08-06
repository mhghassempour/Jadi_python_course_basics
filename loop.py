people = {
    'john' : ('20', 'john@gmail.com'),
    'jane' : ('18', 'jane@gmail.com'),
    'jim' : ('45', 'jim@gmail.com'),
    'jill' : ('56', 'jill@gmail.com'),
    'joe' : ('30', 'joe@gmail.com'),
}

for person in people.keys():
    print(person)

for person in people.values():
    print(person)

for person, data in people.items():
    print(person, data)
    

for person, data in people.items():
    print(f"{person} is {data[0]} years old and can be contacted at {data[1]}")



a = [3, 4, 5.1, 6.9, 7, 12]
tavan = list(map(lambda x:x**2 , a))
print (tavan)

ashari = list(filter(lambda x: x != int(x), a))
print(ashari)


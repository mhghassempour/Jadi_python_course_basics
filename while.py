'''
for i in range(1,11):
    for j in range(1,11):
        print(i*j, end="\t|")
    print()
'''

list = [x if x%7!=0 else "hob" for x in range(1 , 22)]
print(list)

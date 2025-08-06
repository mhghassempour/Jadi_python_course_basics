def decorator(func):
    def wrapper():
        import datetime
        start = datetime.datetime.now()
        func()
        finish = datetime.datetime.now()
        print(finish - start)
    return wrapper

@decorator
def list_maker():
    n = int(input('insert length of the list: '))
    list = []
    for i in range(n):
        list.append(i+1)
    print(list)

list_maker()


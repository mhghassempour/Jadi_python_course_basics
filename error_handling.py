def divis(a, b):
    try:
        # try this
        r = a / b
    except Exception as e:
        # exception in case of an error
        print(f'error: {e}')

    else:
        # will run if no exception happened
        print(r)


divis(1, 2)
divis(1, 0)
divis(1, 'a')

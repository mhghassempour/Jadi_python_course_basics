def skylines(*args):
    tallest = 0
    for i in args:
        if i > tallest:
            tallest = i
    return tallest

tallest_building = skylines (1, 5, 17, 15, 2, 3, 10)

print(f"tallest building is {tallest_building}00 meters high")
import itertools as it

nums = [1,2,3,4]
combo = it.combinations(nums, 2)
combo_with_replacement = it.combinations(nums, 2)

print(list(combo))

numbers = [1, 2, 3]
result = list(it.combinations(numbers, 2))
print(result)
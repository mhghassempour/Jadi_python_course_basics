def is_even(n):
    return n%2 == 0


def count_evens(nums):
  
    count = 0
    for n in nums:
        if is_even (n):
            count += 1
    return count


list_of_numbers = [12 , 10, 1, 2, 58, 7, 9]
print(count_evens(list_of_numbers))
 


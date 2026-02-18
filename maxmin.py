def highest_and_lowest(numbers):

    numbers.sort()

    return [numbers[0], numbers[-1]]


min_max = highest_and_lowest([2, 4, 1, 0, 2, -1])
print(min_max)

def binary_search(array: list[int], target: int):
    low = 0
    high = len(array) - 1
    while (low <= high):
        midpoint = (low + high) // 2
        mid_val = array[midpoint]

        if (mid_val == target):
            return midpoint
        elif (target > midpoint):
            low = midpoint + 1
        else:
            high = midpoint - 1

    return -1


print(binary_search([2, 4, 6, 8, 20], 8))
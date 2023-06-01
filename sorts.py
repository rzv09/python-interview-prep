
# Intuition: at each iteration, the biggest element
# bubbles to the end of the list
def bubble_sort(array: list[int]):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]



def selection_sort(array: list[int]):
    for i in range(len(array)):
        lowest_num_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[lowest_num_index]:
                lowest_num_index = j
        if (lowest_num_index != i):
            array[i], array[lowest_num_index] = array[lowest_num_index], array[i]

data=[2, 6, 1, 0, 2, 4]

print("")
print("Data array: ", data)

print("")
selection_sort(data)

print("Executing selection sort result:", data)

data=[2, 6, 1, 0, 2, 4]

print("")
bubble_sort(data)

print("Executing bubble sort result:", data)
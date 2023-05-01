
# Intuition: at each iteration, the biggest element
# bubbles to the end of the list
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


data=[2, 6, 1, 0, 2, 4]
bubble_sort(data)
print(data)

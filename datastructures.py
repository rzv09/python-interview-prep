# data structures go here

def list_methods():
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    print("There are " + str(fruits.count('apple')) + " apples")

    print("Index of banana:", fruits.index('banana'))

    print("Next banana starting at position 4:", fruits.index('banana', 4))

    fruits.reverse()
    fruits.append('grape')
    fruits.sort()
    fruits.pop()
    print(fruits)

list_methods()

def comprehensions():
    squares = [x**2 for x in range(10)]
    print(squares)

    combined_elements = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
    print(combined_elements)

    # for dictionaries
    my_dict = {x: x**2 for x in (2, 4, 6)}
    print(my_dict)

comprehensions()
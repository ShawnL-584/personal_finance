import shelve

integers1 = [1, 2, 3, 4, 5, 6]
integers2 = [9, 9, 9, 9, 9, 9]
integers3 = [100, 200, 300]


# with shelve.open('/Users/shawnlin/Documents/python/MyProject/udemy_python_all/ch5/shelve_ex', flag='c') as shelf:
#     shelf['ints1'] = integers1
#     shelf['ints2'] = integers2
#     shelf['ints3'] = integers3

with shelve.open('/Users/shawnlin/Documents/python/MyProject/udemy_python_all/ch5/shelve_ex', flag='r') as shelf:
    for key in shelf.keys():
        print(key)
    print(shelf['ints2'])

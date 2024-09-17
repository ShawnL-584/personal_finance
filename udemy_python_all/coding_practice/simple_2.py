#  ----------------1
# def stars(num):
#     for n in range(1, num+1):
#         print('*'*n)


# stars(1)
# print('-----')
# stars(4)

#  ----------------2
# def stars2(num):
#     for n in range(1, num+1):
#         print('*' * n)
#     for m in range(num-1, 0, -1):
#         print('*' * m)

# stars2(1)
# print('-----')
# stars2(3)
# print('-----')
# stars2(4)
# print('-----')
#  ----------------3
# def table1(num):
#     for n in range(1, 10):
#         print(f'{num} x {n} = {num *n}')

# table1(3)
# table1(5)

#  ----------------4
# def table9to9():
#     for n in range(1, 10):
#         for m in range(1, 10):
#             print(f'{n} x {m} = {m *n}')


# table9to9()

#  ----------------5
def swap(str1):
    new_str = ''
    for n in str1:
        if n == n.upper():
            new_str += n.lower()
        else:
            new_str += n.upper()
    return new_str


print(swap('Aloha'))
print(swap('Love you.'))
#  ----------------6


def findMin(list1):
    if list1 == []:
        return 'undefined'
    result = list1[0]
    for n in list1:
        if n < result:
            result = n
    return result


print(findMin([1, 2, 5, 6, 99, 4, 5]))  # returns 1
print(findMin([]))  # returns undefined
print(findMin([1, 6, 0, 33, 44, 88, -10]))  # returns -10

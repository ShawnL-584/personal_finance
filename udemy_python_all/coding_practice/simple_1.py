#  ----------------1
# def printMany():
#     for n in range(1, 101):
#         print(n)


# printMany()
# -----------------2
# def printEvery3():
#     for n in range(1, 90, 3):
#         print(n)


# printEvery3()

# -----------------3
# def position(str1):
#     for num, c in enumerate(str1):
#         if c == c.upper():
#             return (c, num)
#     return -1


# print(position('abcd'))
# print(position('Abcd'))
# print(position('abCD'))

# # -----------------3-1


# def backPosition(str1):
#     final = -1
#     for num, c in enumerate(str1):
#         if c == c.upper():
#             final = (c, num)
#     return final


# print(backPosition('abcd'))
# print(backPosition('Abcd'))
# print(backPosition('abCD'))

# -----------------4
# def findSmallCount(list1, num):
#     count = 0
#     for n in list1:
#         if n < num:
#             count += 1
#     return count


# print(findSmallCount([1, 2, 3], 2))  # returns 1
# print(findSmallCount([1, 2, 3, 4, 5], 0))  # returns 0
# print(findSmallCount([1, 2, 3, 4, 5], 100))  # returns 5

# -----------------5
# def findSmallerTotal(list1, num):
#     sum = 0
#     for n in list1:
#         if n < num:
#             sum += n
#     return sum

# print(findSmallerTotal([1, 2, 3], 3))  # returns 3
# print(findSmallerTotal([1, 2, 3], 1))  # returns 0
# print(findSmallerTotal([3, 2, 5, 8, 7], 999))  # returns 25
# print(findSmallerTotal([3, 2, 5, 8, 7], 0))  # returns 0

# -----------------6
# def findAllSmall(list1, num):
#     return [n for n in list1 if n < num]


# print(findAllSmall([1, 2, 3], 10))  # returns [1, 2, 3]
# print(findAllSmall([1, 2, 3], 2))  # returns [1]
# print(findAllSmall([1, 3, 5, 4, 2], 4))  # returns [1, 3, 2]

# -----------------7
def summ(list1):
    sum = 0
    for n in list1:
        sum += n
    return sum


print(summ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # returns 55
print(summ([]))  # return 0
print(summ([-10, -20, -30]))  # return -60

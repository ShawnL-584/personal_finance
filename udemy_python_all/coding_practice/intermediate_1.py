# -----------------1
# def mySort(list1):
#     list1.sort()
#     return list1


# print(mySort([17, 0, -3, 2, 1, 0.5]))  # returns [-3, 0, 0.5, 1, 2, 17]

# -----------------2
# def isPrime(num):
#     if num == 1:
#         return False
#     for n in range(2, int(num/2)):
#         if num % n == 0:
#             return False
#     return True


# print(isPrime(1))  # returns false
# print(isPrime(5))  # returns true
# print(isPrime(91))  # returns false
# print(isPrime(1000000))  # returns false


# -----------------3
# def palindrome(str1):
#     return str1 == str1[::-1]


# print(palindrome("bearaeb"))  # true
# print(palindrome("Whatever revetahW"))  # true
# print(palindrome("Aloha, how are you today?"))  # false

# -----------------4
# def pyramid(num):
#     for n in range(1, num+1):
#         print(' ' * (num - n) + '*' * (2*n-1))


# pyramid(10)
# print('---------')


# -----------------5
# def inversePyramid(num):
#     for n in range(num, 0, -1):
#         print(' ' * (num-n) + '*' * (2*n-1))


# inversePyramid(4)
# print('---------')
# inversePyramid(3)
# print('---------')
# inversePyramid(2)
# print('---------')

# -----------------6
# def has_33(list1):
#     for n in range(len(list1)-1):
#         if (list1[n] == 3) and (list1[n+1] == 3):
#             return True
#     return False


# print(has_33([1, 2, 3, 4, 5, 3, 3]))
# print(has_33([]))
# print(has_33([4, 3, 4, 5, 2, 1]))
# -----------------7
# def spyGame(list1):
#     check = [0, 0, 7]
#     for n in list1:
#         if check[0] == n:
#             check.pop(0)
#         if not check:
#             return True
#     return False


# print(spyGame([1, 2, 4, 0, 3, 0, 7]))  # True
# print(spyGame([1, 2, 5, 0, 3, 1, 7]))  # False

# ----------7 another solution
def spy_game(list1):
    str1 = '007'
    pointer_str = 0
    pointer_list = 0
    while pointer_list < len(list1):
        if list1[pointer_list] == int(str1[pointer_str]):
            pointer_str += 1
            if len(str1) == pointer_str:
                return True
        pointer_list += 1
    return False


print(spy_game([1, 2, 4, 0, 3, 0, 7]))  # True
print(spy_game([1, 2, 5, 0, 3, 1, 7]))  # False
print(spy_game([1, 2, 0, 0, 3, 0, 3, 6, 7, 7]))  # True

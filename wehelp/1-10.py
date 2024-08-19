#wehelp coding #1 檢查字串是否https://開頭

"""
    @param s:{String}
    @return :{Boolean}
"""
def checkHTTPS(s):
    if   s.lower().startswith('https://') :
        return True
    else :
        return False

#----------------------------------------------
#wehelp coding #2 檢查輸入的領取金額是否合乎規範

"""
檢查輸入的領取金額是否合乎規範
輸入一個正整數代表想要從 ATM 機領取的金額，你的函式能檢查輸入的金額是否合乎以下規範：

輸入的金額必須是 100 的倍數。
輸入的金額必須大於等於 100。
輸入的金額必須小於等於 100000。
若輸入的金額符合規範，回傳真值，不符合規範，則回傳假值。

    @param n:{Integer}
    @return :{Boolean}
"""
def checkMoney(n):
    # 你的程式碼
    if (n % 100 == 0) and (n < 100000):
        return True
    else:
        return False

#----------------------------------------------
#wehelp coding #3 找到最大的整數

"""
找到最大的整數
輸入包含至少一個整數的陣列 / 列表，找到並回傳其中最大的整數。

輸入範例一：[1, 3, 3, 2, 5, -2]
回傳：5

輸入範例二：[-5, -10, -8, -1, -2]
回傳：-1

輸入範例一：[0, 2, 2]
回傳：2

    @param nums:{[Integer]}
    @return :{Integer}
"""
def findMax(nums):
    # 你的程式碼
    max_num = sorted(nums)[-1]
    return   max_num

#----------------------------------------------
#wehelp coding #4 找到第二大的整數
"""
輸入包含至少兩個不同整數的陣列 / 列表，找到並回傳其中第二大的整數。

輸入範例一：[1, 3, 3, 2, 5, -2]
回傳：3

輸入範例二：[-5, -10, -8, 1, -1]
回傳：-1

輸入範例一：[0, 2]
回傳：0

    @param nums:{[Integer]}
    @return :{Integer}
"""

def findSecond(nums):
    # 你的程式碼
    max_num_2 = sorted(set(nums))[-2]
    return max_num_2

#----------------------------------------------
#wehelp coding #5 找到最大公因數
'''

輸入兩個正整數，你的函式能找到並回傳這兩個正整數的最大公因數。
輸入範例一：6 和 4
回傳：2
輸入範例二：5 和 16
回傳：1
輸入範例一：12 和 6
回傳：6

    @param n1:{Integer}
    @param n2:{Integer}
    @return :{Boolean} 
'''
# way 1
def findGCD(n1, n2):
    # 你的程式碼
    g = 0
    if n1 > n2 :
        g = n1
    else:
        g = n2
    for n in range(g,0,-1):
        if n1 % n == 0 and n2 % n == 0:
            return n
#  way 2 chatgpt
# import math
# def findGCD(n1, n2):
#     return math.gcd(n1,n2)
# way 3 chatgpt
# def findGCD(n1, n2):
#     while n2 != 0:
#         n1, n2 = n2, n1 % n2
#     return n1
#----------------------------------------------
#wehelp coding #6 找到最小公倍數
def findLCM(n1, n2):
    # 你的程式碼
    og_n1 ,og_n2 =n1, n2
    while n2 != 0:
        n1 , n2 = n2, n1%n2
    gcd = n1
    LCM = og_n1 * og_n2 // gcd
    return (LCM)


#----------------------------------------------
#wehelp coding #7 將整數陣列 / 列表，轉換為逗號隔開的字串
def toCSVString(nums):
    # 你的程式碼
    num_str = ','.join(map(str,nums))
    return num_str

# list1 = [3, 5, -4, 2]
# list3 = []
# list2 = [1000]
# print(toCSVString(list1))
# print(toCSVString(list2))
# print(repr(toCSVString(list3)))

#wehelp coding #8 將整數陣列 / 列表，轉換為逗號隔開的字串

def sumOfArithmeticSequence(min, max, differ):
    # 你的程式碼
    # sum_num = 0
    # for n in range(min, max+1, differ):
    #     sum_num += n
    # return sum_num
    #
    sum_num = 0
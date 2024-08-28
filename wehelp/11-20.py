#wehelp coding #11 找到目標數字所在的索引位置

def findIndex(nums, target):
    for n in range(len(nums)):
        if nums[n] == target :
            return n
    else:
        return -1

# result1 = [3, 2, 1, 5, 10]
# result2 = [5, 2, 3]
# result3 = [-5, 2, -5, 1, 3]
#
# print(findIndex(result1,1))
# print(findIndex(result2,4))
# print(findIndex(result3,-5))


#wehelp coding #12 找到目標數字所在的多個索引位置
def findIndexes(nums, target):
    # list1 = []
    # for n in range(len(nums)):
    #     if nums[n] == target:
    #         list1.append(n)
    # return list1
    list1 = [n for n in range(len(nums)) if nums[n] == target]
    return list1

# result1=[3, 2, 1, 5, 10]
# result2=[5, 2, 3]
# result3=[-5, 2, -5, 1, -5]
#
# print(findIndexes(result1,1))
# print(findIndexes(result2,4))
# print(findIndexes(result3,-5))

#wehelp coding #13 輸入一個字串，你的函式能夠翻轉這個字串。

def reverseString(s):
    # 你的程式碼
    return s[::-1]

#wehelp coding #14 整數陣列 / 列表中，兩兩相乘的最大值
def findMaxProduct(nums):
    sort_nums = sorted(nums)
    return max(sort_nums[0]*sort_nums[1],sort_nums[-1]*sort_nums[-2])

list1 = [2, -1, 0]
list2 = [-2, -10, 1, 2]
list3 = [3, 1, 9, 4, 5]

print(findMaxProduct(list1))
print(findMaxProduct(list2))
print(findMaxProduct(list3))

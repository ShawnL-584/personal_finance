# -----------------1
def factorPrime(num):
    factors = []
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        divisor += 1
    return ' x '.join(map(str, factors))


def factorPrime2(num):
    ans = str(num) + ' = '
    p = 2
    while p <= num:
        if num % p == 0:
            ans += str(p) + ' x '
            num /= p
        else:
            p += 1
    return ans[:-3]


# print(factorPrime(120))
print(factorPrime2(10001))
# -----------------2


def intersection(list1, list2):
    inter_list = [n for m in list1 for n in list2 if m == n]
    print(inter_list)
    return inter_list


def my_intersection(lst1, lst2):
    return list(set(lst1).intersection(set(lst2)))


# intersection([5, 1, 3, 4, 6, 10], [5, 11, 4, 3, 100, 144, 0])  # returns [3, 4]
print(my_intersection([1, 3, 4, 6, 10],
                      [11, 4, 3, 100, 144, 0]))  # returns [3, 4]

# -----------------3


def flatten(list1):
    flat_list = []
    for item in list1:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)

    return flat_list


result = []


def flatter(list1):
    for n in list1:
        if isinstance(n, list):
            flatter(n)
        else:
            result.append(n)
    return result


print(flatten([1, [[], 2, [0, [1]], [3]], [1, 3, [3], [4, [1]], [2]]]))
print(flatter([1, [[], 2, [0, [1]], [3]], [1, 3, [3], [4, [1]], [2]]]))

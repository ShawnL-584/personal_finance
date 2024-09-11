from copy import deepcopy
a = ([1, 2, 3], 5, 6, 7)
b = [1, 2, 3]
c = b.copy()
d = deepcopy(a)

c[0] = 10000
d[0][0] = 999
print(a)
print(b)
print(c)
print(d)
# ([1, 2, 3], 5, 6, 7)
# [1, 2, 3]
# [10000, 2, 3]
# ([999, 2, 3], 5, 6, 7)
a = {1, 6, 5}
b = {3, 4, 7, 8}
c = {3, 4}
print(a.isdisjoint(b))
print(b.issubset(c))
print(b.issuperset(c))
print(c.issubset(b))
print(c.issuperset(b))

# {1, 5}
# {8, 7}
# {3, 4}
# {3, 4}
# {1, 3, 4, 5, 7, 8}
# {1, 3, 4, 5, 7, 8}

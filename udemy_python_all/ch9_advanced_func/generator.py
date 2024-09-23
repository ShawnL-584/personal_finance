# def cube(num):
#     result = [n ** 3 for n in range(num)]
#     return result
#
#
# print(cube(10))


def cube(num):
    for x in range(num):
        yield x ** 3


print(cube(10))

for n in cube(10):
    print(n)

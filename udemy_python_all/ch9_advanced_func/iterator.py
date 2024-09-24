# iterable is a subset of iterable

x = [1, 2, 3]
print(dir(x))  # list is not iterator
# __iter__() returns a iterator
print(dir(iter(x)))

list_iterator = iter(x)
print(next(list_iterator))
print(next(list_iterator))
print(next(list_iterator))

# 上面這幾行跟下面做的事情一樣
for n in x:
    print(n)

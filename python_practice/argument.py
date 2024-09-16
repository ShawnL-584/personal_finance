# 1. normal argument
# 2. default argument
# 3. *args
# 4. kwargs

def myfunc(p1, p2, p3='Three', *args, **kwargs):
    print('-----------------------')
    print(p1, p2, p3, args, kwargs)


myfunc(1, 2, 3, 4, 5, x=1, y=3)
myfunc(1, 2, 3, 4, x=4)
myfunc(1, 2, 3, 4)
myfunc(1, 2, 3)
myfunc(1, 2)
# -----------------------
# 1 2 3 (4, 5) {'x': 1, 'y': 3}
# -----------------------
# 1 2 3 (4,) {'x': 4}
# -----------------------
# 1 2 3 (4,) {}
# -----------------------
# 1 2 3 () {}
# -----------------------
# 1 2 Three () {}

# myfunc(1)
# 這行會出錯因為argument不夠

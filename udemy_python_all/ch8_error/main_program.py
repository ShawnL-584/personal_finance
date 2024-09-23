import something
try:
    num = 50
    something.enter_age(num)
except something.NegativeNumberException as error:
    print(error)

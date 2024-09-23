import pickle
# import os
# os.chdir('/Users/shawnlin/Documents/python/MyProject/udemy_python_all/ch5')
# print(os.getcwd())

x = 100
y = [6, 6, 9, 9]

# pickle wb
# with open('/Users/shawnlin/Documents/python/MyProject/udemy_python_all/ch5/pickle_file', mode='wb') as p_file:
#     pickle.dump(x, p_file)
#     pickle.dump(y, p_file)

# pickle rb
with open('/Users/shawnlin/Documents/python/MyProject/udemy_python_all/ch5/pickle_file', mode='rb') as p_file:
    a1 = pickle.load(p_file)
    a2 = pickle.load(p_file)
    print(a1, type(a1))
    print(a2, type(a2))

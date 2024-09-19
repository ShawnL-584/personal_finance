import pickle
x = None
y = None
my_list = None


def restore_data():
    global x, y, my_list

    with open('/Users/shawnlin/Documents/python/MyProject/udemy_python_all/ch5/pickle_file2', mode='rb') as pfile:
        data = pickle.load(pfile)
        x = data['x']
        y = data['y']
        my_list = data['my_list']


restore_data()
print(x, y, my_list)

# x = 10
# y = 99
# my_list = [7, 8, 9, 0]
# def save_data():
#     global x, y, my_list
#     data = {'x': x, 'y': y, 'my_list': my_list}

#     with open('/Users/shawnlin/Documents/python/MyProject/udemy_python_all/ch5/pickle_file2', mode='wb') as pfile:
#         pickle.dump(data, pfile)


# save_data()

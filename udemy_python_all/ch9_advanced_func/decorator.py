def new_decorator(original_func):
    def wrap_func():
        print('Codes before og func')
        original_func()
        print('Codes after original func')

    return wrap_func


@new_decorator
def func_needs_decor():
    print('I am a function needs decorator.')


func_needs_decor()

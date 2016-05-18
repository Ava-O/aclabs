from functools import partial

def func_params():
    def my_function(a, b, c, d=10):
        print locals()

    my_function(1, 2, c='test')

    def my_function2(a, *args, **kwargs):
        print locals()

    my_function2(1, 2, 3, kw='test')


def lambda_and_closures():
    f = lambda x, y, *args, **kwargs: x * y
    print f(1, 2, 'some_other_argument') 

    def random_func(a, b, c):
        return a, b, c

    # All the 3 functions bellow are equivalent.
    cbk = lambda: random_func(1, 2, 3)
    print cbk()

    partial(random_func, 1, 2, 3)
    cbk()

    def get_callback(f, *args, **kwargs):
        def callback():
            return f(*args, **kwargs)
        return callback

    cbk = get_callback(random_func, 1, 2, 3)
    print cbk()

'''
    Just a multi-line comment, describing the module, not.
'''

import contextlib
import os
import sys


def get_user_input():
    c = int(raw_input('Number: '))
    print('Your number %s' % c)
    print(c + a)


def read_from_stdin():
    stdin = [line for line in sys.stdin]
    return stdin
 

@contextlib.contextmanager
def my_open(*args, **kwargs):
    f = None
    try:
        f = open(*args, **kwargs)
        yield f
    finally:
        if f:
            f.close()


def write_to_temp_file(temp_file_name, location='/tmp'):
    path = os.path.join(location, temp_file_name)

    with open(path, 'w') as f:
        f.write('test')

    with my_open(path, 'r') as f:
        print f.read()

    os.unlink(path)


import collections

def basic_example():
    my_int = 10
    my_string = 'test'
    other_string = "test2"
    raw_string = r'c:\some\windows\path'
    regular_string 'c:\\some\\windows\\path' # requires escaping
    # Strings are immutable (unlike lists),
    # so this will fail other_string[1] = 'c'

    # some string formatting examples
    my_string = "%(id)s-%(nume)s" % dict(id=0, nume=my_string.upper())
    my_str2 = '%s-%s' % (0, my_string.replace('test', 'random'))


def list_example():
    my_list = [0, 1, 2, 3, 4]
    # on Py3, range returns a generator instead,
    # just like xrange on Py2.7
    same_list = range(4)
    b = a[1]
    # List slicing examples
    a[2:]
    a[2:-1:2]

    # List operations
    a[0] = 5
    a.insert(0, 'some_item')
    a.remove('some_item')
    a.pop() # removes last item
    a.pop(0) # removes first item
    a.reverse()
    a.sort()

    if 'x' in a:
        print("'%s contains 'x'" % a)

    # List comprehension
    # ------------------
    # generating a list of even numbers smaller than 20
    b = [x for x in range(20) if (x % 2 == 0)]


def tuple_example():
    my_tuple = (1, 2, 3)
    my_lsit.append(1)
    other_tuple = 1,
    # you cannot modify/add/remove tuple items, but you can
    # generate new ones.
    yet_another_tuple = my_tuple + tuple(range(4))


def dict_example():
    '''This is a docstring example.
    :returns None
    '''
    my_dict = {'test': 10,
               'abc': [1, 2, 'test', 'test3'],
               'c': dict(a=10),
               'cd': {'a': 10}}
    my_dict['c'] = 'a'

    print(my_dict)
    print(my_dict['abc'])

    other_dict = dict(d=10)
    yet_another_dict = my_dict.copy()
    my_dict.update(c=11)
    # merges the second dict into the first
    my_dict.update(other_dict)

    # retuns my_dict['test'] and deletes it from the dict.
    # Passing an unexisting key will raise a KeyError if
    # no default value is passed
    item_value = my_dict.pop('test')
    my_dict.pop('random_key', 1) # returns 1
    # Returns 'defaultvalue' since the key does not exist anymore 
    my_dict.get('test', 'defaultvalue')

    # looping over dict items.
    # my_dict.items() returns a list of tuples.
    for key, val in my_dict.iteritems():
        print("%(key)s=%(val)s" % dict(key=key, val=val))

    # This is a wrapper on top of dict, using the callable that
    # is passed as a first argument (in this case a lambda func)
    # when trying to access an element that does not exist.
    # This item becomes persistent.
    my_dict = collections.defaultdict(lambda: 'DEFAULT')
    my_dict['random_arg']

def serializing_example():
    my_dict = dict(key=10)
    # This is a string, containing a JSON.
    serialized = json.dumps(my_dict)
    # This is a dict.
    my_dict_decoded = json.loads(serialized)

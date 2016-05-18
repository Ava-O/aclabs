def loop_over_generator_example():
    # We set a breakpoint
    import pdb
    pdb.set_trace()

    for i in xrange(1000000):
        if not (i % 2 == 0):
            continue
        if (None or '' or 0 or False or {} or []):
            print 'found smth'
        print i
        if i in range(3):
            print '%s < 3' % i
        if i >= 5:
            break


def even_generator():
        i = 0
        while True:
            i += 2
            # do not confuse it with 'return'
            yield i


def other_generator_example():
    (x for x in xrange(1000000) if (x % 2 == 0)

    for i in even_generator():
        print i
        if i >= 10:
            break
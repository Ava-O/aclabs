import traceback


def func_raising_exception():
    raise Exception('expected exception')


def test_exc():
    try:
        func_raising_exception()
    except (Exception, IOError) as ex:
        traceback.print_stack()
        print(ex)
        # The traceback is printed but the exception
        # is not re-raised.
    except AttributeError as ex:
        print('Got attribute error: %s ' % ex)
        # This will re-raise the exception
        raise
    finally:
        print('test_exc finished')

from time import time


def performance_time(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        res = func(*args, **kwargs)
        t2 = time()
        print(f'This operation took {t2-t1} seconds to run')
        return res
    return wrapper

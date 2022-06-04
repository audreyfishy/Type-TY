import time

def printTime(func):
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        elapsed_time = time.time() - start
        print("{} seconds in {}".format(elapsed_time, func.__name__))
        return result
    return wrapper
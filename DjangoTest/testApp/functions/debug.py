import time
import sys

def test(*args, **kargs):
    if args:
        print(*args, file=sys.stderr)
    if kargs:
        print(kargs, file=sys.stderr)

def printTime(func):
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        elapsed_time = time.time() - start
        test("{} seconds in {}".format(elapsed_time, func.__name__))
        return result
    return wrapper
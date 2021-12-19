
import cProfile
import datetime
import io
import pstats
import threading
from functools import wraps

def print_to_file(message: str, filename: str = "profile.txt"):

    with open(filename, 'a') as f_file:
        f_file.write(message)


def profile(func):
    """
    A decorator that uses cProfile to profile a function
    :param func:
    :return:
    """

    @wraps(func)
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = func(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        # print(f'{func.__qualname__}.txt')
        now = datetime.datetime.now()
        thread1 = threading.Thread(target=print_to_file, args=[s.getvalue(), f'{func.__qualname__}{now.hour}{now.minute}{now.second}.txt'])
        thread1.start()
        #print(s.getvalue())
        return retval

    return inner
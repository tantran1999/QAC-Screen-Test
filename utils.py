import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[DEBUG] Function `{func.__name__}` elapsed time: {(end - start):0.10f} seconds")

        return result

    return wrapper_timer

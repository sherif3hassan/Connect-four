import time


def time_it(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()

    print(f"{func.__name__} took {(end - start) * 1000} mil sec")

    return result

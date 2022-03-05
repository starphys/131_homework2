import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        total = end - start
        print(f"Total time {round(total)}")

    return wrapper

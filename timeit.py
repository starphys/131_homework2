import time


def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        total = end - start
        print(f"Total time {total}")

    return wrapper

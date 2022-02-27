def doubler(func) :
    def wrapper(*args, **kwargs) :
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

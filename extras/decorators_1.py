import time
from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(
        filename=f'extras\{orig_func.__name__}.log', level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(f'Run with args {args} and kwargs: {kwargs}')
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{orig_func.__name__} ran in: {t2} sec')
        return result

    return wrapper


@my_logger
@my_timer
def display_info(name, age):
    print(f'display info ran with arguments ({name}, {age})')


@my_logger
@my_timer
def display_info_timer(name, age):
    time.sleep(3)
    print(f'display info ran with arguments ({name}, {age})')


#display_info('John', 25)
display_info_timer('Lucas', 36)

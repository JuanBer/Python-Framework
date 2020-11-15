def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'Wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)
    # return the function waiting for be executed
    return wrapper_function

class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f'Call method executed this before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)

@decorator_function
def display():
    print('display function ran')

@decorator_function
def display_info(name, age):
    print (f'display_info ran with arguments({name}, {age})')

@decorator_class
def display_class():
    print('display function ran - decorator class')

@decorator_class
def display_info_class(name, age):
    print (f'display_info ran with arguments({name}, {age}) - decorator class')

# decorated_display = decorator_function(display)
# decorated_display()
display()
display_info('Juan', 25)

display_class()
display_info_class('Jose', 30)
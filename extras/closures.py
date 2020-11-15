# def outer_func():
#     message = 'Hi'

#     def inner_func():
#         print(message)
    
#     return inner_func

def outer_func(msg):
    message = msg

    def inner_func():
        print(message)
    
    return inner_func


i_f = outer_func('Hi')
i_f_2 = outer_func('Hello')
print(i_f)
print(i_f.__name__)
# inner_funct still has acces to message variable
i_f()
i_f_2()
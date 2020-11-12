def square(x):
    return x * x


def cube(x):
    return x * x * x


f = square(5)
# use z as using square
z = square

# print(square)
# print(f)
# print(z)
# print(z(5))


def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


# l = [1, 2, 3, 4, 5, 6, 7]
# squares = my_map(square, l)
# cubes = my_map(cube, l)

# print(squares)
# print(cubes)

# returning a function
def logger(msg):

    def log_message():
        print('Log: ', msg)
    # it returs a function
    return log_message

# closure
# log_hi = logger("Hi")
# log_hi()


def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text


print_h1 = html_tag('h1')
# print(print_h1)
# both remember the tag sent in print_h1 variable
print_h1('Test headline!')
print_h1('Another headline!')

print_p = html_tag('p')
print_p('Test Paragraph!')

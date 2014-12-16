

# def add_one(f):
#     def inner(x, y):
#         return f(x, y) + 1
#     return inner

# @add_one
# def addition(x, y):
#     return x + y

###################

# def add_one(f):
#     return f + 1


# def addition(x, y):
#     return x + y

###################

def add_one(x):
    return x + 1


def addition(f, x, y):
    return f(x + y)


if __name__ == "__main__":

    #assert(addition(add_one, 1, 2)) == 4
    #assert(add_one(addition(1, 2))) == 4
    assert(addition(add_one, 1, 2)) == 4
    print "tests passed"


s = 0

def square(x, y):
    return x * y

def outer(a, b, c):
    def inner():
        s = 2 * (square(a, b) + square(a, c) + square(b, c))
        return s
    return inner()

print(outer(2, 4, 6))


s = 0
def outer(a, b, c):
    def inner(x, y):
        return x * y
    s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
    return s

print(outer(5, 8, 2))


def outer(a, b, c):
    def inner(x, y):
        return x * y
    s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
    return s

print(outer(1, 6, 8))




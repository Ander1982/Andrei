

def average(func):
    def wrap(*args, **kwargs):
        i = len(args)
        func(*args, **kwargs)
        j = s / i
        y = ''
        for x in args:
            y += str(x) + ', '
        print('Среднее арифметическое чисел', y[:-2], '=', j)
        
    return wrap

@average
def sum_1(*args):
    global s
    s = sum(args)
    a = ''
    for i in args:
        a += str(i) + ', '
    print('Cумма чисел', a[:-2], '=', s)

sum_1(2, 3, 3, 4)

def average(func):
    def wrap(*args, **kwargs):
        i = len(args)
        func(*args, **kwargs)
        j = s / i
        y = ''
        for x in args:
            y += str(x) + ', '
        print('Среднее арифметическое чисел', y[:-2], '=', j)


        return wrap


@average
def sum_2(*args):
    global s
    s = sum(args)
    a = ''
    for i in args:
        a += str(i) + ', '
    print('Cумма чисел', a[:-2], '=', s)


sum_2(2, 3, 3, 4)




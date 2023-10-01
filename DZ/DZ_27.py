class Power:
    def __init__(self, dec):
        self.dec = dec

    def __call__(self, mul):
        def wrap(a, b):
            print('Результат:', mul(a, b) ** self.dec)

        return wrap


@Power(3)
def multiplication(a, b):
    return a * b


multiplication(2, 2)

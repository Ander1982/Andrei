class Square:
    def __init__(self, a):
        self.a = a

    def get_per_rerimetrct(self):
        return 4 * self.a

if __name__ == "__main__":
    print('*' * 20)
    s1 = Square(10)
    print(s1.get_per_rerimetrct())
    print("*" * 20)

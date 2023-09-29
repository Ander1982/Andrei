class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_per_rerimetrct(self):
        return 2 * (self.w + self.h)


__author__ = "Andrei"
if __name__ == "__main__":
    print(f'Modul {__name__} (author: {__author__}).')

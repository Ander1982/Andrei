class CarClass:
    def __init__(self, brand, model, year, prodeg):
        self.brand = brand
        self.model = model
        self.year = year
        self.probeg = prodeg

    def show_car(self):
        print(f"{self.brand}, {self.model}, {self.year} год, {self.probeg} км")

if __name__ == '__main__':
    car = CarClass("Tesla", 'T', 2018, 99000)
    car.show_car()

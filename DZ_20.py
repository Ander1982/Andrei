class Car:
    model = 'model'
    year = '0000'
    manufacturer = 'brand'
    power = '000 hp'
    color= 'color'
    price = '00000000000'

    def print_info(self):
        print('Данные автомобиля'.center(40, "*"))
        print(f'Модель: {self.model}\nГод выпуска: {self.year}\nМарка: {self.manufacturer}'
              f'\nМощность двигателя: {self.power}\nЦвет: {self.color}\nЦена: {self.price}')
        print('=' * 40)

    def input_info(self, model, year, manufacturer, power, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.power = power
        self.color = color
        self.price = price

    def set_model(self, new):
        self.model = new
    def get_model(self):
        return self.model

    def set_year(self, new):
        self.year = new

    def get_year(self):
        return self.year

    def set_manufacturer(self, new):
        self.manufacturer = new

    def get_manufacturer(self):
        return self.manufacturer

    def set_power(self, new):
        self.power = new

    def get_power(self):
        return self.power

    def set_color(self, new):
        self.color = new

    def get_color(self):
        return self.color

    def set_price(self, new):
        self.price = new

    def get_price(self):
        return self.price

c1 = Car()
c1.print_info()
c1.input_info('X7 M50i', '2021', 'BMW', '530 л.с.', 'white', ' 10790000')
c1.print_info()
c1.set_model('A6 2X2')
print('Новая модель:', c1.get_model())
c1.set_year('2023')
print('Год:', c1.get_year())
c1.set_manufacturer('Audi')
print('Новый бренд:', c1.get_manufacturer())
c1.set_power('220 л.с')
print('Мощность:', c1.get_power())
c1.set_color('black')
print('цвет:', c1.get_color())
c1.set_price('9800000')
print('Цена:', c1.get_price())
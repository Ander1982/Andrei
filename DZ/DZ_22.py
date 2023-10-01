import re

class Account:

    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'
    rate_usd = 0.013
    rate_eur = 0.011

    def __init__(self, surname, num, percent, value):
        self.surname = surname
        self.num = num
        self.percent = percent
        self.value = value
        print(f'Счет #{self.num} принадлежащий {self.surname} был открыт.')
        print('*' * 50)

    def __del__(self):
        print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт.')
        print('*' * 50)

    @staticmethod
    def convert(value, rate):
        return value * rate

    @staticmethod
    def verify_surname(surname):
        if not isinstance(surname, str):
            raise TypeError('Фамилия должна быть строкой')
        list_1 = list(surname)
        l = ''.join(re.findall('[a-zа-яё-]', surname, flags=re.IGNORECASE))
        for i in list_1:
            if len(i.strip(l)) != 0:
                raise TypeError("Можно ввводить только буквы и дефис")
        if l.title() != l:
            raise TypeError('Первая буква должна быть заглавной')


    @staticmethod
    def verify_num(num):
        if not isinstance(num, str):
            raise TypeError('Номер счета должен быть строкой')
        num_1 = list(num)
        for i in num_1:
            if not i.isdigit():
                raise TypeError('Номер должен содержать цифры')
        if len(num_1) != 5:
            raise TypeError('Номер должен состоять из 5 цифр')

    @staticmethod
    def verify_percent(percent):
        if not isinstance(percent, float):
           raise TypeError('Проценты должны быть вещественным числом')

    @staticmethod
    def verify_value(value):
        if not isinstance(value, int) and not isinstance (value, float):
            raise TypeError('Сумма должна быть вещественным или обычным числом')

    @classmethod
    def set_usa_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.verify_surname(surname)
        self.__surname = surname

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.verify_num(num)
        self.__num = num

    @property
    def percent(self):
        return  self.__percent

    @percent.setter
    def percent(self, percent):
        self.verify_percent(percent)
        self.__percent = percent

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.verify_value(value)
        self.__value = value

    def convert_to_usd(self):
        convert_usd = Account.convert(self.value, Account.rate_usd)
        print(f'Состояние счета: {convert_usd} {Account.suffix_usd}')

    def convert_to_eur(self):
        convert_eur = Account.convert(self.value, Account.rate_eur)
        print(f'Состояние счета: {convert_eur} {Account.suffix_eur}')

    def edit_owner(self, surname):
        self.surname = surname
        self.print_info()

    def add_percent(self):
        self.value += self.value * self.percent
        print(f'Проценты были успешно начислены!')
        self.print_balance()

    def withdraw_money(self, sum):
        if sum > self.value:
            print(f'К сожалению у Вас нет {sum} {Account.suffix}')
        else:
            self.value -= sum
            print(f'{sum} {Account.suffix} было успешно снято!')
        self.print_balance()

    def add_money(self, sum):
        self.value += sum
        print(f'{sum} {Account.suffix} было успешно добавлено!')
        self.print_balance()


    def print_balance(self):
        print(f'Состояние счета: {self.value} {Account.suffix}')

    def print_info(self):
        print(f'Информация о счете:')
        print('-' * 20)
        print(f'#{self.__num}')
        print(f'Владелец: {self.__surname}')
        print(f'Текущий баланс {self.__value}')
        print(f'Проценты: {self.__percent:.0%}')
        print('-' * 20)

acc = Account("Ivanov", '88880', 0.03, 898)
acc.print_info()
acc.surname = ('Тванов')
acc.num = ('09090')
acc.percent = (0.99)
acc.value = (1090)
acc.print_info()


# Вариает employee.py

import re

class Account:

    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'
    rate_usd = 0.013
    rate_eur = 0.011

    def __init__(self, surname, num, percent, value):
        self.verify_surname(surname)
        self.verify_num(num)
        self.verify_percent(percent)
        self.verify_value(value)
        self.surname = surname
        self.num = num
        self.percent = percent
        self.value = value
        print(f'Счет #{self.num} принадлежащий {self.surname} был открыт.')
        print('*' * 50)

    def __del__(self):
        print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт.')
        print('*' * 50)

    @staticmethod
    def convert(value, rate):
        return value * rate

    @staticmethod
    def verify_surname(surname):
        if not isinstance(surname, str):
            raise TypeError('Фамилия должна быть строкой')
        list_1 = list(surname)
        l = ''.join(re.findall('[a-zа-яё-]', surname, flags=re.IGNORECASE))
        for i in list_1:
            if len(i.strip(l)) != 0:
                raise TypeError("Можно ввводить только буквы и дефис")
        if l.title() != l:
            raise TypeError('Первая буква должна быть заглавной')


    @staticmethod
    def verify_num(num):
        if not isinstance(num, str):
            raise TypeError('Номер счета должен быть строкой')
        num_1 = list(num)
        for i in num_1:
            if not i.isdigit():
                raise TypeError('Номер должен содержать цифры')
        if len(num_1) != 5:
            raise TypeError('Номер должен состоять из 5 цифр')

    @staticmethod
    def verify_percent(percent):
        if not isinstance(percent, float):
           raise TypeError('Проценты должны быть вещественным числом')

    @staticmethod
    def verify_value(value):
        if not isinstance(value, int) and not isinstance (value, float):
            raise TypeError('Сумма должна быть вещественным или обычным числом')

    @classmethod
    def set_usa_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    def get_surname(self):
        return self.surname

    def set_surname(self, surname):
        self.verify_surname(surname)
        self.surname = surname

    def get_num(self):
        return self.num

    def set_num(self, num):
        self.verify_num(num)
        self.num = num

    def get_percent(self):
        return  self.percent

    def set_percent(self, percent):
        self.verify_percent(percent)
        self.percent = percent

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.verify_value(value)
        self.value = value

    def convert_to_usd(self):
        convert_usd = Account.convert(self.value, Account.rate_usd)
        print(f'Состояние счета: {convert_usd} {Account.suffix_usd}')

    def convert_to_eur(self):
        convert_eur = Account.convert(self.value, Account.rate_eur)
        print(f'Состояние счета: {convert_eur} {Account.suffix_eur}')

    def edit_owner(self, surname):
        self.surname = surname
        self.print_info()

    def add_percent(self):
        self.value += self.value * self.percent
        print(f'Проценты были успешно начислены!')
        self.print_balance()

    def withdraw_money(self, sum):
        if sum > self.value:
            print(f'К сожалению у Вас нет {sum} {Account.suffix}')
        else:
            self.value -= sum
            print(f'{sum} {Account.suffix} было успешно снято!')
        self.print_balance()

    def add_money(self, sum):
        self.value += sum
        print(f'{sum} {Account.suffix} было успешно добавлено!')
        self.print_balance()


    def print_balance(self):
        print(f'Состояние счета: {self.value} {Account.suffix}')

    def print_info(self):
        print(f'Информация о счете:')
        print('-' * 20)
        print(f'#{self.num}')
        print(f'Владелец: {self.surname}')
        print(f'Текущий баланс {self.value}')
        print(f'Проценты: {self.percent:.0%}')
        print('-' * 20)

acc = Account("Ivanov", '88880', 0.03, 898)
acc.print_info()
acc.set_surname('Mggh')
acc.set_num("99099")
acc.set_percent(0.09)
acc.set_value(100)
acc.print_info()

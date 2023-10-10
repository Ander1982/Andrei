
number = int(input("Введите пятизначную цифру"))
number1 = number // 10000
number2 =  number // 1000 - number1 * 10
number3 = number // 100 - number2 * 10  - number1 * 100
number4 = number // 10 - number3 * 10 - number2 * 100 - number1 * 1000
number5 = number - number4 * 10 - number3 * 100 - number2 * 1000 - number1 * 10000
industrialТumbers = number1 * number2 * number3 * number4 * number5
print('Произведение цифр числа:', number, '=', industrialТumbers)
sumNumbers = (number1 + number2 + number3 + number4 + number5)
print('Сумма цифр числа:', number, '=', sumNumbers)

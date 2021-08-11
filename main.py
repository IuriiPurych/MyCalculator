# Задание 2
# Напишите программу-калькулятор, которая поддерживает следующие операции:
# сложение, вычитание, умножение, деление и возведение в степень.
# Программа должна выдавать сообщения об ошибке и продолжать работу при вводе некорректных данных,
# делении на ноль и возведении нуля в отрицательную степень.
class OperationException(Exception):
    def __init__(self, text):
        print('Wrong operation:', text)


print('My calculator.')
operations = ('+', '-', '*', '/', '^')
while True:
    try:
        value1 = float(input('Input first value: '))
        value2 = float(input('Input second value: '))
        operation = input('Input operation: ')
        if operation not in operations:
            raise OperationException(operation)
    except ValueError as e:
        print(e)
    except OperationException as e:
        pass
    else:
        try:
            if operation == '+':
                print(value1, '+', value2, '=', value1 + value2)
            elif operation == '-':
                print(value1, '-', value2, '=', value1 - value2)
            elif operation == '*':
                print(value1, '*', value2, '=', value1 * value2)
            elif operation == '/':
                print(value1, '/', value2, '=', value1 / value2)
            elif operation == '^':
                print(value1, '^', value2, '=', pow(value1, value2))
        except ZeroDivisionError as e:
            print(e)

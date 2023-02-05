import random
import os
import sys

digits = '0123456789'
digits.split()
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
lowercase_letters.split()
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
uppercase_letters.split()
punctuation = '!#$%&*+-=?@^_.'
punctuation.split()
chars = []
print('Добро пожаловать в генератор безопасных паролей')

count = int(input('Введите колличество паролей\n'))
pass_lenght = int(input('Введите длину одного пароля\n'))

question1 = input('включать ли цифры(д-да,н-нет)\n')
if question1 == 'д':
    chars += digits
elif question1 == 'н':
    var = None
else:
    print('Ошибка ввода')
    os.execl(sys.executable, sys.executable, *sys.argv)
question2 = input('включать ли прописные буквы(д-да,н-нет)\n')
if question2 == 'д':
    chars += lowercase_letters
elif question2 == 'н':
    var = None
else:
    print('Ошибка ввода')
    os.execl(sys.executable, sys.executable, *sys.argv)
question3 = input('включать ли строчные буквы(д-да,н-нет)\n')
if question3 == 'д':
    chars += uppercase_letters
elif question3 == 'н':
    var = None
else:
    print('Ошибка ввода')
    os.execl(sys.executable, sys.executable, *sys.argv)
question4 = input('включать ли символы(д-да,н-нет)\n')
if question4 == 'д':
    chars += punctuation
elif question4 == 'н':
    var = None
else:
    print('Ошибка ввода')
    os.execl(sys.executable, sys.executable, *sys.argv)
question5 = input('исключать ли символы il1Lo0O(д-да,н-нет)\n')
if question5 == 'д':
    chars.remove('i')
    chars.remove('l')
    chars.remove('1')
    chars.remove('L')
    chars.remove('o')
    chars.remove('0')
    chars.remove('O')
elif question5 == 'н':
    var = None
else:
    print('Ошибка ввода')
    os.execl(sys.executable, sys.executable, *sys.argv)
a = []
i = 0
while i < count:
    if len(a) < pass_lenght:
        a.append(random.choice(chars))
    elif len(a) == pass_lenght:
        print(*a, sep='')
        a = []
        i += 1

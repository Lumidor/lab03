ch1 = float(input('Введите число:'))
zn = input('Введите: +, -, * или / :')
ch2 = float(input('Введите число:'))
if zn == '+':
    print(f'{(ch1+ch2):.2f}')
elif zn == '-':
    print(f'{(ch1-ch2):.2f}')
elif zn == '*':
    print(f'{(ch1*ch2):.2f}')
elif zn == '/':
    while ch2 != 0:
        print(f'{(ch1/ch2):.2f}')
    else:
        print('Деление на ноль запрещено')
else:
    print('Неизвестная операция')

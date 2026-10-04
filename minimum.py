ch1 = int(input('Введите число:'))
ch2 = int(input('Введите число:'))
ch3 = int(input('Введите число:'))
if ch1<ch2 and ch1<ch3:
    print('Наименьшее:', ch1)
elif ch2<ch1 and ch2<ch3:
    print('Наименьшее:', ch2)
elif ch3<ch1 and ch3<ch2:
    print('Наименьшее:', ch3)

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
value = list(per_cent.values())  # формируем список значений
money0 = input('Введите сумму: ')  # сумма от пользователя
print(money0)
num = ""    # Извлекаем числа из текста в str///
for c in money0:
    if c.isdigit():
        num = num + c  # ///////////////////////
print(type(num))
deposit = [] # список накопленных средств за год вклада
if num != '':
    money = int(num)
    print(type(money))
    for i in value:
        deposit.append(int(i*money/100)) #   добовляем в список сумму накоплений по каждому банку
    print(deposit)
    deposit_str = str(max(deposit))
    # print('Максимальная сумма, которую вы можете заработать —', deposit_str)
    print(deposit_str[:-3] + ' ' + deposit_str[-3:])
else:
    print('введите цифры')
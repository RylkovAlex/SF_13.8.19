def get_sum(message):
    try:
        return int(input(message))
    except ValueError:
        return get_sum('Пожалуйста введите число:\n')


def calculate_deposit(money, per_cent={'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}):
    if money <= 0:
        return print('Рассчёт депозита возможен только для положительных значений!')
    deposits = list(map(lambda kv: (kv[0], int(kv[1] * money)), per_cent.items()))
    max_deposit = max(deposits, key=lambda kv: kv[1])
    print(
        f'Максимальная сумма, которую вы можете заработать — {max_deposit[1]} (депозит в {max_deposit[0]} банке, без расчёта сложных процентов).')
    print(f'Расчёт по всем банкам:\n{str(dict(deposits)).strip("{}")}')


calculate_deposit(get_sum('Введите сумму, которую планируете положить под проценты:\n'))
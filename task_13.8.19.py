def input_positive_int(input_message,
                       input_error_message='Ошибка ввода данных! Введите пожалуйста положительное целое число:\n'):
    value = None
    is_first_try = True
    while not value:
        try:
            value = int(input(input_message)) if is_first_try else int(input(input_error_message))
            if value > 0:
                return value
            value = None
            raise ValueError
        except ValueError:
            is_first_try = False
            continue


def calculate_prise(tickets_quantity):
    def get_prise(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390

    is_discount = tickets_quantity > 3
    ages = [input_positive_int(f'Введите возраст участника №{i + 1}\n') for i in range(0, tickets_quantity)]
    full_prise = sum(map(get_prise, ages))
    return int(full_prise * 0.9) if is_discount else full_prise


prise = calculate_prise(input_positive_int('Введите желаемое количество билетов:\n'))
print(f'К оплате: {prise} руб.')

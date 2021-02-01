# Первое задание от Михея.
# Цель задачи создать валидатор для банковских карт.
if __name__ == '__main__':
    manager = ''
    while manager != 'exit':
        onError = False
        cardNumber = ''
        try:
            cardNumber = int(input('Введите номер карты'))
        except:
            print('введите цыфры')
            onError = True
        if cardNumber == 1111 and not onError:
            print('MASTER CARD')
        elif cardNumber == 2222 and not onError:
            print('VISA')
        elif not onError:
            print('not found')
        manager = 'exit'
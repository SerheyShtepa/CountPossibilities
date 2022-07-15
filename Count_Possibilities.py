

def count_possibilities(n):

    if n < 0:
        return 0
    if n == 0:
        return 1
    return count_possibilities(n - 1) + count_possibilities(n - 2) + count_possibilities(n - 3)


if __name__ == '__main__':
    while True:
        try:
            n = int(input('Введите количество ступенек.\nДля остановки введите "0"\n:'))
        except:
            print('Некорректный ввод!!!')
            continue
        if n == 0:
            break
        print(f'При количестве ступенек {n}, у вас есть', count_possibilities(n), 'способов подняться вверх.')


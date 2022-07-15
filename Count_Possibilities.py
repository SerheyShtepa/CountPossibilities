

def count_possibilities(n):

    if n < 0:
        return 0
    if n == 0:
        return 1
    return count_possibilities(n - 1) + count_possibilities(n - 2) + count_possibilities(n - 3)


if __name__ == '__main__':
    n = int(input('Введите количество ступенек:'))
    print(f'При количестве ступенек {n}, у вас есть', count_possibilities(n), 'способов подняться вверх.')


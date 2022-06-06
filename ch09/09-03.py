import random

def nrandom(start, end, n, duplicated = False):
    lst = []
    if duplicated:
        for _ in range(n):
            lst.append(random.randint(start, end))
    else:
        lst = list(random.sample(range(start, end + 1), n))

    return sorted(lst)

if __name__ == '__main__':
    print('로또 복권: ', nrandom(1, 45, 6))
    print('주사위 3번: ', nrandom(1, 6, 3, True))



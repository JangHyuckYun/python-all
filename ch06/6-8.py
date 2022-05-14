from random import randrange
from random import sample

mylotto = set()
while True:
    num = randrange(1,46)
    print(num, end='')
    mylotto.add(num)
    if len (mylotto) == 6:
        break
print()
print('집합: {}'.format(mylotto))
print('정렬 리스트: {}'.format(sorted(mylotto)))
print()

lotto = sample(range(1, 46), 6)
print('sample 함수 리스트: {}'.format(lotto))
print('sample 함수 정렬 리스트: {}'.format(sorted(lotto)))
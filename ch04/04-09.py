n = input('10진수의 한 자릿수 입력 >> ')
print('두 자릿수 정수에서 최소 한 자릿수가 %s인 정수 찾기: ' % n)
print(' 결과: '.center(50, '='))

for i in range(10, 100):
    snum = str(i)
    if n in snum:
        print(i, end= ' ')
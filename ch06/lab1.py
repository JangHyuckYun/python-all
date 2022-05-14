from random import choice

dcs = {'가위': '보오', '바위': '보오', '보오': '바위'}

tit = ['비김', '철수', '영희', '승자']

rsp = ('가위', '바위', '보오')

print('*' * 17)
print('{:4} {:4} {:4}'.format(tit[1], tit[2], tit[3]))
print('*' * 17)

for _ in range(10):
    cs = choice(rsp)
    yh = choice(rsp)

    print('{:4} {:4}'.format(cs, yh), end=' ')

    if cs == yh:
        index = 0
    elif dcs[cs] == yh:
        index = 1
    else:
        index = 2

    print('{:4}'.format(tit[index]))
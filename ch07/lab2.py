from random import sample

winnum = set()

def buyautolotto():
    lotto = []
    for i in range(5):
        # lst = sorted(list(sample(list(range(1, 46)), 6)))
        num6 = set(sample( list(range(1, 46)), 6 ))
        lotto.append(num6)
    return lotto

def printnums(nums):
    for num in sorted(nums):
        print("%02d" % num, end = ' ')
    print()

def printlotto(lotto):
    for i, item in enumerate(lotto):
        print("%c 자 동 " % (ord('A') + i), end = '')
        printnums(item)
    print()

def setwinlotto():
    global winnum
    winnum = set(sample( list(range(1, 46)), 6 ))

def getwinner(lotto):
    for i, item in enumerate(lotto):
        print('%c' % (ord('A') + i), end = ' ')
        win = winnum.intersection(set(item))
        if win:
            wincnt = len(win)
            print('당첨번호 개수 %d,' % wincnt, end='')
            printnums(win)
        else:
            print('꽝')

lotto = buyautolotto()
printlotto(lotto)
setwinlotto()
print('당첨번호: ', end='')
printnums(winnum)
print()
getwinner(lotto)
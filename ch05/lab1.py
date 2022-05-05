sports = ['축구', '야구', '농구', '배구']

num = [11,9,5,6]
print(num)

for i in range(len((sports))):
    print('%s: %d명 '%(sports[i], num[i]), end = ' ')
print(); print()


sponum = [sports, num]
print(sponum)

for i in range(len((sponum))):
    print('%s: %d명 '%(sponum[0][i], sponum[1][i]), end = ' ')
print(); print()

psponum = [[sports[i], num[i]] for i in range(len(sports))]
print(psponum)

for one in psponum:
    print('%s: %d명 '%(one[0], one[1]), end = ' ')
print()

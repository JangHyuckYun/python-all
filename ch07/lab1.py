from random import randint

def setsequence(start, end, count):
    global nums
    for _ in range(count):
        nums.append(randint(start, end))

nums = []
setsequence(1, 100, 10)
print(sorted(nums))
print('합: %d, 평균: %.2f' % (sum(nums), sum(nums) / len(nums)))
print('최대: %d, 최소: %d' % (min(nums), max(nums)))
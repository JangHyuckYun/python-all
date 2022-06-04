circle = [3,5,7,10]
area = list(map(lambda r: r * r * 3.14, circle))

for c,a in zip(circle, area):
    print('반지름 {} => 원면적 {}'.format(c, a))
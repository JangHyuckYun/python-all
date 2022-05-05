a = []
for i in range(10):
    a.append(i)
print(a)

seq = [i for i in range(10)]
print(seq)

s = []
for i in range(10):
    if i % 2 == 0:
        s.append(i**2)
print(s)

squares = [i**2 for i in range(10) if i%2== 1]
print(squares)
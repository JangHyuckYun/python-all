# 20224224 윤장혁

word = list('삶꿈정')
word.extend('복및')
print(word)
word.sort()
print(word)

fruit = ['복숭아', '자두', '골드키위', '귤']
print(fruit)
fruit.sort(reverse=True)
print(fruit)

mix = word + fruit
print(sorted(mix))
print(sorted(mix, reverse=True))

f1 = ['사과', '귤', '복숭아', '파인애플']
f2 = f1
f2.pop()
print(f1)
print(f2)
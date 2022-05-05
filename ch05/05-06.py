food = ['짜장면', '짬뽕', '우동', '울면']
print(food)

food.append('탕수육')
print(food)

food[1] = '귤짬뽕'
print(food)

food[food.index('우동')] = '물만두'
print(food)
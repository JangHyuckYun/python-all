words = "The core of extensible programming is defining functions.".split()

print(sorted(words, key= str.lower))

print(sorted(words, key= lambda word: word[1]))

groupnumber = [('잔나비', 5), ('트와이스', 5), ('블랙핑크', 4), ('방탄소년단', 7)]

print(sorted(groupnumber))

print(sorted(groupnumber, key=lambda singer: singer[1]))
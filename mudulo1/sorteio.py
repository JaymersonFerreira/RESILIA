from random import randint

sort = []
while True:   
    num = randint(1, 5)
    if num not in sort:
        sort.append(num)
    if len(sort) == 5:
        break
    
print(sort)

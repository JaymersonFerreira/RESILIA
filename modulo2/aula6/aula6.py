# tupla04 = ('a',)
# tupla04 = tupla04 + ('b',)
# tupla04 = tupla04 + ('c',)

# print(tupla04(0))


# if (0,1,2) < (0,1,4):
#     print('verdadeiro')
# else:
#     print('falso')

# if (0,1,5) < (0,1,4):
#     print('verdadeiro')
# else:
#     print('falso')

# x = 10
# y = 20

# x,y = y,x

# print(x,y)

# a,b = 1,2
# print(a,b)

# tupla = ()
# for i in range(10):
#     tupla = tupla + (i)

# print(tupla)

tupla1 = (0,1,2,3,4,5,6,7,8,9)
tupla2 = (0,1,2,3,4,5,6,7,8,9)
tupla3 = ()
tupla4 = ()
# tupla3 =  tupla1 * tupla2
for i in range(10):
    tupla3[i] += tupla1[i] * tupla2[i]

print(tupla3)

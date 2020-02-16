# Dictionary
d = {'key1': 'value', 'key2': 123}
print('Print out key 2: ' + str(d['key2']))

e = {'k1': [1, 2, 3]}
print('Priting out the values in k1: ' + str(e['k1']))
my_list = e['k1']
print('Return first value of the list: ' + str(my_list[0]))

t = (1, 2, 3)
my_list[0] = 'NEW'
print(str(t) + ' ' + str(my_list))
# tople are immutable, so they cant change the values like the list
# t[0] = 'NEW' returns an error

# Comparison operators
b = 1<2
print('Returns true: ' + str(b))

c = (1 < 2) and (2 < 3)
print('Should print true: ' + str(c))

d = (1 < 2) or (2 > 3)
print('Should print true eventhough last condition os false: ' + str(d))

if 1<2:
    print('1 is less then 2')

if my_list[0] == 2:
    print('First')
else:
    print('Last')

# 1: Power of
print('Task 1: ')

x = 7 ** 4
print(x)

print('-------------------------------')
# 2: Split the string
print('Task 2: ')

s = "Hi, there Sam!"
print(s.split())
print(s.split(','))

print('-------------------------------')
# 3 grab value from nested dictionary:
print('Task 3: ')

d = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}
print(d.keys())
# Only one key
print(d['k1'][3]['tricky'][3]['target'][3])

print('-------------------------------')
# 4 format
print('Task 4: ')

planet = "Earth"
diameter = 12742
print('The diameter of {} is {}'.format(planet, diameter))

print('-------------------------------')
# 5 indexing
print('Task 5: ')

lst = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
print(lst[3][1][2][0])

print('-------------------------------')
# 6 create functuin
print('Task 6: ')


def domainGet(email):
    return email.split('@')[1]


print(domainGet('hei@gmail.com'))

print('-------------------------------')
# 7 Count word
print('Task 7: ')


def countDog(st):
    count = 0
    for word in st.lower().split():
        if word == 'dog':
            count += 1
    return "Amount of times 'dogs' have been said is: " + str(count)


print(countDog('I have the best dog. The dog is tall and good. The DoG is 7 years old'))
print('-------------------------------')

# 8 lambda to filter
print('Task 8: ')

seq = ['soup', 'dog', 'salad', 'cat', 'great']
my_list = list(filter(lambda word: word[0] == 's', seq))
print(my_list)

print('--------------------------')

# 9 Final problem:
print('Task 9')


def caught_speeding(speed, is_birthday):
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed

    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'


print(caught_speeding(81, True))

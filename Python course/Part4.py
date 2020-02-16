# Lambda functions:
def times2(var):
    return var*2


print(times2(2))
print('-----------------------------------------')

seq = [1, 2, 3, 4, 5]
print(list(map(times2, seq)))
print('-----------------------------------------')

# Rewriting function times2 to a lambda expression
t = lambda var:var*2
print(t(6))
print('-----------------------------------------')

print(list(map(lambda num: num*3, seq)))
print('-----------------------------------------')

# Filter-function:
my_list = list(filter(lambda num: num%2 == 0, seq))
print(my_list)

# Methods:
s = 'Hello, my name is Sam'
print(s.lower() + '\n' + str(s.split()))
print('-----------------------------------------')
tweet = 'Go sports! #Sports'
print(tweet.split('#'))
print('-----------------------------------------')

d = {'k1': 1, 'k2': 2}
print(d.items())
print(d.values())
print('-----------------------------------------')
print(seq)
seq.pop(3)
print(seq)
seq.insert(3, 4)
print(seq)
print('-----------------------------------------')

# Packing tuples:
x = [(1, 2), (3, 4), (5, 6)]
for (a, b) in x:
    print(a)
    print(b)

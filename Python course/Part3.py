# For-loops:
seq = [1, 2, 3, 4, 5]

for num in seq:
    print(str(num))
print('-----------------------------------------')
i = 1
while i <= 5:
    print('i is: {}'.format(i))
    i = i + 1
print('-----------------------------------------')
range(0, 5)
for x in range(0, 5):
    print(x)
print('-----------------------------------------')
my_list = list(range(0, 5))
for x in my_list:
    print(x)
print('-----------------------------------------')
x = [1, 2, 3, 4]
out = []
for num in x:
    out.append(num ** 2)
print(out)
# Comprehend this to a list:

comprehend_out = [num ** 2 for num in x]
print(comprehend_out)

print('-----------------------------------------')


# Functions:
def my_func(param1):
    print(param1)


my_func('Hello World!')


# Generating another functuin
def my_func2(name='Default name'):
    print('Hello ' + name)


my_func2('Sam')

# Default name
my_func2()

print('-----------------------------------------')


def square(num):
    """
    THIS IS A DOCSTRING.
    THIS FUNCTUIN SQUARES A NUMBER
    :param num:
    :return:
    """
    return num ** 2


output = square(3)
print(output)
print('-----------------------------------------')
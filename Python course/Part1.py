# Datatypes:

x = 2
y = 3
print(x + y)

z = 1.2
k = 2.4
print(z * k)

# Strings:
single_quote = 'This is the first string'
double_quote = "This is the second string"
mixed_quote = "Single quote inside can't be forgotten"

print(single_quote + "\n" + double_quote + "\n" + mixed_quote)

# Print formatting:
num = 12
name = 'Sam'
print('My number is {} and my name is {}'.format(num, name))

print('My number is {one} and my name is {two}'.format(one=num, two=name))

# Indexing Strings:
s = 'hello'
print('Should print out h:' + '\n' + s[4])

s = 'abcdefg'
print('Should print out first 3 letters: ' + s[:3])
print('Should print out last 3 letters: ' + s[4:])
print('Should print out mid letters: ' + s[2:5])

# List:
my_list = ['a', 'b', 'c']
# Adding to list:
my_list.append('e')
print('Printing last value: ' + my_list[3])
nest = ['a', 'b', ['c', 'd']]
print('Printing nested list ' + nest[2][1])

# Variables
a = 1
b = 2

# Conditional examples
if a < b:
    print("a is less than b")
if a > b:
    print("Unreachable")

# if, elif, else
if a != 0:
    print("a is not equal to 0")
elif a > 1:
    print("a is greater than 1")
else:
    print("a is not equal to zero nor greater than 1")

# Conditional Expression (Ternary operator)
###########################################

# Example 1
raining = False
raining = True
print("Let's go to the", 'beach' if not raining else 'library')

# Example 2
age = 12
age = 40
s = 'minor' if age < 21 else 'adult'
print(age, s)

# Example 3
'yes' if ('baz' in ['foo', 'bar', 'baz']) else 'no'

'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'
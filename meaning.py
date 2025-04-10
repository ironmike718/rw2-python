meaning = 42
print('')

# if meaning > 10:
#     print('Right on!')
# else:
#     print('Not today')

# Ternary Operator
print('Right on!') if meaning > 10 else print('Not today')

# learn how to use and and or operators

# x = 10
x = 1
# y = 20
y = 1
z = 30

if x > 5 and y > 10:
    print("Both are True")
else:
    print("Atleast 1 is not True")

if x > 5 or y > 10:
    print("Atleast 1 is True, successful OR")
else:
    print("None are True")
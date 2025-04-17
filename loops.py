# Playing with Loops!

# while loops

#value = 1
#while value <= 10:
#    print("the value of value is: " + str(value))
#    if value == 5:
#        break
#    value += 1

# value = 1
# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))

# for loops

# names = ["Kita", "Jaylen", "George"]
# for x in names:
#     print("Name of student is " + x)

names = ["Kita", "Jaylen", "George"]
actions = ["Studies", "Works", "Sleeps"]

for name in names:
    for action in actions:
        print(name + " " + action + ".")


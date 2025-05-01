# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if file doesn't exist

my_file = open("names.txt", "r")

#print(my_file.read())
#print(my_file.read(4))

#print(my_file.readline())
#print(my_file.readline())

for line in my_file:
    print(f"Student name is {line}")


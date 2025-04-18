
def multiple_items(*args):
    print(args)
    print(type(args))
    print(args[0])
    print(args["Ashley"])

multiple_items("Dave", "John", "Sara")

my_dictionary = {
    "Ashley":"Hacker",
    "Jaylen":"Coder",
    "George":"GRC Master",
}
multiple_items(my_dictionary)
# concatenate to print strings
person = "Dave"
coins = 3
print("\n" + person + " has " + str(coins) + " coins left.")


# use %s to print strings
message = "\n%s has %s coins left." % (person, coins)
print(message)


# use .format method to print strings
message = "\n{} has {} coins left.".format(person, coins)
print(message)


# use f-strings to print strings
message = f"\n{person} has {coins} coins left."
print(message)


student = "kita"
subject = "python"

print(f"{student} is studying {subject}\n")



import mypyvars
from pythonping import ping

# these variables were imported from mypyvars.py file
print(f"username is {mypyvars.uname} and password is {mypyvars.pword}")

# this function was imported from mypyvars.py file
value = mypyvars.calc()
print(f"the value of my variable is {value}")

message = ping('127.0.0.1', verbose=False)

print(message)
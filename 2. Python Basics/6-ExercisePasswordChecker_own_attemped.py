print('Whats your username')
username_data = str(input())
print('Whats your password')
password_data = str(input())
password_lenght = len(password_data)
#für Python 3.6 soll man laut dev F strings nehmen wichtig is,dass man beim Multiplizieren der Password länge (password_lenght) das * mit den den doppelt "" zeichen setzt....
print (f'Hello {username_data}, your password is {"*" * password_lenght} length is {password_lenght}')

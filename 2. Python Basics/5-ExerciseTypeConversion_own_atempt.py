from datetime import datetime
print('Whats your brithday year:')
z = int(input())
x = datetime.now().year
y = int(x) - z
print('Your Age ist, ' + str(y))

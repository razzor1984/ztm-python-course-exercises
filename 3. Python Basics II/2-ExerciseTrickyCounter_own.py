
#liste wird hier definiert
my_list = [1,2,3,4,5,6,7,8,9,10]
#neue Variabel wird auf 0 gesetzt
total =  0

#man looped durch die liste 1 bis 10 dann werden die daten in total abgespeichert
for value in my_list:
   total = total + value

print(total)

#Variante zwei mit sum funktion ohne schleife

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = sum(my_list)
print(total)

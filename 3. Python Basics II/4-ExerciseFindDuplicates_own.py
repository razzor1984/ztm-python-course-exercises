#Exercise: Check fpr duplicates in List
some_list = ['a', 'b', 'c', 'b', 'd', 'm' ,'n', 'n']

# list to store duplicate elements
duplicate = []

for num in some_list:
    # check if it is duplicate of not
    if some_list.count(num) > 1:
        # check if it is already present in the list or not
        if num not in duplicate:
            duplicate.append(num)

print(duplicate)

# VARIANTE 2
# nested loops to find duplicates
for i in range(len(some_list)):
    for j in range(i+1, len(some_list)):
        if some_list[i] == some_list[j]:
            print(some_list[i])
            break

# VARIANTE 3
# create a list of duplicate elements
duplicates = list(set([num for num in some_list if some_list.count(num) > 1]))
print(duplicates)

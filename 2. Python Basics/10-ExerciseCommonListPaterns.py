#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']

print(friends.sort() + new_friend)


EDIT:
OWN TRY

friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
friends.append('Stanley')
sort_newlist = sorted(friends)

print(sort_newlist)










































# Solution: (keep in mind there are multiple ways to do this, so your answer may vary. As long as it works that's all that matters!)
# friends.extend(new_friend)
# print(sorted(friends))



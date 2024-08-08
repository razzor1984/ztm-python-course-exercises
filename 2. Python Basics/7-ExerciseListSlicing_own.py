#What is the output of this code?
#Before you clikc RUN, guess the output of each print statement!
new_list = ['a', 'b', 'c']
print(new_list[1])                      own: output =  a
print(new_list[-2])                     own: output =  0  
print(new_list[1:3])                    own: output = a b c
new_list[0] = 'z'                        
print(new_list)                         own: output = z a b c

my_list = [1,2,3]                        
bonus = my_list + [5]                    
my_list[0] = 'z'
print(my_list)                          own: output = z 1 2 3 
print(bonus)                            own: output = 1 2 3 5

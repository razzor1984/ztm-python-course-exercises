#What is the output of this code?
#Before you clikc RUN, guess the output of each print statement!
new_list = ['a', 'b', 'c']
print(new_list[1])                      #own: output =  a            #PC = b                In Python beginnen Listenindizes tatsächlich bei 0. Das bedeutet, dass der erste Eintrag in der Liste den Index 0 hat, der zweite Eintrag den Index 1, und so weiter.
print(new_list[-2])                     #own: output =  0            #PC = b                 new_list[-2] bezieht sich auf das zweitletzte Element der Liste ('b' in deinem Fall).
print(new_list[1:3])                    #own: output = a b c         #PC = b c              Startindex (1) = b  & Endindex (3). Das bedeutet, dass der Slice von new_list[1:3] das Element mit Index 1 ('b') und das Element mit Index 2 ('c') enthält, aber nicht das Element mit Index 3 (falls es existieren würde).
new_list[0] = 'z'                        
print(new_list)                         #own: output = z a b c       #PC = z b c            Durch new_list [0] = 'z' wird der vorehrgehende parameter a überschrieben und der ouput dadurch ist zbc 

my_list = [1,2,3]                        
bonus = my_list + [5]                    
my_list[0] = 'z'
print(my_list)                          #own: output = z 1 2 3       #PC = ['z', 2, 3]     Durch my_list[0] = 'z' wird der vorehrgehende parameter 1 überschrieben und der ouput dadurch ist z 1 2 3  weil anstelle 1 jezt z gesetzt wird
print(bonus)                            #own: output = 1 2 3 5       #PC = [1, 2, 3, 5]

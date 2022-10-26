# # print string in reverse

# import string


# star_str = ['S','T','A','R','S']

# # create the index list (start, stop(not included), inc/dec)
# #index = range(len(star_str)-1, -1, -1)
# #for pos in index:
# #    print(star_str[pos])
# #for item in star_str:
# #    print(item)

# # Capitalize letter 
# # Write code that takes a string as input and capitalize the first letter of each word. 
# # Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”

#str_input = input("Enter word please: ")
#cap = str_input.capitalize()
#word_count = str_input.count(str_input)
#print(word_count)
#space_count = str_input.count(' ')
#print(space_count)
#character_count = int(1)
##print(character_count)
#for item in range(space_count):
#     character_count = character_count + 1
#first_letter = []
#if item in range(str_input) != ' ':
#     first_letter


some_str = "Now is the time for all good people to come to the aid of their country."
new_str = ""
index = 0
for letter in some_str:
   # for each letter, examine the previous letter and if equals to a blank, capitalize myself
       # conditional 
           # 1) save the current letter for next "iteration"
           # 2) use the index some_str[index-1]
   # add the current letter to the new string
   # potential_letter = letter
    if some_str[index-1] == " ":

       new_str = new_str + some_str[index].upper()
    else:    
          new_str   = new_str + some_str[index]
    # new_str += potential_letter
    index += 1  
    print(some_str[index])  

    # Loops conditionals indexing capitalization


# "Now is the"

# | N | o | w | _ | i | s | _ |....
#   0   1   2   3   4   5   6   ...
#index = 4

#if some_str[index-1] == " ":
#    new_str = new_str + some_str[index].upper()
#else:
#    new_str = new_str + some_str[index]
#
#new_str = "No"
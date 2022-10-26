#  Write code that takes a string as input and capitalize the first letter of each word. 
    # provide string or take in string from user
    # evaluate the string to identify where the spaces are
    # cap the first letter after a space
# # Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”


#user_string = input("Enter string please: ")
#user_string = user_string.capitalize()
#index = 0
#capd_string = ""
#
#for letter in user_string:
#    if user_string[index-1] == ' ':
#        capd_string = capd_string + user_string[index].capitalize()
#    else:
#        capd_string = capd_string + user_string[index]
#    index +=1
#
#print(capd_string)

#Compress a string of characters
    # take in a string
    # identify how the string should be compressed
    # based on the information from the above, create a way to compress
#For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"
#use a loop to run through the characters in the string
#count the number of times a character is listed
#print the compressed string


str_to_comp = 'aaabbbbbccccaacccbbbaaabbbaaa'
index = 0
comp_str = ''
letter_num = 0
ready_to_comp = False
cnt = 0
for word in str_to_comp:
    letter_same = str_to_comp[index]
    prev_letter = str_to_comp[index-1]   
    if letter_same == prev_letter or letter_num == 0:
        index += 1
        letter_num += 1    
    else:
        comp_str = comp_str + str(letter_num) + str(prev_letter)
        letter_num = 0
    cnt += 1
print(comp_str)
#for word in str_to_comp:
#    print(letter_same)
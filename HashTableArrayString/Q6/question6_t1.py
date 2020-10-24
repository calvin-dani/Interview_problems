import parsecases as pc


string_list = ''


for test_c in pc.parsed:
    
    string_list += test_c

temp = None
solution =''
count = 1

for letter_ind in range(len(string_list)):

    if letter_ind == len(string_list)-1:
        solution += temp + str(count)+'\n'

    if temp == None:
        temp = string_list[letter_ind]
    elif temp != string_list[letter_ind]:
        solution += temp + str(count)
        temp = string_list[letter_ind]
        count = 1
    elif temp == string_list[letter_ind]:
        count += 1


if len(solution) > len(string_list):
    print(string_list)
else:
    print(solution)
        

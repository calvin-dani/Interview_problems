import parsecases as pc


string_1 = ''
string_2 = ''
string_list = list()

for test_c in pc.parsed:
    
    
    if len(test_c[0]) < len(test_c[1]):
        string_1 = test_c[0]
        string_2 = test_c[1]
    
    else:
        string_1 = test_c[1]
        string_2 = test_c[0]


letter_dict = dict()

for letter in string_2:
    if letter in letter_dict:
        letter_dict[letter] += 1
    else:
        letter_dict[letter] = 1
    
for letter in string_1:
    if letter in letter_dict:
        letter_dict[letter] -= 1
    else:
        print("Rotation it is not")
        quit()

print("Rotation it is")
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

letter_set = set()

for letter in string_1:
    for idx_2 in range(len(string_2)):
        if idx_2 not in letter_set and string_2[idx_2] == letter:
            letter_set.add(idx_2)
            break

if len(letter_set) == len(string_1):
    print("String rotation it is")

else:
    print(letter_set)
    print("String rotation it is not")

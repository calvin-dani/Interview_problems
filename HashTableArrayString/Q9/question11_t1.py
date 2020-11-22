import parsecases as pc


string_1 = ''
string_2 = ''
string_list = list()

for test_c in pc.parsed:  
    string_1 = test_c[0]
    string_2 = test_c[1]

count_str = 0

for idx in range(len(string_2)):
    if string_2[idx] == string_1[0]:
        for count in range(len(string_1)):
            if string_1[count] == string_2[(count + idx)%len(string_1)]:
                count_str += 1
                continue
            break
    if count_str == len(string_1):
        print("Is a rotation")
        quit()

print("Is not a rotation")





  
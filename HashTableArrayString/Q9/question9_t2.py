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

string_1 = list(string_1)
string_2 = list(string_2)
string_1.sort()
string_2.sort()
p = 0
p2 = 0

for letter in string_2:
    if letter == string_1[p]:
        p += 1

if p == len(string_1):
    print("Rotation it is")
else:
    print("Rotation it is not")
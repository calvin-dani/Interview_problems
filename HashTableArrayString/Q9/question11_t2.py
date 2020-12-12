import parsecases as pc


string_1 = ""
string_2 = ""


for test_c in pc.parsed:
    string_1 = test_c[0]
    string_2 = test_c[1]

count_str = 0


string_2 += string_2

if string_1 in string_2:
    print("Is a rotation")

else:
    print("Is not a rotation")

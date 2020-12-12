import parsecases as pc


string_1 = ""
string_2 = ""
string_list = list()

for test_c in pc.parsed:

    if len(test_c[0]) < len(test_c[1]):
        string_1 = test_c[0]
        string_2 = test_c[1]

    else:
        string_1 = test_c[1]
        string_2 = test_c[0]

    print(string_1, string_2)
    edit = 0
    p = 0

    if len(string_1) == len(string_2):
        for letter in string_2:
            if letter != string_1[p]:
                edit += 1

            p += 1

    else:
        for letter in string_2:
            if p == len(string_1):
                edit += 1
            else:
                if letter != string_1[p]:
                    edit += 1

                else:
                    p += 1

    print(edit < 2)
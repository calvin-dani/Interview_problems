import parsecases as pc


string_arr = list()
string_list = list()

for test_c in pc.parsed:
    print(test_c)
    string_arr.append(test_c)
    string_list = (string_arr[0].split())

print('%20'.join(string_list))

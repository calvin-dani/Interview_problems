import parsecases as pc


string_arr = list()
string_list = list()

for test_c in pc.parsed:
    print(test_c)
    string_arr.append(test_c)
    string_list = string_arr[0].strip()


ans = ""

for letter in string_list:
    if letter.isalpha():
        ans += letter
    else:
        ans += "%20"

print(ans)

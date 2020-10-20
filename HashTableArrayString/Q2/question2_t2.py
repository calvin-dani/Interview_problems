import parsecases as pc


string_arr = list()


for test_c in pc.parsed:
    print(test_c)
    string_arr.append(test_c)

s1 = list(string_arr[0])
s2 = list(string_arr[1])
s1.sort()
s2.sort()

if s1 == s2:
    print(s1)
    print("Is a combination")

else:
    print("is not a combination")
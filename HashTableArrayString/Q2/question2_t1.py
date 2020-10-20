import parsecases as pc


string_arr = list()
letter_set = set()

for test_c in pc.parsed:
    print(test_c)
    string_arr.append(test_c)

for letter in string_arr[0]:
    letter_set.add(letter)

for letter in string_arr[1]:
    if letter in letter_set:
        letter_set.remove(letter)

if len(letter_set):
    print("Not a combination")
else:
    print("Is a combination")

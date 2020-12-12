import parsecases as pc


string_arr = list()
letter_set = {}

for test_c in pc.parsed:
    print(test_c)
    string_arr.append(test_c)

for letter in string_arr[0]:
    if letter in letter_set:
        letter_set[letter] += 1
    else:
        letter_set[letter] = 1

for letter in string_arr[1]:
    if letter in letter_set:
        letter_set[letter] -= 1
        if letter_set[letter] == 0:
            del letter_set[letter]
    else:
        print("Not a combination")
        quit()

if len(letter_set):
    print("Not a combination")
else:
    print("Is a combination")

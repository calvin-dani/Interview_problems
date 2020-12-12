import parsecases as pc


string_list = ""
hashset = set()

for test_c in pc.parsed:
    print(test_c)
    string_list += test_c.lower()


for letter in string_list:
    if letter not in hashset and not letter.isspace():
        hashset.add(letter)
    elif letter in hashset:
        hashset.remove(letter)

if len(hashset) > 1:
    print("Not a pallindrome")

else:
    print("pallindrome combination possible")
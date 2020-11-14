import parsecases as pc
import BitVector

string_list = ''
bitVec = BitVector.BitVector(size= 127)
temp_set = 0

for test_c in pc.parsed:
    print(test_c)
    string_list += test_c.lower()

for letter in string_list:
    if not letter.isspace():
        temp_set = ord(letter)
        bitVec[temp_set] = bitVec[temp_set] ^ 1

count = 0
for bit in bitVec:
    if bit == 1:
        count += 1
    if count > 1:
        print("Not a permutation of palindrome")
        quit()
    
print("Is a permutation of a palindrome")

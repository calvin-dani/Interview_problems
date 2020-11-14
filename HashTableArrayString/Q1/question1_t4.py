import parsecases as pc
import BitVector


for test_c in pc.parsed:
    print(test_c)
    flag = 0
    bitVec = BitVector.BitVector(size= 127)
    for num in test_c:
        str_num = str(num)
        temp_set = ord(str_num)
        bitVec[temp_set] = bitVec[temp_set] ^ 1
        if bitVec[temp_set] == 1:
            continue
        else:
            print("Not Unique")
            flag = 1
    
    if flag == 0:
        print("Unique")
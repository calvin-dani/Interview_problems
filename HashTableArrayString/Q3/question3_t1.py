import parsecases as pc


string_arr = list()
string_list = list()

for test_c in pc.parsed:
    print(test_c)
    string_arr.append(test_c)
    string_list = list(string_arr[0])
      

p1 = len(string_list) - 1 
p2 = p1

whit_spc = '%20'

while p1 > -1:
    
    while(not string_list[p1].isalpha()):
        p1 -= 1
    
    while(string_list[p1].isalpha()):
        string_list[p2] = string_list[p1]
        p1 -= 1
        p2 -= 1
    
    for spc in whit_spc[::-1]:
        string_list[p2] = spc
        p2 -= 1
        

print(''.join(string_list))
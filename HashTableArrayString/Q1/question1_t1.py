import parsecases as pc



for test_c in pc.parsed:
    print(test_c)
    flag = 0
    for p1 in range(len(test_c)):
        p2 = p1 + 1
        while p2 < len(test_c):
            if test_c[p1] == test_c[p2]:
                print("Not unique")
                flag = 1 
                break
            p2 += 1
    
    if flag != 1:
        print("All numbers are unique")
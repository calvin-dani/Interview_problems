import parsecases as pc


for test_c in pc.parsed:
    print(test_c)
    flag = 0
    test_c.sort()
    for num_ind in range(len(test_c) - 1):
        if test_c[num_ind] == test_c[num_ind + 1]:
            print("Not unique")
            flag = 1
            break

    if flag != 1:
        print("Unique number")
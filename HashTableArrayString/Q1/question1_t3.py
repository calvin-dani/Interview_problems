import parsecases as pc


for test_c in pc.parsed:
    print(test_c)
    flag = 0
    hashtab = set()
    for num_ind in range(len(test_c) - 1):
        if test_c[num_ind] in hashtab:
            flag = 1
            print("not unique")
            break

        hashtab.add(test_c[num_ind])
    if flag != 1:
        print("Unique")

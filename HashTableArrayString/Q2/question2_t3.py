import parsecases as pc

string_arr = list()


for test_c in pc.parsed:
    print(test_c)
    string_arr.append(test_c)

sentence_one = string_arr[0]
sentence_two = string_arr[1]

all_permutation_set = set()


def permutation_of_string(base_string, permutated_string,all_permutation_set):
    if(len(base_string)==0):
        return all_permutation_set.add(permutated_string)
    else:
        for letter_index in range(len(base_string)):
            prefix_splice = base_string[0:letter_index]
            suffix_splice = ""
            if(letter_index < len(base_string)):
                suffix_splice = base_string[letter_index+1:len(base_string)] 
            
            spliced_string = prefix_splice + suffix_splice
            permutated_string_builder = permutated_string + base_string[letter_index]
            permutation_of_string(spliced_string,permutated_string_builder,all_permutation_set)
        return all_permutation_set

def check_is_permutation(sentence, permutation_set):
    if sentence in permutation_set:
        print("Is a combination")
    else:
        print("is not a combination")


all_permutation_set = permutation_of_string(sentence_one,"",all_permutation_set)
check_is_permutation(sentence_two,all_permutation_set)
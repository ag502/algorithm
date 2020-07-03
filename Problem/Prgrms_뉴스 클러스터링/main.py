def make_string_set(string):
    string_set = {}
    for ch1, ch2 in zip(string, string[1:]):
        ch1 = ch1.lower()
        ch2 = ch2.lower()
        if ch1 != '' and ch2 != '' and 'a' <= ch1 <= 'z' and 'a' <= ch2 <= 'z':
            if ch1 + ch2 in string_set:
                string_set[ch1 + ch2] += 1
            else:
                string_set[ch1 + ch2] = 1
    return string_set

def intersection(set1, set2):
    if len(set1) == 0 and len(set2) == 0:
        return 1
    num_of_intersection = 0
    for string in set1:
        if string in set2:
            num_of_intersection += min(set1[string], set2[string])
    return num_of_intersection

def union(set1, set2):
    if len(set1) == 0 and len(set2) == 0:
        return 1
    num_of_union = 0
    for string in set1:
        if string in set2:
            num_of_union += max(set1[string], set2[string])
        else:
            num_of_union += set1[string]

    for string in set2:
        if string not in set1:
            num_of_union += set2[string]

    return num_of_union

def solution(str1, str2):
    str1_set = make_string_set(str1)
    str2_set = make_string_set(str2)
    answer = int((intersection(str1_set, str2_set) / union(str1_set, str2_set)) * 65536)
    return answer
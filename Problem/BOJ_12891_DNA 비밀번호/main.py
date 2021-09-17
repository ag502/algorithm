from sys import stdin

base = ['A', 'C', 'G', 'T']

def is_password(temp_base, standard_base):
    for base, count in standard_base:
        if temp_base[base] < count:
            return False
    return True

def main():
    stdin = open('Problem\BOJ_12891_DNA 비밀번호\input.txt', 'r')
    length_of_dna, length_of_password = map(int, stdin.readline().split())
    dna = stdin.readline().rstrip()
    min_base_number = list(map(int, stdin.readline().split(' ')))
    standard_base = list(zip(base, min_base_number))
    
    answer = 0
    temp_base = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for i in range(length_of_password):
        temp_base[dna[i]] += 1
    
    if is_password(temp_base, standard_base):
        answer += 1
        
    for i in range(length_of_dna - length_of_password):
        temp_base[dna[i]] -= 1
        temp_base[dna[i + length_of_password]] += 1
        
        if is_password(temp_base, standard_base):
            answer += 1
            
    print(answer)
    
if __name__ == "__main__":
    main()
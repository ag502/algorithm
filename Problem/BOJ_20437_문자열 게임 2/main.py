from sys import maxsize, stdin

def main():
    stdin = open('Problem\BOJ_20437_문자열 게임 2\input.txt', 'r')
    test_case = int(stdin.readline())
    
    for _ in range(test_case):
        string = stdin.readline().rstrip()
        k = int(stdin.readline())
        
        shortest_string_len = maxsize
        longest_string_len = -maxsize
        
        standard_char = {}
        for idx, char in enumerate(list(string)):
            if char not in standard_char:
                standard_char[char] = []
            standard_char[char].append(idx)
        for char, index_list in standard_char.items():
            if len(index_list) >= k:
                for i in range(len(index_list) - k + 1):
                    shortest_string_len = min(shortest_string_len, index_list[i + k - 1] - index_list[i] + 1)
                    longest_string_len = max(longest_string_len, index_list[i + k - 1] - index_list[i] + 1)

        if shortest_string_len == maxsize or longest_string_len == -maxsize:
            print(-1)
        else:
            print('{} {}'.format(shortest_string_len, longest_string_len))
        
if __name__ == "__main__":
    main()
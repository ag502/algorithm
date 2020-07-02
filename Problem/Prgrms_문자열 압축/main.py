def compress_string(s, compress_unit=1):
    unit_char = s[:compress_unit]
    repeat_num = 1
    compressed_string = ''

    if len(s) == 1:
        return s

    for i in range(1, len(s), compress_unit):
        if unit_char == s[i:i + compress_unit]:
            repeat_num += 1
        elif unit_char != s[i:i + compress_unit]:
            compressed_string += (unit_char if repeat_num == 1 else str(repeat_num) + unit_char)
            unit_char = s[i:i + compress_unit]
            repeat_num = 1
        elif i + compress_unit >= len(s):
            compressed_string += (unit_char if repeat_num == 1 else str(repeat_num) + unit_char)
    return compressed_string

def solution(s):
    answer = 1001
    if len(s) == 1:
        return len(compress_string(s))
    for i in range(1, len(s)):
        compressed_string = compress_string(s, i)
        answer = min(answer, compressed_string)
    return answer

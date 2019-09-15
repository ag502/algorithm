def min_fee(pages_to_print):
    pages_to_print.sort()
    current_late_fee = 0
    total_late_fee = 0
    for page in pages_to_print:
        current_late_fee += page
        total_late_fee += current_late_fee
    return total_late_fee

    
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
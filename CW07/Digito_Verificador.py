def calculate_check_digit(role_id):
    id_str = str(role_id)
    
    # 2. Reverse the number
    reversed_id = id_str[::-1]
    

    sequence = [2, 3, 4, 5, 6, 7]
    total_sum = 0
    
    for i, digit in enumerate(reversed_id):
        # The % operator helps loop the sequence if we run out of numbers
        multiplier = sequence[i % len(sequence)]
        total_sum += int(digit) * multiplier
        
    remainder = total_sum % 11

    check_digit = 11 - remainder
    
    if check_digit == 11:
        check_digit = 0
    elif check_digit == 10:
        check_digit = 'K'
        
    return f"{role_id}-{check_digit}"

test_number = "201012341"
result = calculate_check_digit(test_number)
print(f"The full role ID is: {result}")
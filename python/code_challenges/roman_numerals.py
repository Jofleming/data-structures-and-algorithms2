
def total_roman_numeral(numeral_string):
    roman_numbers = {
        'I': 1, 'V': 5, 
        'X': 10, 'L': 50, 
        'C': 100, 'D': 500,
        'M': 1000,
    }
    total = 0

    for i in range(len(numeral_string)):
        if not numeral_string[i + 1]:
            total += roman_numbers[numeral_string[i]]

        elif roman_numbers[numeral_string[i]] < roman_numbers[numeral_string[i + 1]]:
            total -= roman_numbers[numeral_string[i]]

        elif roman_numbers[numeral_string[i]] >= roman_numbers[numeral_string[i + 1]]:
            total += roman_numbers[numeral_string[i]]

    return total

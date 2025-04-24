def sum_even_digits(number):
    number = abs(number)
    
    if number == 0:
        return 0
    
    last_digit = number % 10
    rest_sum = sum_even_digits(number // 10)
    
    if last_digit % 2 == 0:
        return rest_sum + last_digit
    return rest_sum


def count_vowel_triplets(text):
    text = text.lower()
    vowels = "aeiouy"
    count = 0

    for i in range(len(text) - 2):
        if text[i] in vowels and text[i + 1] in vowels and text[i + 2] in vowels:
            count += 1
    
    return count


def find_fibonacci_index(number):
    if number < 1:
        return -1

    a, b = 1, 1
    index = 2 if number > 1 else 1

    if number == 1:
        return 1

    while b < number:
        a, b = b, a + b
        index += 1
        if b == number:
            return index

    return -1


def remove_duplicates(string):
    if string == "":
        return ""
    if len(string) == 1:
        return string

    if string[0] == string[1]:
        return remove_duplicates(string[1:])
    return string[0] + remove_duplicates(string[1:])
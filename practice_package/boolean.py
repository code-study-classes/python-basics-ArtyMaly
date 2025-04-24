def check_between_numbers(A, B, C):
    return (A < B < C) or (C < B < A)


def check_odd_three(number):
    abs_number = abs(number)
    return 100 <= abs_number <= 999 and (abs_number % 2 != 0)


def check_unique_digits(number):
    abs_number = abs(number)
    num_str = str(abs_number)
    return 100 <= abs_number <= 999 and len(set(num_str)) == 3


def check_palindrome_number(number):
    num_str = str(abs(number))
    return num_str == num_str[::-1]


def check_ascending_digits(number):
    abs_number = abs(number)
    num_str = str(abs_number)
    return 100 <= abs_number <= 999 and num_str[0] < num_str[1] < num_str[2]
def calculate_distance(x, y):
    return abs(x - y)


def calculate_segments(a, b):
    return a // b


def calculate_digit_sum(number):
    return sum(int(digit) for digit in str(abs(number)))


def calculate_rect_area(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    return float(width * height)


def round_to_multiple(number, multiple):
    return multiple * round(number / multiple)
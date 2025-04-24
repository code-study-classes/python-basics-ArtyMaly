def is_weekend(day):
    return day in (6, 7)


def get_discount(amount):
    if amount >= 5000:
        return round(amount * 0.1, 2)
    elif amount >= 1000:
        return round(amount * 0.05, 2)
    return 0


def describe_number(n):
    parity = "четное" if n % 2 == 0 else "нечетное"
    
    digit_word = {
        1: "однозначное",
        2: "двузначное",
        3: "трехзначное"
    }.get(len(str(n)), "неизвестность")
    
    return f"{parity} {digit_word} число"


def convert_to_meters(unitNumber, lengthInUnits):
    factors = {
        1: 0.1,
        2: 1000,
        3: 1,
        4: 0.001,
        5: 0.01
    }
    return lengthInUnits * factors.get(unitNumber, 0)


def describe_age(age):
    tens = age // 10
    ones = age % 10

    tens_word = {
        2: "двадцать",
        3: "тридцать",
        4: "сорок",
        5: "пятьдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "восемьдесят",
        9: "девяносто"
    }.get(tens, "") if tens < 10 else ("сто" if age == 100 else "")

    ones_word = {
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять"
    }.get(ones, "")

    num_word = f"{tens_word} {ones_word}".strip()

    if 11 <= age % 100 <= 14:
        suffix = "лет"
    else:
        suffix = {
            1: "год",
            2: "года",
            3: "года",
            4: "года"
        }.get(ones, "лет")

    return f"{num_word} {suffix}"
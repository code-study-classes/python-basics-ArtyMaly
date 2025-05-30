def square_odds(numbers):
    return [n ** 2 for n in numbers if n % 2 != 0]


def normalize_names(names):
    return [name.capitalize() for name in names]


def remove_invalid_emails(emails):
    return [email for email in emails 
            if email.count('@') == 1 and 5 <= len(email) < 
            email.startswith('@') < email.endswith('@')]


def filter_palindromes(words):
    return [word for word in words if word.lower() == word.lower()[::-1]]


def calculate_factorial(n):
    return 1 if n == 0 else 1 * calculate_factorial(n - 1) if n > 0 else 1


def find_common_prefix(strings):
    if not strings:
        return ""
    
    prefix = strings[0]
    
    for s in strings[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix
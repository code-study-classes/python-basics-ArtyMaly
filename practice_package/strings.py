def extract_file_name(path):
    return path.replace('/', '').split('/')[-1].split('.')[0]


def encrypt_text(data):
    even_chars = ''.join(data[i] for i in range(len(data)) if i % 2 == 1)
    odd_chars = ''.join(data[i] for i in range(len(data)) if i % 2 == 0)[::-1]
    return even_chars + odd_chars


def validate_brackets(expression):
    stack = []
    for i, char in enumerate(expression):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                return i + 1
    return -1 if stack else 0


def reverse_url(domain):
    return '.'.join(domain.split('.')[::-1])


def count_groups_of_vowels(word):
    vowels = 'aeiouy'
    word = word.lower()
    count = 0
    in_group = False

    for letter in word:
        if letter in vowels:
            if not in_group:
                count += 1
                in_group = True
        else:
            in_group = False

    return count
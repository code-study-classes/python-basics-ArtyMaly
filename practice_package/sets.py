def get_common_elements(set1, set2):
    return {item for item in set1 if item in set2}


def check_superset(set_a, set_b):
    return all(item in set_a for item in set_b)


def eliminate_duplicates(items):
    return list(dict.fromkeys(items))


def count_distinct_words(text):
    words = text.lower().split()
    return len(set(words))


def get_intersection_of_sets(*sets):
    if not sets:
        return set()
    
    intersection = sets[0]
    
    for s in sets[1:]:
        intersection.intersection_update(s)
    
    return intersection
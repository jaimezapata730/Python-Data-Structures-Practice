# def multiple_letter_count(phrase):
#     """Return dict of {ltr: frequency} from phrase.

#         >>> multiple_letter_count('yay')
#         {'y': 2, 'a': 1}

#         >>> multiple_letter_count('Yay')
#         {'Y': 1, 'a': 1, 'y': 1}
#     """

def multiple_letter_count(phrase):
    storage = {}
    for ltr in phrase:
        storage[ltr] = storage.get(ltr,0) + 1

    return storage
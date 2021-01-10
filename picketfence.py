#!/usr/bin/python3

""" Take (or prompt for) a string of text to encypher, picketfence-style. Hint given."""

import random
import sys


def randomize_alpha(alpha):
    """Build a random equivalent of the alpha string.
       Try to avoid matching passthroughs--a few times.
       Warn the user if we failed every attempt."""
    tries = 0
    matching = True
    while matching:
        tries += 1
        usort = random.sample(alpha, len(alpha))
        matching = False
        for index in range(len(alpha)):
            if alpha[index] == usort[index]:
                matching = True
        if tries >= 10:
            break
    if tries > 1:
        if matching:
            print("tries:", tries, "warning: not such a good random list")
        else:
            print("tries:", tries)
    return usort


def create_substitution_box(usort, alpha):
    """Create a dictonary of letters to substitute  for the letters."""
    # initial vector. Allow common punctuation to pass through
    sbox = {' ': ' ', '.': '.', '\'': '\'', '"': '"', '!': '!', '?': '?'}
    # append the random into the s-box
    fence = ""
    for index in range(len(alpha)):
        fence += usort[index]
        sbox[alpha[index]] = usort[index]
    return sbox


def get_text():
    """Get something to encypher either from the command line,
       meaning, easily used in a filter, or by prompting the user.
       Case is needs to be unimportant, so fold to lowercase."""
    if len(sys.argv) <= 1:
        mixedplaintext = str(input("enter a string: "))
    else:
        args = sys.argv
        args.reverse()
        args.pop()
        args.reverse()
        mixedplaintext = ""
        for arg in args:
            if len(mixedplaintext) > 1:
                mixedplaintext += " "+str(arg)
            else:
                mixedplaintext = str(arg)
    return(mixedplaintext.lower())


def encypher(sbox, plaintext):
    """Generate a cypher by substituting every char in the plain text.
       If we can't substitute, then just pass through."""
    cypher = ""
    for each in plaintext:
        try:
            cypher += sbox[each]
        except KeyError:
            cypher += each
    return cypher


def test_encypher():
    test_sbox = {'a': 'x', 'b': 'y', 'c': 'z'}
    test_plaintext = "abc123"
    test_expected = "xyz123"
    test_actual = encypher(test_sbox, test_plaintext)
    assert test_expected == test_actual


def frequency_count(text, alpha):
    """Hints depend on the letter histogram. But the stats needs to exist."""
    stats = {'dummy': 0}
    for letter in text:
        try:
            count = stats[letter]
        except KeyError:
            # why is there no entry in stats for this letter?
            count = 0
        # only bump alpha counts, not punctuation, etcetera
        if letter in alpha:
            count += 1
        stats[letter] = count
    del stats['dummy']
    return stats


def test_frequency_count():
    test_text = "azbb"
    test_alfa = ['a', 'b']
    expected_stats = {'a': 1, 'z': 0, 'b': 2}
    print("expect stats", expected_stats)
    actual_stats = frequency_count(test_text, test_alfa)
    print("actual stats", actual_stats)
    assert expected_stats == actual_stats


def remove_letter(letter, stats):
    """ Remove a letter (and therefore, count) permenently from stats."""
    # careful with references, shallow and deep copies
    if letter in stats:
        del stats[letter]
    return stats


def test_remove_letter():
    test_stats = {'a': 1, 'z': 7, 'b': 2}
    expected_stats = {'a': 1, 'b': 2}
    # does exist
    actual_stats = remove_letter('z', test_stats)
    assert expected_stats == actual_stats
    # doesn't exist
    actual_stats = remove_letter('k', test_stats)
    assert expected_stats == actual_stats


def remove_vowels(stats):
    for vowel in "aeiou":
        remove_letter(vowel, stats)
    return stats


def test_remove_vowels():
    test_stats = {'a': 1, 'z': 7, 'b': 2}
    expected_stats = {'z': 7, 'b': 2}
    # print("expected", expected_stats)
    actual_stats = remove_vowels(test_stats)
    # print("actual", actual_stats)
    assert expected_stats == actual_stats


def find_hint(plain, stats):
    """Search the stats for letter with the most number of occurances.
    Two catches: we can't use a vowel, and we have to return something."""
    hint_key = ''
    hint_count = -1
    remove_vowels(stats)
    # basically, offer the highest counted letter as a hint
    for hint in stats:
        if stats[hint] > hint_count:
            hint_count = stats[hint]
            hint_key = hint
    return hint_key


def test_find_hint():
    """Should ignore the vowel a and find b"""
    test_plain = "azb"
    test_stats = {'a': 9, 'z': 7, 'b': 8}
    expected_hint = 'b'
    print("expected_hint", expected_hint)
    actual_hint = find_hint(test_plain, test_stats)
    print("actual_hint", actual_hint)
    assert expected_hint == actual_hint


def make_hint(plain, sub_box, stats):
    hint = find_hint(plain, stats)
    return(hint, sub_box[hint])


def test_make_hint():
    test_plain = "azb"
    test_stats = {'a': 9, 'z': 7, 'b': 8}
    expected_hint = 'b'
    # print("expected_hint", expected_hint)
    test_sbox = {'a': 'x', 'b': 'y', 'c': 'z'}
    expected_use = 'y'
    # print("expected_use", expected_use)
    (actual_hint, actual_use) = make_hint(test_plain, test_sbox, test_stats)
    # print("actual_hint", actual_hint, "actual_use", actual_use)
    assert expected_hint == actual_hint
    assert expected_use == actual_use


def cypher(alpha):
    """ encypher a string from the command line or prompt.
    Build a list of count statistics as we go over the alpha."""
    unsorted = randomize_alpha(alpha)
    sub_box = create_substitution_box(unsorted, alpha)
    plain = get_text()
    stats = frequency_count(plain, alpha)
    encyphered = encypher(sub_box, plain)
    (hint_for, hint_use) = make_hint(plain, sub_box, stats)
    # results
    print("plain text :", plain)
    print("Subsitution:", sub_box)
    print("cypher text:", encyphered)
    print("Hint       : for", hint_for, "use", hint_use)


if __name__ == '__main__':
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cypher(alphabet)

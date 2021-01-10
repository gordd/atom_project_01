#!/usr/bin/python3

""" Take (or prompt for) a string of text to encypher, picketfence-style. Hint given."""

import random
import sys


def randomize_alpha(alpha):
    """Build a random equivalent of the alpha string.
       Try to avoid passthroughs--a few times.
       Warn the user if we failed every attempt."""
    tries = 0
    matching = True
    while matching:
        tries += 1
        usort = random.sample(alpha, 26)
        matching = False
        for index in range(26):
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


def create_substitution_box(usort):
    """Create a dictonary of letters to substitute  for the letters."""
    # initial vector. Allow common punctuation to pass through
    sbox = {' ': ' ', '.': '.', '\'': '\'', '"': '"', '!': '!'}
    # append the random into the s-box
    fence = ""
    for index in range(26):
        fence += usort[index]
        sbox[alpha[index]] = usort[index]
    print("Subsitution:", fence)
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


def frequency_count(text):
    """Hints depend on the letter histogram. But the stats needs to exist."""
    stats = {'dummy': 0}
    for letter in text:
        try:
            count = stats[letter]
        except Exception:
            # why is there no entry in stats for this letter?
            count = 0
        # only bump alpha counts, not punctuation, etcetera
        if letter in alpha:
            count += 1
        stats[letter] = count
    del stats['dummy']
    return stats


def remove_letter(letter, stats):
    """ Remove a letter (and therefore, count) permenently from stats."""
    if letter in stats:
        del stats[letter]


def remove_vowels(stats):
    for vowel in "aeiou":
        remove_letter(vowel, stats)


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


def make_hint(plain, sub_box, stats):
    hint = find_hint(plain, stats)
    return(hint, sub_box[hint])


def cypher():
    """ encypher a string from the command line or prompt.
    Build a list of count statistics as we go over the alpha."""
    unsorted = randomize_alpha(alpha)
    sub_box = create_substitution_box(unsorted)
    plain = get_text()
    stats = frequency_count(plain)
    encyphered = encypher(sub_box, plain)
    (hint_for, hint_use) = make_hint(plain, sub_box, stats)
    # results
    print("plain text :", plain)
    print("cypher text:", encyphered)
    print("Hint       : for", hint_for, ", use", hint_use)


if __name__ == '__main__':
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cypher()

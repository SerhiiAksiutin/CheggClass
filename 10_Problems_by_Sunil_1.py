""""
- [1] Print duplicate characters from string. Example:
    * If provide String as "Java" output should be 'a'
    * If provide String as "Hello" output should be 'l'
"""


def dupChar(w):
    n = 1
    for v in w.lower():
        if v in w[n:]:
            return v
            n += 1
        else:
            n += 1

print dupChar("Apple")

"""
- [2] Program to print first non-repeated character from string? Example:
    * If given string "Morning" then it should print "M"
"""


def nonRep(w1):
    n1 = 1
    w1 = w1.lower()
    for v in w1:
        if v not in w1[n1:] and v not in w1[:n1 - 1]:
            return v
            n1 += 1
        else:
            n1 += 1

print nonRep('MorningM')

"""
- [3] Reverse the string. Example
    * "hello" to "olleh"
"""


def revStr(w2):
    n = ''
    for v in range(len(w2) + 1):
        if v == 0:
            pass
        else:
            n += w2[-v]
    return n


print revStr('Hello')

"""

- [4] Check if string contain any digit. Example:
    * "hell7t" contain 7 or "hello" doesn't contain any digit
"""


def intCheck(w3):
    for v in w3:
        try:
            int(v)
            return v
        except:
            pass
    return "No digits found"


print intCheck('Hell7')

"""
- [5] Find duplicates in string. Example:
    * "Programming" contain g: 2, r:2 and m:2
"""


def dupLett(w4):
    c = dict()
    n = 0
    for v in w4:
        n += 1
        if v in w4[n:]:
            c[v] = 2
    return c

print dupLett('Programmming')

"""
- [6] Count number of vowels and consonants in a String.
    * If Input is "Java" then program should print " 2 vowels and 2 consonants"
"""


def counSoun(w5):
    all_vowels = ['a', 'e', 'i', 'o', 'u']
    vowels = 0
    consonants = 0
    for v in w5:
        if v in all_vowels:
            vowels += 1
        else:
            consonants += 1
    return "%s vowels and %s consonants" % (vowels, consonants)

print counSoun("Javayofd")

"""
- [7] Could occurrence of given character. Example:
    * If input string is "java" and given character is 'a' then
    it should return 2
"""


def counOccur(w6, character):
    n = 0
    for v in w6.lower():
        if v == character:
            n += 1
    return n


print counOccur("java", 'a')

"""
- [8] Replace each given character to other. Example:
    * If input is "Python is great" and asked to replace space with "%20" then
    it should return "Python%20is%20great"
"""


def replaceer(w7, x):
    y = ""
    for v in w7:
        if v in w7 and v != " ":
            y += v
        else:
            y += x

    return y

print replaceer('Python is great', '%20')

"""
- [9] Return highest occurred character in string. Example:
    * "aaaaaaaaaaaaaaaabbcdddddddddeeeeeee" should return "a"
"""


def highestCher(w8):
    x = dict()
    for v in w8:
        x[v] = 0
    for v in range(len(w8)):
        x[w8[v]] += 1

    return max(x.values())


print highestCher('aaabbbbbbbbbbbbbbbbbbbc')

"""
- [10] Remove a given character from string. Example:
    * "Python" need to remove "y" so output should be "Pthon"
"""


def remChar(w9, character1):
    t = ""
    for v in w9.lower():
        if v != character1:
            t += v
    return t

print remChar("Python", 'p')

"""
- [11] Find anagrams of each other in String. Example:
    * "Army" and "Mary" are anagram of each other. (little info: Two string are
    anagrams if they are written using the same exact letters, ignoring space,
    punctuation and capitalization. Each letter should have same count in both
    strings)
"""


def anagrams(w10, w11):
    for v in w10.lower():
        if v not in w11.lower():
            return "%s and %s are not anagrams of each other" % (w10, w11)
        else:
            return "%s and %s are anagrams of each other" % (w10, w11)

print anagrams("Tom Marvolo Riddle", "I am Lord Voldemort")

### Thomas Silva
### ENGR 103 Assignment 8b.
### Nov 22, 2023.


def words_in_both(str1, str2):
    words1 = set(str1.lower().split())
    words2 = set(str2.lower().split())

    common_words = words1.intersection(words2)

    return common_words

string1 = "She is a jack of all trades"
string2 = "Jack was tallest of all"
result = words_in_both(string1, string2)
print(result)

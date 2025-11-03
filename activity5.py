words_file = open('CROSSWD.txt', 'r')
for i in words_file:
    print(i.strip())


def more_than_20(file):
    open_file = open(file)
    ret_list = []
    for i in open_file:
        x = i.strip()
        if len(x) > 20:
            ret_list.append(x)
    return ret_list


def has_no_e(word):
    return "e" not in word.lower()

def uses_only(word, letters):
    for char in word:
        if char not in letters:
            return False
    return True

def all_uses_only(file, letters):
    valid_words = []
    with open(file, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                if uses_only(word.lower(), letters.lower()):
                    valid_words.append(word)
    return valid_words

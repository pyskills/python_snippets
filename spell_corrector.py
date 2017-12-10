import re, collections


def get_words(text):
    return re.findall('[a-z]+', text.lower())


def langModel(wordseq):
    wordCount = collections.defaultdict(lambda: 1)
    for word in wordseq:
        wordCount[word] += 1
    return wordCount


dictionary = langModel(get_words(
    open('shakespeare.txt').read()))  # all the words in the language model. you cant get and download this easily
alphabet = 'abcdefghijklmnopqrstuvwxyz'


def dist1_words(word):
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]  # n deletions
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]  # n-1 transpositions
    replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]  # 26n alterations
    inserts = [a + c + b for a, b in splits for c in alphabet]  # 26(n+1) insertions
    return set(deletes + transposes + replaces + inserts)


def dist2_words(word):
    return set(word2 for word1 in dist1_words(word) for word2 in dist1_words(word1))


def legal_words(words):
    return set(w for w in words if w in dictionary)


def correct_word(word):
    possibleWords = legal_words([word]) or legal_words(dist1_words(word)) or legal_words(dist2_words(word)) or [word]
    return max(possibleWords, key=dictionary.get)


def correct_words(sentence):
    words = get_words(sentence)
    return ' '.join(correct_word(word) for word in words)


if __name__ == '__main__':
    # test samples
    print(correct_word("spell"))
    print(correct_word("spel"))
    print(correct_word("checke"))
    print(correct_word("checer"))
    print(correct_words("teis is a simpl spel corrector"))

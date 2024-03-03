def findSubstring(s: str, words: list[str]) -> list[int]:
    if len(s) == 0 or s is None or words is None:
        return []

    word_freq = {x: words.count(x) for x in words}
    word_len = len(words[0])
    wordsLen = len(words) * word_len
    result = []
    words_seen = {}

    for l in range(len(s) - wordsLen + 1):
        words_seen.clear()

        for r in range(len(words)):
            word_ind = l + r * word_len
            temp_word = s[word_ind:word_ind + word_len]

            if temp_word not in word_freq:
                break

            words_seen[temp_word] = words_seen.get(temp_word, 0) + 1

            if words_seen[temp_word] > word_freq[temp_word]:
                break

        if words_seen == word_freq:
            result.append(l)

    return result


s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "word"]
s = "barfoothefoobarman"
words = ["foo", "bar"]

print(findSubstring(s, words))


# barfoothefoo barman = len(s)
#              foobar = wordsLen

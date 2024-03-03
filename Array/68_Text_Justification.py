def fullJustify(words: list[str], maxWidth: int) -> list[str]:
    words_lst = [(word, len(word)) for word in words]
    N = len(words)
    l, r = 0, 0
    res = []
    while True:
        width = 0
        initial = -1
        while width <= maxWidth and r <= N-1:
            initial = 0 if initial == -1 else 1
            width += words_lst[r][1]+initial
            r += 1

        if width > maxWidth:
            string = create_str(words_lst[l:r-1], maxWidth)
            r -= 1
            l = r
            res.append(string)
        elif r > N-1:
            string = create_last(words_lst[l:N], maxWidth)
            res.append(string)
            break
    return res


def create_str(words_lst: list[tuple], maxWidth: int) -> str:
    n = len(words_lst)
    if n == 1:
        return words_lst[0][0].ljust(maxWidth, ' ')

    spaces = maxWidth - sum((word[1] for word in words_lst))
    div, ost = divmod(spaces, n-1)
    string = [''] * n
    for i in range(n):
        delta = 1 if ost >= 1 else 0
        string[i] = (words_lst[i][0] + ' ' * (div+delta)
                     ) if i < n-1 else words_lst[i][0]

        ost -= 1
    return ''.join(string)


def create_last(words_lst: list[tuple], maxWidth: int) -> str:
    n = len(words_lst)
    string = [words_lst[i][0] + ' ' if i < n-1 else words_lst[i][0]
              for i in range(len(words_lst))]

    return ''.join(string).ljust(maxWidth, ' ')


words = ["Science", "is", "what", "we", "understand", "well", "enough", "to",
         "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
maxWidth = 20
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
words = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth = 16

words = ["Science", "is", "what", "we", "understand", "well", "enough", "to",
         "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
maxWidth = 20

for row in fullJustify(words, maxWidth):
    print(row)

"""
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

"""

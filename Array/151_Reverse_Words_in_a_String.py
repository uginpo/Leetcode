def reverseWords(s: str) -> str:
    return ' '.join(s.strip().split()[::-1])


s = "a good   example   "
print(f'{reverseWords(s)=}')

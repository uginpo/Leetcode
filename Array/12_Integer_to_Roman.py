def intToRoman(num: int) -> str:

    integers = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    roman = []
    for key, value in integers.items():
        count, num = divmod(num, key)
        if count:
            roman.append(integers[key]*count)

    return ''.join(roman)


num = 1994

print(intToRoman(num))

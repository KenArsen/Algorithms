"""
I — означает «один» (1)
V — означает «пять» (5)
X — означает «десять» (10)
L — означает «пятьдесят» (50)
C — означает «сто» (100)
D — означает «пятьсот» (500)
M — означает «тысяча» (1000)

Для записи чисел в римской системе используются два правила:
    каждый меньший знак, поставленный слева от большего, вычитается из него;
    каждый меньший знак, поставленный справа от большего, прибавляется к нему.
число 49 в римской системе счисления имеет вид XLIX = (50−10)+(10−1)=40+9(две группы первого вида)
число 444 в римской системе счисления будет записано в виде CDXLIV=(500−100)+(50−10)+(5−1)=400+40+4
(три группы второго вида).
"""


def roman_to_int(roman):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(roman):
        value = roman_numerals[char]

        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value

    return total


def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num


print(int_to_roman(49))  # XLIX
print(roman_to_int("XLIX"))   # 49



"""
Consider all integer combinations of ab for 2 <= a <= 5 and 2 <= b <= 5:

2^2=4,  2^3=8,   2^4=16,  2^5=32
3^2=9,  3^3=27,  3^4=81,  3^5=243
4^2=16, 4^3=64,  4^4=256, 4^5=1024
5^2=25, 5^3=125, 5^4=625, 5^5=3125

If they are then placed in numerical order, with any repeats removed, we get
the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by ab
for 2 <= a <= 100 and 2 <= b <= 100?
"""


def solution(n: int = 100) -> int:
    """Returns the number of distinct terms in the sequence generated by a^b
    for 2 <= a <= 100 and 2 <= b <= 100.

    >>> solution(100)
    9183
    >>> solution(50)
    2184
    >>> solution(20)
    324
    >>> solution(5)
    15
    >>> solution(2)
    1
    >>> solution(1)
    0
    """
    collect_powers = set()

    current_pow = 0

    n += 1

    for a in range(2, n):
        for b in range(2, n):
            current_pow = a**b  # calculates the current power
            collect_powers.add(current_pow)  # adds the result to the set
    return len(collect_powers)


if __name__ == "__main__":
    print("Number of terms ", solution(int(str(input()).strip())))

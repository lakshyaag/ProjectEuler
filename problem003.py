"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the given number?

largestPrimeFactor(2) should return 2.
largestPrimeFactor(3) should return 3.
largestPrimeFactor(5) should return 5.
largestPrimeFactor(7) should return 7.
largestPrimeFactor(13195) should return 29.
largestPrimeFactor(600851475143) should return 6857.
"""


def largestPrimeFactor(number):
    prime = 2
    max = 1
    while prime <= number:
        if number % prime == 0:
            max = prime
            number = number / prime
        else:
            prime = prime + 1

    return print(max)


largestPrimeFactor(2)
largestPrimeFactor(3)
largestPrimeFactor(5)
largestPrimeFactor(7)
largestPrimeFactor(13195)
largestPrimeFactor(600851475143)

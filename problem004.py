"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two n-digit numbers.

largestPalindromeProduct(2) should return 9009.
largestPalindromeProduct(3) should return 906609.
"""


def largestPalindromeProduct(n):
    max_palindrome = 0
    lower_limit = pow(10, n - 1)
    upper_limit = pow(10, n) - 1

    for a in range(upper_limit, lower_limit, -1):
        for b in range(upper_limit - 1, lower_limit, -1):
            product = (a * b)
            if product > max_palindrome and str(product) == str(product)[::-1]:
                max_palindrome = product
                break

    return print(max_palindrome)


largestPalindromeProduct(2)
largestPalindromeProduct(3)
largestPalindromeProduct(4)

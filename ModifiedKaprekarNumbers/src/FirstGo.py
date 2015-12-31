'''
Solving the Modified Kaprekar Numbers puzzle on hackerrank.

https://www.hackerrank.com/challenges/kaprekar-numbers

Note, the problem is ambiguous. d is the number of digits in the original
number, the test is that the sum of r, the digits up to d, and l, the 
remaining digits, add up to the original number.

Bizarre, and not really the Kaprekar numbers at all. Poorly worded description.

--------------------

Problem Statement

A modified Kaprekar number is a positive whole number n with d digits, such that when we split its square into two pieces - a right hand piece r with d digits and a left hand piece l that contains the remaining d or d-1 digits, the sum of the pieces is equal to the original number (i.e. l + r = n).

Note: r may have leading zeros.

Here's an explanation from Wikipedia about the ORIGINAL Kaprekar Number (spot the difference!): In mathematics, a Kaprekar number for a given base is a non-negative integer, the representation of whose square in that base can be split into two parts that add up to the original number again. For instance, 45 is a Kaprekar number, because 45**2 = 2025 and 20+25 = 45.

The Task 
You are given the two positive integers p and q, where p is lower than q. Write a program to determine how many Kaprekar numbers are there in the range between p and q (both inclusive) and display them all.

Input Format

There will be two lines of input: p, lowest value q, highest value

Constraints: 
0<p<q<100000
Output Format

Output each Kaprekar number in the given range, space-separated on a single line. If no Kaprekar numbers exist in the given range, print INVALID RANGE.

--------------------

Created on 31 Dec 2015

@author: chris
'''
def testKaprekar(iTest):
    square = iTest*iTest
    digits = str(square)
    
    isKaprekar = False
    d = len(str(iTest))
    if d < len(digits):
        left = int(digits[:-d])
        right = int(digits[-d:])
    else:
        left = int(digits)
        right = 0
    
    if left + right == iTest:
        isKaprekar = True    
    
    return isKaprekar
    
iStart = int(raw_input().strip())
iEnd   = int(raw_input().strip())

kaprekarNumbers = []
for iTest in range(iStart, iEnd + 1):
    isKaprekar = testKaprekar(iTest)
    if isKaprekar:
        kaprekarNumbers.append(iTest)

if len(kaprekarNumbers) > 0:
    print " ".join(map(str,kaprekarNumbers))
else:
    print "INVALID RANGE"
    
    
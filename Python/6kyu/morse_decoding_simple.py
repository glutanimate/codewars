# -*- coding: utf-8 -*-
""" Decode the Morse code

Part of Series 1/3
This kata is part of a series on the Morse code. After you solve this kata, you may move to the next one.

In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superceded by voice and digital data communication channels, it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words.

Your task is to implement a function decodeMorse(morseCode), that would take the morse code as input and return a decoded human-readable string.

For example:

decodeMorse('.... . -.--   .--- ..- -.. .')
# should return "HEY JUDE"
# it is MorseCode.Get('.--'), in Haskell the codes are in a Map String String and can be accessed like this: morseCodes ! ".--", in Elixir it is morse_codes variable.
The Morse code table is preloaded for you as a dictionary, feel free to use it. In CoffeeScript, C++, Go, JavaScript, PHP, Python, Ruby and TypeScript, the table can be accessed like this: MORSE_CODE['.--'], in Java it is MorseCode.get('.--'), in C

#, tests will fail if the solution code throws an exception, please keep that in mind. This is mostly because otherwise the engine would simply ignore the tests, resulting in a "valid" solution.
All the test strings would contain valid Morse code, so you may skip checking for errors and exceptions. In C

Good luck!

After you complete this kata, you may try yourself at Decode the Morse code, advanced.


Tags: ALGORITHMS

Link: https://www.codewars.com/kata/decode-the-morse-code
"""

#############################################################
#                       TEST FRAMEWORK                      #
#############################################################

import sys
import os
sys.path.append(os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', "tests")))
from Test import *

MORSE_CODE = {'.-...': '&', '--..--': ',', '....-': '4', '.....': '5', '...---...': 'SOS', '-...': 'B', '-..-': 'X', '.-.': 'R', '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F', '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?', '.----': '1', '-.-': 'K', '-..': 'D', '-....': '6', '-...-': '=', '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N',
              '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';', '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G', '--.-': 'Q', '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':', '-.--': 'Y', '-': 'T', '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0', '----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8', '...--': '3'}


#############################################################
#                        MY SOLUTIONS                       #
#############################################################


def decodeMorse(morse_code):
    words = [i for i in morse_code.split("   ")]
    sentence = []
    for w in words:
        translated = "".join(MORSE_CODE[l] for l in w.split())
        sentence.append(translated)
    # the outer join..split construct removes extra whitespace
    return " ".join(" ".join(sentence).split())


#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################


#############################################################
#                           TESTS                           #
#############################################################

def testAndPrint(got, expected):
    if got == expected:
        test.expect(True)
    else:
        print "<pre style='display:inline'>Got '%s', expected '%s'</pre>" % (got, expected)
        test.expect(False)


test.describe("Example from description")
testAndPrint(decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')

test.describe("Basic Morse decoding")
testAndPrint(decodeMorse('.-'), 'A')
testAndPrint(decodeMorse('.'), 'E')
testAndPrint(decodeMorse('..'), 'I')
testAndPrint(decodeMorse('. .'), 'EE')
testAndPrint(decodeMorse('.   .'), 'E E')
testAndPrint(decodeMorse('...---...'), 'SOS')
testAndPrint(decodeMorse('... --- ...'), 'SOS')
testAndPrint(decodeMorse('...   ---   ...'), 'S O S')

test.describe("Extra zeros handling")
testAndPrint(decodeMorse(' . '), 'E')
testAndPrint(decodeMorse('   .   . '), 'E E')

test.describe("Complex tests")
testAndPrint(decodeMorse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '),
             'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')

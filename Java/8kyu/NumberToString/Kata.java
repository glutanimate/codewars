/* Convert a Number to a String!

We need a function that can transform a number into a string.

What ways of achieving this do you know?

Examples:

Kata.numberToString(123); // returns "123";   
Kata.numberToString(999); // returns "999";

Tags: FUNDAMENTALS, TYPE CASTING, NUMBERS, STRINGS

Link: https://www.codewars.com/kata/convert-a-number-to-a-string/train/java
*/

//#############################################################
//#                        MY SOLUTIONS                       #
//#############################################################

class Kata {
  public static String numberToString(int num) {
    return "" + num;
  }
}


//#############################################################
//#             OTHER INTERESTING SOLUTIONS & REMARKS         #
//#############################################################

// solution above is succinct, but not very pretty and less
// memory-effective because it produces two String objects

// One of the following solutions should be used instead:

class Kata {
  public static String numberToString(int num) {
    return String.valueOf(num);
  }
}

class Kata {
  public static String numberToString(int num) {
    return Integer.toString(num);
  }
}

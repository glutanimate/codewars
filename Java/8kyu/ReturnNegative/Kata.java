/* Return Negative

In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

Example:

Kata.makeNegative(1); // return -1
Kata.makeNegative(-5); // return -5
Kata.makeNegative(0); // return 0
Notes:

The number can be negative already, in which case no change is required.
Zero (0) can't be negative, see examples above.

Tags: FUNDAMENTALS, NUMBERS

Link: https://www.codewars.com/kata/55685cd7ad70877c23000102
*/

//#############################################################
//#                        MY SOLUTIONS                       #
//#############################################################

public class Kata {

  public static int makeNegative(final int x) {
      return x < 0 ? x : -x;
  }
  
}


//#############################################################
//#             OTHER INTERESTING SOLUTIONS & REMARKS         #
//#############################################################

// More compact, but less efficient:

import static java.lang.Math.abs;

public class Kata {
  public static int makeNegative(final int x) {
    return -abs(x);
  }
  
}


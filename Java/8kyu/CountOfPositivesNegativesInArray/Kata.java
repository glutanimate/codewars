/* Count of positives / sum of negatives

Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array:

C#/Java: new int[] {} / new int[0];
C++: std::vector<int>();
JavaScript/CoffeeScript/PHP/Haskell: [];
Rust: Vec::<i32>::new();
ATTENTION!

The passed array should NOT be changed. Read more here.

For example:

input int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15} 
return int[] {10, -65}.

Tags: FUNDAMENTALS, ARRAYS, LISTS, DATA STRUCTURES, ARITHMETIC, MATHEMATICS, ALGORITHMS, NUMBERS

Link: https://www.codewars.com/kata/count-of-positives-slash-sum-of-negatives/train/java
*/

//#############################################################
//#                        MY SOLUTIONS                       #
//#############################################################

public class Kata
{
    public static int[] countPositivesSumNegatives(int[] input)
    {
        if (input == null || input.length == 0) {
            return new int[0]; // return zero-length aray
        }
        
        int posCount = 0;
        int negSum = 0;
        
        for (int nr: input) {
          if (nr > 0) {
            posCount++;
          } else if (nr < 0) {
            negSum += nr;
          }
        }
        
        // declare, initialize, and return array using array literal
        return new int[] {posCount, negSum};
    }
}


//#############################################################
//#             OTHER INTERESTING SOLUTIONS & REMARKS         #
//#############################################################

// "else if" above would not have been necessary; could have just added
// all 0s. Though it would be interesting to know which option is actually
// faster: Checking (nr < 0) in every case, or just incrementing negSum
// for all numbers that don't fulfill (nr > 0)

// Solution using streams (>= Java 8):

import java.util.stream.*;

public class Kata {

  public static int[] countPositivesSumNegatives(int[] input) {
    return input == null || input.length == 0 ? 
      new int[0] : 
      new int[] { (int)IntStream.of(input).filter(i->i>0).count(), IntStream.of(input).filter(i->i<0).sum() };
  }
}

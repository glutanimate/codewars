/* Sum without highest and lowest number

Sum all the numbers of the array (in F# and Haskell you get a list) except the highest and the lowest element (the value, not the index!).
(The highest/lowest element is respectively only one element at each edge, even if there are more than one with the same value!)

Example:

{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6


If array is empty, null or None, or if only 1 Element exists, return 0.
Note:In C++ instead null an empty vector is used. In C there is no null. ;-) 


-- There's no null in Haskell, therefore Maybe [Int] is used. Nothing represents null.
Have fun coding it and please don't forget to vote and rank this kata! :-)

Tags: FUNDAMENTALS, BASIC LANGUAGE FEATURES

Link: https://www.codewars.com/kata/sum-without-highest-and-lowest-number/train/java
*/

//#############################################################
//#                        MY SOLUTIONS                       #
//#############################################################

public class Kata
{
  public static int sum(int[] numbers)
  {
    if (numbers == null || numbers.length <= 1) {
      return 0;
    }
    
    int max = numbers[0];
    int min = max;
    int sum = 0;
    
    for (int num : numbers) {
      sum += num;
      if (num > max) {
        max = num;
      }
      if (num < min) {
        min = num;
      }
    }
    
    return sum - max - min;
  }
}


//#############################################################
//#             OTHER INTERESTING SOLUTIONS & REMARKS         #
//#############################################################


public class Kata
{
  public static int sum(int[] numbers)
  {
    if (numbers == null || numbers.length == 0 || numbers.length == 1) return 0;
    // Interesting shorthand for declaring and initiating multiple
    //  variables at once:
    int min,max,sum;
    sum = min = max = numbers[0];

    for (int i = 1; i < numbers.length; i++)
    {
      sum += numbers[i];
      if (numbers[i] < min) min = numbers[i];
      if (numbers[i] > max) max = numbers[i];
    }
    return sum - min - max;
  }
}

// Using streams:

import static java.util.stream.IntStream.of;

public class Kata {

  public static int sum(int[] numbers) {
    return (numbers == null || numbers.length <= 2) ? 0 : of(numbers).sum() - of(numbers).max().getAsInt() - of(numbers).min().getAsInt();
  }
}

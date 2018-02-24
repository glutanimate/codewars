/* Convert number to reversed array of digits

Given a random number:

C#: long;
C++: unsigned long;
You have to return the digits of this number within an array in reverse order.

Example:

348597 => [7,9,5,8,4,3]

Tags: FUNDAMENTALS, NUMBERS, ARRAYS

Link: https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits/train/java
*/

//#############################################################
//#                        MY SOLUTIONS                       #
//#############################################################

import java.util.ArrayList;

public class Kata {
  public static int[] digitize(long n) {
    
    // use ArrayList because of unknown digit count:
    ArrayList<Integer> res = new ArrayList();
    long div = n;
    int dig;
    
    while (div != 0) {
      dig = (int) (div % 10); // explicitly cast result to int 
      div = div / 10;
      res.add(dig);
    }
    
    // convert ArrayList<Integer> to int[] (https://stackoverflow.com/a/23945015/1708932):
    int[] array = res.stream().mapToInt(i->i).toArray();
    
    return array;
    
  }
}

//#############################################################
//#             OTHER INTERESTING SOLUTIONS & REMARKS         #
//#############################################################


// Solutions that use Strings as intermediates:

// Using String[]
public class Kata {
    public static int[] digitize(long n) {
        String[] nums = new StringBuilder(String.valueOf(n)).reverse().toString().split("");
        int[] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            result[i] = Integer.parseInt(nums[i]);
        }
        return result;
    }
}

// Using StringBuilder
public class Kata {
  public static int[] digitize(long n) {
        return new StringBuilder().append(n)
                                  .reverse()
                                  .chars()
                                  .map(Character::getNumericValue)
                                  .toArray();
  }
}

// Converting char ASCII values for digits to their int values
import java.lang.Math;
public class Kata {
  public static int[] digitize(long n) {
    String s = String.valueOf(n);
    int length = s.length();
    int[] array = new int[length];
    for ( int i = 0; i < length; i++){
      // Casting a char to int returns its ascii value. 
      // The ascii value for '0' for example is 48, 
      // so subtracting 48 from it will convert it into its proper int value.
      array[i] = (int) (s.charAt(length - i - 1)) - 48;
    }
    return array;
  }
}

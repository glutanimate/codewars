/* Parse nice int from char problem

Ask a small girl - "How old are you?". She always says strange things... Lets help her!

For correct answer program should return int from 0 to 9.

Assume test input string always valid and may look like "1 year old" or "5 years old", etc.. The first char is number only.


Tags: BUGSINTEGERSNUMBERSCHARSFUNDAMENTALS

Link: https://www.codewars.com/kata/parse-nice-int-from-char-problem/train/java
*/

//#############################################################
//#                        MY SOLUTIONS                       #
//#############################################################

public class CharProblem {
  public static int howOld(final String herOld) {
    return Character.getNumericValue(herOld.charAt(0));
  }
}

//#############################################################
//#             OTHER INTERESTING SOLUTIONS & REMARKS         #
//#############################################################

/* 

"The nice thing about getNumericValue(char) is that it also works with strings like "el٥" and "el५" where ٥ and ५ are the digits 5 in Eastern Arabic and Hindi/Sanskrit respectively."

https://stackoverflow.com/a/4968343/1708932

More performant solution, although much more opaque:

str1="2345";
int x=str1.charAt(2)-'0';
//here x=4;

→ When subtracting chars, Java will use the ASCII-code value of each char. Since the ASCII
values increment for all digits starting from 0, we can simply subtract '0' from the digit string
to get the digit as an int.

 */


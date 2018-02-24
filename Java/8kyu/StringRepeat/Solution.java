/* String repeat

Write a function called repeatStr which repeats the given string string exactly n times.

repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"

Tags: FUNDAMENTALS

Link: https://www.codewars.com/kata/string-repeat/train/java
*/

//#############################################################
//#                        MY SOLUTIONS                       #
//#############################################################

public class Solution {
    public static String repeatStr(final int repeat, final String string) {
        String retStr = "";
        for (int i = repeat; i > 0; i--) {
          retStr += string;
        }
        return retStr;
    }
}


//#############################################################
//#             OTHER INTERESTING SOLUTIONS & REMARKS         #
//#############################################################


// String concatenation, as exemplified above, is very inefficient
// as a new String object will be created for every iteration
// Instead, one should usually opt for the StringBuilder class:

public class Solution {
    public static String repeatStr(final int repeat, final String string) {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < repeat; i++) {
            sb.append(string);
        }

        return sb.toString();
    }
}
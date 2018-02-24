/* Remove First and Last Character

It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

Tags: FUNDAMENTALS, BASIC LANGUAGE FEATURES, STRINGS

Link: https://www.codewars.com/kata/remove-first-and-last-character/java
*/

//#############################################################
//#                        MY SOLUTIONS                       #
//#############################################################

public class RemoveChars {
    public static String remove(String str) {
        StringBuilder sb = new StringBuilder(); 
        
        // String objects don't have a .length property like arrays
        // Instead we have to use the .length() method
        for (int i = 1; i < str.length() - 1; i++) {
            sb.append(str.charAt(i));
        }

        return sb.toString();
    }
}


//#############################################################
//#             OTHER INTERESTING SOLUTIONS & REMARKS         #
//#############################################################

// Welp, looks like there's a String.substring method:
public class RemoveChars {
    public static String remove(String str) {
        return str.substring(1, str.length() - 1);
    }
}


// Another interesting solution, using StringBuffer:
public class RemoveChars {
    public static String remove(String str) {
       return new StringBuffer(str).deleteCharAt(0).deleteCharAt(str.length()-2).toString();
    }
}
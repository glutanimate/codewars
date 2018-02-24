/* Sentence Smash

Write a method smash that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

Example

var words = ['hello', 'world', 'this', 'is', 'great'];
smash(words); // returns "hello world this is great"
Assumptions

You can assume that you are only given words.
You cannot assume the size of the array.
You can assume that you will always get an array.
What We're Testing

We're testing basic loops and string manipulation. This is for beginners who are just learning loops and string manipulation.

Disclaimer

This is for beginners so we want to test basic loops and string manipulation. Advanced users should easily be able to do this in one line.


Tags: FUNDAMENTALSLOOPSCONTROL FLOWBASIC LANGUAGE FEATURESCONDITIONAL STATEMENTSSTRINGSARRAYS


Link: https://www.codewars.com/kata/sentence-smash/train/java
*/

//#############################################################
//#                        MY SOLUTIONS                       #
//#############################################################


// Using Java8 String.join method:

public class SmashWords {
    // varargs notation "var..." for variable number of method arguments
    public static String smash(String... words) {
        return String.join(" ", words);
  }
}

// Manual implementation using loop

public class SmashWords {
  
    public static String smash(String... words) {
        int idx = 0;
        int max = words.length - 1;
        StringBuilder sb = new StringBuilder(); 

        for (String str: words) {
            sb.append(str);
            if (idx != max) {
                sb.append(" ");
            }
            idx++;
        }
        
        return sb.toString();
  }
}


//#############################################################
//#             OTHER INTERESTING SOLUTIONS & REMARKS         #
//#############################################################




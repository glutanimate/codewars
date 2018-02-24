/* A Needle in the Haystack

Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle

So

find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
findNeedle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
findNeedle(new Object[] {"hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"})
find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"])
should return

'found the needle at position 5'
'found the needle at position 5'
'found the needle at position 5'
"found the needle at position 5"
"found the needle at position 5"


Tags: FUNDAMENTALS, ARRAYS

Link: https://www.codewars.com/kata/a-needle-in-the-haystack/train/java
*/

//#############################################################
//#                        MY SOLUTIONS                       #
//#############################################################

public class Kata {
  public static String findNeedle(Object[] haystack) {
    for (int i = 0; i < haystack.length; i++) {
      Object arrItem = haystack[i];
      // using instanceof to prevent undefined comparisons
      // e.g. null vs String
      if (arrItem instanceof String && arrItem.equals("needle")) {
        // initially used "==" for String comparison, but ".equals"
        // is the prefered way of checking non-primitive type equivalency
        // (i.e. holding the same String value)
        // (https://stackoverflow.com/a/767379/1708932)
        return "found the needle at position " + i;
      }
    }
    return "needle not found.";
  }
}

//#############################################################
//#             OTHER INTERESTING SOLUTIONS & REMARKS         #
//#############################################################

// Clever utilization of List.indexOf:

import java.util.*;

public class Kata {
  public static String findNeedle(Object[] haystack) {
    return "found the needle at position " + Arrays.asList(haystack).indexOf("needle");
  }
}

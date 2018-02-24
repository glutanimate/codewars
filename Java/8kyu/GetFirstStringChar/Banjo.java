/* Are You Playing Banjo?

Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo" 
name + " does not play banjo"
Names given are always valid strings.

Tags: FUNDAMENTALSSTRINGSFUNCTIONSCONTROL FLOWBASIC LANGUAGE FEATURES

Link: https://www.codewars.com/kata/are-you-playing-banjo/train/java
*/

//#############################################################
//#                        MY SOLUTIONS                       #
//#############################################################

public class Banjo {
  public static String areYouPlayingBanjo(String name) {
    char first = name.charAt(0);
    if (first == 'r' || first == 'R') {
        return name + " plays banjo";
    }
    return name + " does not play banjo";
  }
}


//#############################################################
//#             OTHER INTERESTING SOLUTIONS & REMARKS         #
//#############################################################


// using String.toUpperCase and String.startsWith:

public class Banjo 
{
  public static String areYouPlayingBanjo(String name) 
  {
    if( name.toUpperCase().startsWith("R") )
      return name + " plays banjo";
    else
      return name + " does not play banjo";
  }
}
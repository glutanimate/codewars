/* Counting sheep...

Consider an array of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

For example,

[true,  true,  true,  false,
  true,  true,  true,  true ,
  true,  false, true,  false,
  true,  false, false, true ,
  true,  true,  true,  true ,
  false, false, true,  true]
The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined

Tags: FUNDAMENTALS, ARRAYS

Link: https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/java
*/

//#############################################################
//#                        MY SOLUTIONS                       #
//#############################################################

public class Counter {
  public int countSheeps(Boolean[] arrayOfSheeps) {
    int sheepCount = 0;
    
    for (int i = 0; i < arrayOfSheeps.length; i++) {   
      if (arrayOfSheeps[i] != null && arrayOfSheeps[i]) {
        sheepCount++;
      }
    }
    
    return sheepCount;
  }
}


//#############################################################
//#             OTHER INTERESTING SOLUTIONS & REMARKS         #
//#############################################################

/*
The check for null values is necessary because in boolean
comparisons both sides around the comparator are automatically
unboxed to boolean values, e.g.:

> param == true

implicitly becomes

> param.booleanValue() == true

----

Another solution would have been to use a construct similar
to the following:

> if (Boolean.TRUE.equals(param))
>   return "a";
> if (Boolean.FALSE.equals(param))
>   return "b";
> return "c";

*/


// Using a foreach loop:

// this does not perform a null check, though
public class Counter {
  public int countSheeps(Boolean[] arrayOfSheeps) {
    int count = 0;
    for (Boolean b : arrayOfSheeps) if (b) count++;
    return count;
  }
}
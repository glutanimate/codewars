/* Basic Mathematical Operations

Your task is to create a function - basic_op().

The function should take three arguments - operation(string/char), value1(number), value2(number). The function should return result of numbers after applying the chosen operation.

Examples:

basicOp('+', 4, 7)         // Output: 11
basicOp('-', 15, 18)       // Output: -3
basicOp('*', 5, 5)         // Output: 25
basicOp('/', 49, 7)        // Output: 7

Tags: FUNDAMENTALS, MATHEMATICS, ALGORITHMS, NUMBERS, OPERATORS

Link: https://www.codewars.com/kata/basic-mathematical-operations/java
*/

//#############################################################
//#                        MY SOLUTIONS                       #
//#############################################################

public class BasicOperations
{
  public static Integer basicMath(String op, int v1, int v2)
  {
  
    if (op.equals("+")) {
        return v1 + v2;
    } else if (op.equals("-")) {
        return v1 - v2;
    } else if (op.equals("*")) {
        return v1 * v2;
    } else if (op.equals("/")) {
        return v1 / v2;
    }
    
    return null;
  }
}


//#############################################################
//#             OTHER INTERESTING SOLUTIONS & REMARKS         #
//#############################################################


// Using switch:

// Question: How does the switch/case statement check for equality / equivalence?
// using the String.equals() method?
// 
// Answer: Yep,
// "The String in the switch expression is compared with the expressions 
// associated with each case label as if the String.equals method were being used. "
// (Source: https://docs.oracle.com/javase/tutorial/java/nutsandbolts/switch.html)

public class BasicOperations
{
  public static Integer basicMath(String op, int v1, int v2)
  {
  switch (op) {
    case "-":
      return v1 - v2;
      // break not needed because we return immediately
    case "+":
      return v1 + v2;
    case "*":
      return v1 * v2;
    case "/": {
      if (v2 == 0)
        throw new IllegalArgumentException("Division by zero");
      return v1 / v2;
    }
    default:
      throw new IllegalArgumentException("Unknown operation: " + op);
    }
  }
}
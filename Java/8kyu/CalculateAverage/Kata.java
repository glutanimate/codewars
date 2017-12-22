/* Calculate average

Description:

Write function avg which calculates average of numbers in given list.

Tags: FUNDAMENTALS,FUNCTIONAL PROGRAMMING,DECLARATIVE PROGRAMMING

Link: https://www.codewars.com/kata/calculate-average
*/

//#############################################################
//#                        MY SOLUTIONS                       #
//#############################################################

public class Kata{
  public static double find_average(int[] array){
    int length = array.length;
    double sum = 0; // need to declare sum as double to return double further below
    
    for (int number: array) {
      sum += number;
    }
    
    return sum / length;
  }
}

//#############################################################
//#             OTHER INTERESTING SOLUTIONS & REMARKS         #
//#############################################################
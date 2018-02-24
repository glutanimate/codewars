/* Grasshopper - Summation

Write a program that finds the summation of every number between 1 and num. The number will always be a positive integer greater than 0.

For example:

summation(2) -> 3
1 + 2

summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

Tags: FUNDAMENTALS, LOOPS, CONTROL FLOW, BASIC LANGUAGE FEATURES

Link: https://www.codewars.com/kata/grasshopper-summation/java
*/

//#############################################################
//#                        MY SOLUTIONS                       #
//#############################################################

public class GrassHopper {

    public static int summation(int n) {
        int res = 0;
        
        for (int i = 1; i <= n; i++) {
            res += i;
        }
        
        return res;
    }
}

//#############################################################
//#             OTHER INTERESTING SOLUTIONS & REMARKS         #
//#############################################################


// Turns out we can just use an algorithm to calculate the series
// (so called triangular number [de: Dreieckszahl, berechnet nach Gaußscher
// Summenformel], https://en.wikipedia.org/wiki/Triangular_number):
public class GrassHopper {

    public static int summation(int n) {

        return  n*(n+1)/2;
    }
}

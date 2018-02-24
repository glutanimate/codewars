/* Number of People in the Bus

There is a bus moving in the city, and it takes and drop some people in each bus stop.

You are provided with a list (or array) of integer arrays (or tuples). Each integer array has two items which represent number of people get into bus (The first item) and number of people get off the bus (The second item) in a bus stop.

Your task is to return number of people who are still in the bus after the last bus station (after the last array). Even though it is the last bus stop, the bus is not empty and some people are still in the bus, and they are probably sleeping there :D

Take a look on the test cases.

Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the return integer can't be negative.

The second value in the first integer array is 0, since the bus is empty in the first bus stop.

Tags: FUNDAMENTALS

Link: https://www.codewars.com/kata/number-of-people-in-the-bus/train/java
*/

//#############################################################
//#                        MY SOLUTIONS                       #
//#############################################################

import java.util.ArrayList;

class Metro {

  public static int countPassengers(ArrayList<int[]> stops) {
      int passengers = 0;
      
      for (int[] inAndOut: stops) {
          passengers += inAndOut[0] - inAndOut[1];
      }
      
      return passengers;
  }
}


//#############################################################
//#             OTHER INTERESTING SOLUTIONS & REMARKS         #
//#############################################################


// Solution using streams and lambda function:

import java.util.ArrayList;

class Metro {

  public static int countPassengers(ArrayList<int[]> stops) {
    return stops.stream()
                .mapToInt(x -> x[0] - x[1]) // lambda function declaration
                .sum();
  }
}
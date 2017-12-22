/* Calculate BMI

Write function bmi that calculates body mass index (bmi = weight / height ^ 2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"

Tags: FUNDAMENTALS

Link: https://www.codewars.com/kata/calculate-bmi/train/java
*/

//#############################################################
//#                        MY SOLUTIONS                       #
//#############################################################

import static java.lang.Math.pow;

public class Calculate {
    public static String bmi(double weight, double height) {
        double bmiVal = weight / pow(height, 2);
    
        if (bmiVal <= 18.5) {
            return "Underweight";
        } else if (bmiVal <= 25.0) {
            return "Normal";
        } else if (bmiVal <= 30.0) {
            return "Overweight";
        } else {
            return "Obese";
        }
    }
}


//#############################################################
//#             OTHER INTERESTING SOLUTIONS & REMARKS         #
//#############################################################



public class Calculate {
  public static String bmi(double weight, double height) {
    
      double bmi = weight / (height * height);  // simple operators instead of Math.pow

      // much simpler conditional, taking advantage of return statements:
      if ( bmi <= 18.5) return "Underweight";
      if ( bmi <= 25) return "Normal";
      if ( bmi <= 30) return "Overweight";
      return "Obese";

  }
}


// conditional return using nested ternary statements:
public class Calculate {
  public static String bmi(double weight, double height) {
    double bmi =weight/(height*height);
    return bmi <= 18.5 ? "Underweight": bmi <=25.0 ? "Normal" : bmi<=30.0 ? "Overweight" : "Obese";
    }
}
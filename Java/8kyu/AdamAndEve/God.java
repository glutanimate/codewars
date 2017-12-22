/* Basic subclasses - Adam and Eve

According to the creation myths of the Abrahamic religions, Adam and Eva were the first Humans to wander the earth.

You have to do God’s job. The creation method must return an array of length 2 containing objects representing Adam and Eva. The first object in the array should be an instance of the class Man. The second should be an instance of the class Woman. Both objects have to be subclasses of Human. Your job is to implement the Human, Man and Woman classes.


Tags: FUNDAMENTALS, CLASSES, BASIC LANGUAGE FEATURES, OBJECT-ORIENTED PROGRAMMING

Link: https://www.codewars.com/kata/basic-subclasses-adam-and-eve
*/

//#############################################################
//#                        MY SOLUTIONS                       #
//#############################################################

public class God {
  public static Human[] create(){
    Man adam = new Man();
    Woman eve = new Woman();
    
    Human[] creation = {adam, eve};

    return creation;
  }
}

class Human {}
class Man extends Human {}
class Woman extends Human {}

//#############################################################
//#             OTHER INTERESTING SOLUTIONS & REMARKS         #
//#############################################################

// General Remarks:
// Multiple classes cannot be declared as public in the same .java file.
// Each public class requires a separate .java file named after its class name.


// It makes sense to implement Human as an abstract class, since it is never 
// initialized:
public class God {
  public static Human[] create() {
     return new Human[] { new Man(), new Woman() };
  }
}

abstract class Human {}

class Man extends Human {}

class Woman extends Human {}


// Alternatively you might also consider implementing Human as an interface:

public class God {
  public static Human[] create(){
     return new Human[]{new Man(), new Woman()};
  }
}

interface Human {}
class Man implements Human {}
class Woman implements Human {}
###**Tips**
Our interviews are behavioral based, consisting of open ended questions to evaluate your technical abilities, work experience and behavioral traits.

Be familiar with General Dynamics Mission Systems–Canada, have an understanding of what we do.

Know the requirements of the job for which you are applying. Be able to explain how you meet and exceed these requirements.

Find a way to fill the hiring managers need with some of your other skills. Explain this to your interviewer, don't put yourself in a box. Use every opportunity to help yourself stand out and sell your skills.

Bring examples of any (non-proprietary) work products, writing samples, etc. that you have.

If you are applying for a technical job such as a software or systems engineer, be prepared to answer technical questions. (i.e. software development)

Come prepared with questions for your interviewer and make sure that you ask them.

Turn your experience into stories. Explain how what you did in the past relates to what you can do for us.

Be on time. One of our hiring managers informed that she is always in the lobby 15 minutes prior to an interview to see when the candidate arrives.

###**General**
1. What is the strongest attribute that you bring to the table?
2. Describe the last team that you worked on and your role on it.
3. What did you like and not like about your last company?
4. For a recent college graduate, what was your favorite class and why? What was your least favorite class and why?
5. What is your definition of accountability?
6. What has been your biggest success story to date?
7. Why do you want to work for General Dynamics Mission Systems–Canada?
8. How do you ensure that what your work is the highest quality?
9. How do you define project requirements and how do you make sure they are realistic?
10. Explain how you reason through problems when you don't know the answer right away.
11. Tell us about a time you received feedback which indicated you were not meeting expectations.
12. Describe your ideal work environment.
13. What work experience have you had that prepares you to be successful in this position?


##**Technical**
###**Gen Dy 1. Explain a few significant differences between the C++ and Java programming languages.**
  - Difference between Java and C
    - Java
      - Interpreted Language: the code is translated to bytecode and is executed by the Java virtual machine, this makes Java code portable on different devices
      - Object oriented. Good practices are high cohesion and low coupling.
        - Inheritance: Allows subclasses to be created from super classes that share a set of attributes and methods.
          Doesn't allow multiple inheritance due to parents having methods with the same signature, the compiler doesn't know which to call.
        - encapsulation: Used for data hiding and it groups data and the methods that only work on that data into a capsule
          Getter and setters to hide internal representation
        - abstraction: Used to hide implementation details and only show relevant methods to reduce complexity for the user that wants to implement them. We use abstract classes and interfaces to just present the methods.
          - Can implement multiple interfaces.
          - Fully abstract class and interface are the same. Interface use X implements Y. and is a contract for X to supply those methods.

            - abstract class
              - But, if a class has at least one abstract method, then the class must be declared abstract.
              - If a class is declared abstract, it cannot be instantiated.

              The purpose of abstract classes is to function as base classes which can be extended by subclasses to create a full implementation. For instance, imagine that a certain process requires 3 steps:
               1. The step before the action.
               2. The action.
               3. The step after the action.

               If the steps before and after the action are always the same, the 3-step process could be implemented in an abstract superclass with this Java code:
              ```
              public abstract class MyAbstractProcess {

                public void process() {
                    stepBefore();
                    action();
                    stepAfter();
                }

                public void stepBefore() {
                    //implementation directly in abstract superclass
                }

                public abstract void action(); // implemented by subclasses

                public void stepAfter() {
                    //implementation directly in abstract superclass
                }
              }
              ```

        - polymorphism (is - a): This means any child class object can take any form of a class in its parent hierarchy and of course itself as well. (methods may do different things so may want to be a different object)
          Ex. Person -> Teacher.
            We can create
              Person person = new Person(); //Person reference and object
              Person another_person = new Teacher(); //Person reference, Teacher object
              Teacher teacher = new Teacher(); //Teacher reference and obj.
              - If the reference is higher in the hierarchy, then it can create any child object. We do this because some subclasses have overwritten methods that do different things.
      - Garbage collection for unreferenced objects
      ```
      - No pointers, it has references, which is an alias variable for an already existing variable, it shares the same memory address, and are strongly typed (Can't cast to a different type unless the object is actually the type it is being cast to. Ex Object A = var; A = str(var); only if Object is a String object itself). One level of indirection and cannot reference NULL.
      ```
      - Method overloading: Same method name, but different parameters.
      - Java uses exception handling, so you can catch and deal with it.

    - C
      - C is compiled, as long as the platform has a C compiler it is portable, it converts code into machine code representation which is understood by the processor, but there is some code that is not portable other hardware. Like assuming a specific memory address is mapped to a hardware register and specific API (application programming interface) calls to the operating system.
      - Procedural, executes in the order it was written.
      - Need to manage memory with malloc and free or we risk memory leaks.
      ```
      - A pointer is a variable that holds the memory address of another variable, it can be re-assigned to point to another location, and you can perform arithmetic on pointers. Multiple levels of indirection and can point to NULL.
      ```
      - C, when there is an error it stops.

###**Gen Dy 2. Pick a project that you can discuss in detail and had a significant role on. Discuss the system design/architecture. What was the worst problem you had with this system and how did you fix it?**

###**Gen Dy 3. How much reuse do you get out of the code you develop?**


###**Gen Dy 4. Explain a time when you were able to improve upon the design that was originally requested.**
  Maze robot

###**Gen Dy 5. Do you want to stay on a technical career path or eventually move to a leadership/management role?**

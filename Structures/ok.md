TO DO:
	Searching/sorting algorithms code and by hand
	memorize pin calling in RPI

	In C, arguments to functions are passed by value, not by reference (do a search on that), you need pointers to get the behavior of the latter

	How to setup wiring pi and piface libraries : ?? simply download and include"??
	Missing up to date fourth year project code?? LOL

###**C exercises**

###**data structures**
- Array
- Linked List
- Hash map
- Stack
- Queue
- Binary Tree
- Matrix:
	Used in computer graphics to project 3D space onto a 2D screen.
	For data encryption and decryption
	- 2D array.
		- double myArray[3][12] = {0}; 3 arrays containing 12 elements, fill with 0;
		-	A[3][4] = { { 0, 0, 0, 0 }, { 0, 0, 0, 0 }, { 0, 0, 0, 0 } };
	- Sparse Matrix with multiple linked Lists


###**Algorithms**
- searching
- Sorting
- recursive
- iterative

###**Big O**
####**Purpose**
-	(yes) its used to describe the performance of an algorithm, usually the worst-case scenario, an example is the time complexity of a search.

-	(O(1)) For O of 1 it means the algorithm will always execute in the same time regardless of the size of the input data. An example is the best case for a search is O of 1, since the best case scenario is that first location searched contains the target.

-	(O(n)) For O of n it means the algorithm's performance grows linearly and in direction proportion to the size of the input data. An example is the worst case for a linear search where the target is at the very end.

- (O(n^2)) For O of n squared the algorithm's performance is directly proportional to the square of the input data. This usually involves nested loops over a data set.

- (O(log n)) For O of log n the algorithm's performance is proportional to the logarithmic function and means after the curve starts to flatten, the increase of input data has minimal effect on its performance. An example is binary search.

###**Strongly typed**
https://stackoverflow.com/questions/11328920/is-python-strongly-typed
- Python is Strongly, Dynamically typed
	Strongly: Type changes require explicit conversion. Example a string with only digits doesn't automatically convert to a number.
 	Dynamic: where at run time the objects are given a type.

- C is weakly, statically typed
	Weakly: A type can be converted implicitly. Example is assigning a byte value to an integer. The value will convert to an integer.
	Static: The type must be declared

###**OS class, programming in linux, using its OS**
== Processes: Has its own Process control block and runs in its own virtual address space. Can only interact with other processes through mechanisms like shared memory structures.
	States, Scheduling information (which process is going to run), identifiers (Process ID).
	InterProcess Communication (IPC): Linux supports the classic Unix TM IPC mechanisms of signals, pipes and semaphores and also the System V IPC mechanisms of shared memory, semaphores and message queues.

== Memory management:
	Placement Algorithm: Best fit, First Fit (from the top), Next fit (continue from current pointer).
Just read notes end \\\\\\\\\\\\\\\\\\\\\

###**Linux command line**
https://maker.pro/linux/tutorial/basic-linux-commands-for-beginners
4001 lab summaries
end \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

###**GCC (GNU (OS) Compiler Collection)**
https://www.thegeekstuff.com/2012/10/gcc-compiler-options/?utm_source=feedburner
end \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

###**software develop models**
== waterfall and incremental models
end \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

###**embedded systems: rpi, arduino**

== Little endian: Least significant byte in the lowest address, and MSB in highest address. ARM, intel, rpi
== example of Big endian is Motorola

== My experience is mainly writing and reading from/to pins for Sensor interpretation and fusion to complete tasks. For example, my projects like a maze robot and touch screen system.

== Reading and writing to pins: https://www.iot-programmer.com/index.php/books/22-raspberry-pi-and-the-iot-in-c/chapters-raspberry-pi-and-the-iot-in-c/35-raspberry-pi-iot-in-c-introduction-to-the-gpio?showall=&start=2

Initialize pins: pinMode(LedPin, OUTPUT);
write and read: digitalWrite(LedPin, HIGH);
								digitalRead(ButtonPin) == 0 //pushed, completing the circuit so rpi reads 0;
The circuit in the rpi is transistor switched, so writing LOW to an output turns the LED on.
		3.3V
			|
			|
			+----- to LED
OUT--// Transistor. Inputing high will draw to gnd
			|
			GND

== Pull up and down: http://learnelectronicsblog.com/what-is-a-pull-up-and-pull-down-resistor/

== changing a GPIO to: http://www.mosaic-industries.com/embedded-systems/microcontroller-projects/raspberry-pi/gpio-pin-electrical-specifications#gpio-pin-circuitry
	Input: Has hysteresis enable
	Output: output enable  

###**Arduino pin calls**
// Setup all output pins, first LED is at top. 13 pins, pin 2 is for INT0
pinMode(LED_BUILTIN, OUTPUT);
pinMode(0, OUTPUT);

// Interrupt pin
attachInterrupt(digitalPinToInterrupt(Hall_PIN), pin_ISR, FALLING);

digitalWrite(row+1, HIGH);

###**RPI C call. Link WiringPi**
gcc -o blink blink.c -lwiringPi		// compile

#include <wiringPi.h>

// Setup
if (wiringPiSetup () == -1)
	return 1 ;

pinMode (0, OUTPUT) ;         // aka BCM_GPIO pin 17

digitalWrite (0, 1) ;       // On. Pin 0, send 1

digitalWrite (0, 0) ;       // Off

int digitalRead (int pin) ;
analogRead (int pin) ;
analogWrite (int pin, int value) ;

###**PI Face**

pifacedigital_open(pfd2) //open the Pi Face board. pfd2 is just an integer. if pfd2 = 2, then open the 2nd PiFace

* @param pin_num The pin number to write to.
* @param value The value to write.
void pifacedigital_digital_write(uint8_t pin_num, uint8_t value);

* @param data The value to write.
* @param bit_num The bit number to read from.
* @param reg The register to write to (example: INPUT, OUTPUT, GPPUB).
* @param hw_addr The hardware address (configure with jumpers: JP1 and JP2).
void pifacedigital_write_bit(uint8_t data,
														uint8_t bit_num,
														uint8_t reg,
														uint8_t hw_addr);

pifacedigital_write_bit(1, sensor_thread_info.pin_num, OUTPUT, sensor_thread_info.pfd2_num);	//turn on IR LED
pifacedigital_write_bit(0, sensor_thread_info.pin_num, OUTPUT, sensor_thread_info.pfd2_num);	//turn off IR LED

* @param reg The register to read from (example: INPUT, OUTPUT).
* @param hw_addr The hardware address (configure with jumpers: JP1 and JP2).
uint8_t pifacedigital_read_reg(uint8_t reg, uint8_t hw_addr);

uint8_t inp = pifacedigital_read_reg(INPUT, pfd2_addr);	//Bulk read all 8 inputs at once from one pfd2_addr

pifacedigital_close(pfd2);

###**RPI python pins calls**
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT) # GPIO pin 12
pwm = GPIO.PWM(12, 1000) # Arbitrary 1000 for frequency
pwm.start(0)

pwm.ChangeDutyCycle(dutyCalc)

pwm.stop()

GPIO.cleanup()

end \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

###**C programming stuff**

== Call functions from other file:
	Calling another .c file - #include "ClasseAusiliaria.c"
	Better to have a .h file in the same directory - #include "ClasseAusiliaria.h"
		A header file is generally used to define all of the functions, variables and constants contained in any function library that you might want to use.
		https://www.tutorialspoint.com/cprogramming/c_header_files.htm
		https://stackoverflow.com/questions/7109964/creating-your-own-header-file-in-c

== Makefile: organize code compilation, collection of files to compile
##	hellomake: hellomake.c hellofunc.c
##		 gcc -o hellomake hellomake.c hellofunc.c -I.

== mutex vs semaphore: https://www.geeksforgeeks.org/mutex-vs-semaphore/
	wait(): if !=0 decrement, to enter critical section
	signal() or post() increment after critical section
	Try to achieve mutual exclusion, fairness, no starvation or deadlock, and progress (eventually complete)

	Synchronization means that you synchronize/order the access of multiple threads to the shared resource.

	Mutual exclusion means that only a single thread should be able to access the shared resource at any given point of time.

== header files and .c files: https://gcc.gnu.org/onlinedocs/gcc-3.0.2/cpp_2.html
	header files the related declarations appear in only one place and provides an interface for your source files

== linker vs compiler: https://stackoverflow.com/questions/3831312/what-are-the-differences-between-a-compiler-and-a-linker
	- The compiler converts code written in a human-readable programming language into a machine code representation which is understood by your processor. This step creates object files.
	- The linker is needed to create the executable where it links all the libraries involved.

== Pointers And Arrays: https://www.le.ac.uk/users/rjm1/cotter/page_59.htm

== Pointers: https://www.programiz.com/c-programming/c-pointers
	- int *i = malloc(sizeof *i);  **Here i is initialized to point to a dynamically-allocated block of memory. Don't forget to free(i) once you're done with it**
	- int i = 42, *p = &i; **here is how you create an automatic variable and a pointer to it as a one-liner. i is the variable, p points to it**
		- A function that has a pointer as an arg like int sort(int *size); ** can call by just doing sort(p);

== How C strings work, and how they are also pointers and arrays:
	char word[6] = "hello" or char word[3] = {"H", "I"}, need extra space for terminating
	Terminating char added by itself if string iteral (a constant which will be on read only memory): char word = "hello";
	Can explicitly add for custom terminating value. char word[3] = {'H', 'I', '\0'}. Can have a custom terminating value, just make sure you check for it.

	Iterating through arrays.
		With pointer
		char *i = list; i != "/0"; i ++  \\\\*
			i;

		Or Indexing
		int i = 0; i < size; i ++
								or (i <= size -1)
			array[i];

== passing arrays as parameter: through a pointer, since remember that the function pop its stack after finished execution; leave that function scope.
 	void sort(int *arr) or void sort(int arr[]). if want size you need to iterate through it to count.*

	int array[2] = {2, 3};
	Pass to the function like: sort(array)

== How bad C string use can result in buffer overflows: Avoid by checking length with boundaries and using strncpy and fgets to limit the number of bytes to use. Buffer overflow Could overwrite adjacent memory locations, or cause crash due to restricted action.

== How to cast anything to anything (its all just 1s and 0s after all:
		str to long; unsigned long int strtoul(const char *str, char **endptr, int base); **
		int to string (char *  itoa ( int value, char * str, int base )

== Manual memory management malloc/free: malloc (allocates the requested size of memory), calloc (sets the memory to 0), free (deallocates the pointed memory)

== array in declaring scope: https://stackoverflow.com/questions/11656532/returning-an-array-using-c
	- Declare in caller function, then pass it to the function:
			void foo(char *buf, int count) {
				for(int i = 0; i < count; ++i)
						buf[i] = i;
				}

			int main() {
    		char arr[10] = {0};
    		foo(arr, 10);
			}
			** Since declared in caller, the variable will still be present when returned from foo.

	- char *foo(int count) {
	    char *ret = malloc(count);
	    if(!ret)
	        return NULL;

	    for(int i = 0; i < count; ++i)
	        ret[i] = i;

	    return ret;	// Return pointer to the dynamically allocated array on heap
		}

		int main() {
		  char *p = foo(10);
		  if(p) {
		      // do stuff with p
		      free(p);
		  }

		  return 0;
		}
		** Since allocated on heap, when foo pops off stack the array is on the heap and still available.

== Stack vs Heap: https://www.gribblelab.org/CBootCamp/7_Memory_Stack_vs_Heap.html
- The Stack is a LIFO structure and is a limited region of memory that is optimized and managed by the CPU. It temporarily stores the variables declared by each function when called. When a variable is declared by a function it is pushed onto the stack and when the function exits all its variables are popped, so the variable scope is local.

	**Summary**
	- local variables only
	- the stack grows and shrinks as functions push and pop local variables
	- very fast access
	- there is no need to manage the memory yourself, variables are allocated and freed automatically
	- the stack has size limits (OS-dependent)
	- stack variables only exist while the function that created them, is running
	- variables cannot be resized

- The Heap is a larger region of your computer's memory that is not managed automatically so the user must be responsible for freeing any manual allocation. If not done memory leaks may occur. (A memory leak reduces the performance of the computer by reducing the amount of available memory). Variables created on the heap are accessible by any function, anywhere in your program. Heap variables are essentially global in scope.

	**Summary**
	-	variables can be accessed globally
	- no limit on memory size
	- (relatively) slower access
	- no guaranteed efficient use of space, memory may become fragmented over time as blocks of memory are allocated, then freed
	- you must manage memory (you're in charge of allocating and freeing variables)
	- variables can be resized using realloc()


== Function pointers: https://www.geeksforgeeks.org/function-pointer-in-c/   and example usb.   A function pointer references to code in memory and its a way to select which function to execute at run time based on conditional statements. Example calculator functions.

== main: https://stackoverflow.com/questions/204476/what-should-main-return-in-c-and-c
For C: int main(); where returning 0 indicates normal exit and any other is abnormal termination.
	int main(int argc, char* argv[])
	int main(int argc, char** argv); where argc is the number of arguments and argv is the vector of arguments.
		Example: gcc -o myprog myprog.c
		argc
			4
		argv[0]
			gcc
		argv[1]
			-o
		argv[2]
			myprog
		argv[3]
			myprog.c

		Another: ./fubar a b c

		argc = 4
		argv[0] = ./fubar
		argv[1] = a
		argv[2] = b
		argv[3] = c


For Python: if __name__ == "__main__":
	One reason for doing this is that sometimes you write a module (a .py file) where it can be executed directly. Alternatively, it can also be imported and used in another module. By doing the main check, you can have that code only execute when you want to run the module as a program and not have it execute when someone just wants to import your module and call your functions themselves.

end \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

###**Projects:**
RPI: Touch screen
Arduino: maze robot: Based on sensor data from detecting the line in a line maze or walls in a wall maze the motor behaviour changed to navigate the robot.
	LED globe: Persistance of vision illusion. Spin the 2D array of LEDs fast enough, 30 frames per second, it creates the illusion of a solid image when the LEDs and motor are synced.

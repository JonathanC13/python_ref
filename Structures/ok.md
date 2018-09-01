TO DO:
	String manipulation and Searching/sorting algorithms code and by hand
	memorize pin calling in RPI

	See what the value of referencing a pointer is
	int *p;*
	int c = 5;

  - print(&p); address of the actual pointer
  - print(p); address of stuff pointed to

	p = &c;
	print(*p) ; value*
	print(p)	; address of now c
	print(&p)	; address of actual pointer

	How to setup wiring pi and piface libraries : ?? simply download and include"??
	Missing up to date fourth year project code?? LOL

###**Gen Dy 1. Explain a few significant differences between the C++ and Java programming languages.**
  - Difference between Java and C
    - Java
      - Interpreted Language: the code is translated to bytecode and is executed by the Java virtual machine, this makes Java code portable on different devices
      - Object oriented
        - Inheritance: Allows subclasses to be created from super classes that share a set of attributes and methods.
        - encapsulation: Used for data hiding, the object has data and the functions it contains only deal with that data.
        - abstraction: Used to only show relevant methods to reduce complexity for the user that wants to implement them. We use abstract classes and interfaces to just present the methods.
        - polymorphism (is - a): This means any child class object can take any form of a class in its parent hierarchy and of course itself as well.
          Ex. Person -> Teacher.
            We can create
              Person person = new Person(); //Person reference and object
              Person another_person = new Teacher(); //Person reference, Teacher object
              Teacher teacher = new Teacher(); //Teacher reference and obj.
              - If the reference is higher in the hierarchy, then it can create any child object. We do this because some subclasses have overwritten methods that do different things.
      - Garbage collection for unreferenced objects
      ```
      - No pointers, it has references, which is an alias variable for an already existing variable, it shares the same memory address, and cannot be re-assigned. One level of indirection and cannot reference NULL.
      ```
      - Method overloading: Same method name, but different parameters.
      - Java uses exception handling, so you can catch and deal with it.

    - C
      - C is compiled, so it converts code into machine code representation which is understood by the processor. As long as the platform has a C compiler it is portable, but there is some code that is not portable. Like assuming a specific memory address is mapped to a hardware register and specific API (application programming interface) calls to the operating system.
      - Procedural, executes in the order it was written.
      - Need to manage memory with malloc and free or we risk memory leaks.
      ```
      - A pointer is a variable that holds the memory address of another variable, it can be re-assigned to point to another location, and you can perform arithmetic on pointers. Multiple levels of indirection and can point to NULL.
      ```
      - C, when there is an error it stops.

###**Gen Dy 2. Pick a project that you can discuss in detail and had a significant role on. Discuss the system design/architecture. What was the worst problem you had with this system and how did you fix it?**

###**Gen Dy 3. How much reuse do you get out of the code you develop?**


###**Gen Dy 4. Explain a time when you were able to improve upon the design that was originally requested.**

###**Gen Dy 5. Do you want to stay on a technical career path or eventually move to a leadership/management role?**


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

###**Processors**

####**Models:**
  - Von Neumann Model: Arithmetic and Logic unit (ALU), control unit (control signals), memory unit (holds data and program), input unit, and output unit.

  - System Bus model 3: Microprocessor controls the system bus, which has the data, address, and control busses, and the I/O and memory systems use those busses.
    - The Microprocessor controls the memory and I/O through the busses. 3 main tasks:
      1. Data transfer: MOV, Push, Pop, IN, OUT
      2. Arithmetic and logic: ADD, SUB, MUL.
      3. Program flow: Branch, Jump. Flags.
    - Types:
      - General Purpose: Desktop - Intel
      - GPU: Graphics Processing Unit - high throughput graphics processing
      - DSP: Digital Signal Processors
      - Microcontrollers: Entire computer on a single chip.

    - Address Bus: N Address line can access 2^N locations:
      - If N = 20 lines, then 1 M byte
      - If 16 MB locations, then 2^4 * 2^20 means N = 24 lines.

####**Registers:**
  - Execution Unit (execution of program instructions) multipurpose registers:
    - EAX: Accumulator: Used for arithmetic and logic operations. Destination for MUL and DIV
    - EBX: Base Index: Usually used to hold offset address
    - ECX: Count: Usually used to hold count value for instructions like loops and rotates.
    - EDX: Data: temporary data storage for part of a result from multiplication or division (dividend, remainder)

    - ESP Stack pointer: Used to offset into the stack segment to address the stack. PUSH/POP
    - EBP Base pointer: Used to store a base memory location for data transfers
    - EDI Destination Index: Usually used as an offset for the destination memory location for string/byte transfers
    - ESI Source index: Usually used as an offset for the source memory location for string/byte transfers.

    - Flag register: Certain bits for flags:
      - C, carry flag
      - P, parity
      - A, auxiliary
      - Z, zero result
      - S, sign
      - T, trap
      - I, interrupt
      - D, direction
      - O, overflow; result exceeded
        - indicates that result is too large to fit in the 8-bit destination operand:
          Due to 2's complement
            Signed
          - the sum of two positive signed operands exceeds 127.
          - the difference of two negative operands is less than -128.

  - BIU (Bus Interface Unit) - provides interface to memory and I/O:
    1. controls the address, data, and control busses.
    2. handles instruction fetch and data read/write functions
      - CS Code Segment: Used to compute the starting address of the section of memory holding code (restricted to 64K in REAL mode).

      - DS Data Segment: Used to compute the starting address of the section of memory holding data (restricted to 64K in REAL mode).

      - SS Stack Segment: Used to compute the starting address of the section of memory holding the stack (restricted to 64K in REAL mode).

      - ES Extra Segment: Additional data segment used by some string instructions.

      - FS&GS Additional segment registers in the 80386 (and up) for program use.

  - Address Generation:
    - Real Mode: the 8086/8088/186 can only operate in this mode)
      - Allows the mP to address the first 1Mbyte of memory only.
      The mP has a set of rules that apply whenever memory is addressed, which define the segment and offset register combination used by certain addressing modes.
      ```
      Segment |Offset                 |  Special Purpose
      --------|-----------------------|------------------------------
      CS      |  IP                   |  Instruction address
      SS      |  SP or BP             |  Stack address
      DS      |  BX,DI,SI,            |  Data address
              |  8bit # or 16bit #    |
      ES      | DI                    |  String destination
              |(for string instruction)
      ```
    - Protected mode:
      - This mode uses the segment register contents (called a selector) to access a descriptor from a descriptor table.

####**Addressing Modes**
  Effective Address (EA): The execution unit is responsible for the BIU which combines it with the segment register.

  - Register Addressing:
    - Data is in the registers specified in the instructions.
    - eg: MOV AX,BX

  - Immediate addressing:
    - Data is a constant and is part of the instruction.
    - eg: MOV AX,3AH

  - Direct Addressing:
    - The 16 bit effective address is part of the instruction.
    - e.g. MOV BX,[1000H]

  - Register indirect addressing (based addressing)
    - the effective address is held in BP, BX, DI or SI.
    - MOV BX,1000H
      MOV AX,[BX]

      ; AL ← DS x 10H + 1000H
      ; AH ← DS x 10H + 1001H

  - Register relative addressing (base + displacement)
    - formed by the sum of a base or index register plus a displacement.
    - MOV AX,[BX+4H]

  - Base plus index addressing (base + index)
    - effective address is formed as the sum of a base register (BP or BX) and an index register (DI or SI)
    - MOV [BX+DI],CL

  - base relative plus index addressing (base + displacement + index)
    - effective address is the sum of base + index + displacement.
    - MOV [BX+DI+8AH],CL

####**I/O systems:**

  Handshaking to guarantee transfer
    1. VALID signal latches/strobes data into port
    2. The STATUS bit is set by the VALID signal
    3. mP reads the STATUS bit
    4. mP reads DATA resets STATUS asserts ACK
    5. Device sees ACK deasserts VALID prepares next data
    6. Port deasserts ACK when VALID is deasserted

  1. I/O mapped I/O (isolated I/O): I/O Ports are isolated from memory in a separate I/O address space. Data transfer from/to I/O is restricted to IN and OUT instructions. Separate control signals using M/IO, WR, RD enable I/O ports. Intel-based PC’s use isolated I/O.

  2. Memory Mapped I/O: I/O device is treated as a memory location. Any memory transfer instruction can used to access the device. Reserves fixed portion(s) of the memory map for I/O.

####**Interrupts: Special event requiring CPU to stop normal program execution and perform some service related to that event. Allows for asynchronous execution of service routines. An interrupt service procedure (ISP) is the interrupt.**

  - A hardware interrupt is an electronic alerting signal sent to the processor from an external device, like a disk controller or an external peripheral. For example, when we press a key on the keyboard or move the mouse, they trigger hardware interrupts which cause the processor to read the keystroke or mouse position.
    - caused by mP pins
    - INTR – interrupt pin
      - level sensitive
      - must remain held by external device at logic 1 until INTA goes low
      - usually reset within the interrupt service routine (ISR)
    - NMI – non-maskable interrupt
      - edge triggered.
      - must be logic zero for two clock periods before positive edge.
      - must remain held by external device at logic 1 until INTA goes low.
      - Often used for parity errors, power failures and other major faults.

  - A software interrupt is caused either by an exceptional condition or a special instruction in the instruction set which causes an interrupt when it is executed by the processor.
    - INT n – specify interrupt type (32-255)
    - INT 3 is special 1-byte case (useful for debugging)
    - INTO – interrupt on overflow (‘O’ flag bit)
    - BOUND – specify upper & lower bounds
    - Divide by zero error
```
  Interrupted processing: doesn’t “know” it was interrupted
    Processor:
      - temporarily suspends current thread of control
      - runs ISR
      - resumes suspended thread of control

  Polling: The state of continuous monitoring is known as polling. The microcontroller keeps checking the status of other devices; and while doing so, it does no other operation and consumes all its processing time for monitoring.
    - sequential programming: next instruction determined by control transfer instructions.

  Interrupts: device tells CPU it is time to do something … NOW.
    - event-driven programming.  
    - external hardware spontaneously cause control transfer (interruption in default program sequence).
```
  - For every interrupt, there must be an interrupt service routine (ISR), or interrupt handler. When an interrupt occurs, the microcontroller runs the interrupt service routine. For every interrupt, there is a fixed location in memory that holds the address of its interrupt service routine, ISR. The table of memory locations set aside to hold the addresses of ISRs is called as the Interrupt Vector Table.

  - Level–sensitive: external interrupt generated as long as pin is high/low
      Pros: multiple interrupt sources can be tied to this pin.
      Cons: source must ensure line becomes inactive before IRQ’s ISR is complete if only one interrupt request pending.

  - Edge-sensitive: external interrupt generated when pin changes (either high-low or low-high)
      Pros: no need for interrupt source to control duration of IRQ pulse.
      Cons: not suitable for noisy environment (falling edge caused by noise will be recognized as an interrupt).

  - Interrupt Response Sequence
    Each time the mP completes execution of an instruction, it will check the status of NMI and INTR.
    - if either is active, or if the next instruction is INTO, INT n, or BOUND, then:
      1. Push flag register onto stack.
      2. Clear IF and TF (interrupt enable and trap flags). Interrupts are now disabled. (So an interrupt cannot be interrupted)
      3. Push CS then IP on stack.
      4. Fetch the interrupt vector: Each interrupt vector contains the address (segment and offset) of the service routine.
      5. Proceed to the ISR; flush the instruction queue
    - The final statement of an interrupt service routine (ISR) is IRET – it pops IP, CS and Flags.

  Applications:
    - If a sensor read high, it just reset a counter

end \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

###**By Reference and value**
When a parameter is passed by reference, the caller and the callee use the same variable for the parameter. If the callee modifies the parameter variable, the effect is visible to the caller's variable.

When a parameter is passed by value, the caller and callee have two independent variables with the same value. If the callee modifies the parameter variable, the effect is not visible to the caller.

###**C programming stuff**

== A pointer stores the address of another variable.

== 	In C, arguments to functions are passed by value. Example passing a pointer is passing the value of the pointer and to use it, you can deference it (*p for the content)* or reference ((&p or p) to get the address)

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

###**Multithreading**###
Creating a new or duplicate process:
	- In Linux, use
		pid_t pid;
		pid = fork(); // create child process.

Creating a thread:

  ```
	#include <pthread.h>

	void *thread_function(void *arg);

	int main()

		int result;
		pthread_t a_thread;
		void *thread_result;

		//int pthread_create(pthread_t *thread, const pthread_attr_t *attr, void *(*start_routine) (void *), void *arg);
		result = pthread_create(&a_thread, NULL, thread_function, (void *)message);

		if (result != 0){
			perror("Thread creation failed.");
			exit(EXIT_FAILURE);
		}

		printf("\n waiting for thread to finish . . .\n");
		res = pthread_join(a_thread, &thread_result);
		if (res != 0){
			perror("thread join failed\n");
			exit(EXIT_FAILURE);
		}
	```

C semaphore:

For one whole program
**Init:**

  ```
	int res;

	// int sem_init(sem_t *sem, int pshared, unsigned int value); if 0 it is shared among threads, if pshared is non-zero means shared with multiple processes so need a shared memory location.
	res = sem_init(&bin_sem, 0, 0);	// 2nd arg is scope
	if (res != 0){
		perror("Semaphore initialization failed.\n");
		exit(EXIT_FAILURE);
	}
  ```

**decrement (wait):**

  ```
	sem_wait(&bin_sem);// decrement by 1, if sem is 0 then it is blocked here
  ```

**increment (signal):**

  ```
	sem_post(&bin_sem); // increment by 1, if 0 it may unblock for another thread or process
  ```
If multiple programs with same semaphore (Like two processes using shared memory), then need to use:
  ```
	int semctl(int sem_id, int sem_num, int command, ...);
	int semget(key_t key, int num_sems, int sem_flags);
	int semop(int sem_id, struct sembuf *sem_ops, size_t num_sem_ops);
  ```

###**Synchronization** for threads and processes that share a resource.###
The OS can block the process/thread instead of doing a busy waiting in a loop for a shared resource, wasting CPU time on their processor.

Try to satisfy:
  - Mutual exclusion: only one thread is in its critical section at a time.
	- Progress
	- Bounded wait: Guarantees all processes can enter the critical section. Picked from blocked queue.
	- Fairness: If only one process needs to enter the critical section then it should be able to do it immediately.


  - General Semaphores: An integer used for signaling for processes and there are only 3 operations; initialize, decrement (may block a process, wait()), and increment (may unblock a process, signal()).
    - Strong: The process blocked the longest is released from the queue first (FIFO). Guarantees no starvation.
    - Weak: order removed from blocked queue not specified.

  - Mutex: is a lock and the processes that locked the mutex must be the one to unlock it.

  - Inter-process communications (IPC) facilities:
  	1. Sharing common sempaphore
	  2. Shared memory: It allows two unrelated processes to access the
same logical memory. Shared memory is a very efficient way of transferring data between two running
processes. A special range of addresses that is created by IPC for one process and appears in the
address space of that process. Other processes can then “attach” the same shared memory segment into
their own address space. All processes can access the memory locations just as if the memory had been
allocated by malloc . If one process writes to the shared memory, the changes immediately become visible
to any other process that has access to the same shared memory.

  ```
	#include <sys/shm.h>
	void *shmat(int shm_id, const void *shm_addr, int shmflg);
	int shmctl(int shm_id, int cmd, struct shmid_ds *buf);
	int shmdt(const void *shm_addr);
	int shmget(key_t key, size_t size, int shmflg);
  ```

	Ex.
	#include "shm_com.h"	// shared memory structure for both consumer and producer to use, has a flag within to indicate which process will continue. int written_by_you;

  ```
	int running = 1;
	void *shared_memory = (void *)0;
	struct shared_use_st *shared_stuff;
	int shmid;

	srand((unsigned int)getpid());	// seed for random. next = getpid() value

	// create, returns unique id
	shmid = shmget((key_t)1234, sizeof(struct shared_use_st), 0666 | IPC_CREAT);	//

	if(shmid == -1){
		fprintf(stderr, "shmget failed\n");
		exit(EXIT_FAILURE);
	}

	// attach
	shared_memory = shmat(shmid, (void*)0, 0);	//attach the shared memory to shmid. Returns pointer to the first byte of the shared memory
	if (shared_memory == (void*)-1){
		fprintf(stderr, "shmat failed\n");
		exit(EXIT_FAILURE);
	}

	// after finished, detach from shared memory
	if (shmdt(shared_memory) == -1){
		fprintf(stderr, "shmdt failed\n");
		exit(EXIT_FAILURE);
	}

	// Delete the shared memory since this is the creator
	if(shmctl(shmid, IPC_RMID, 0) == -1){
		fprintf(stderr,"shmctl(IPC_RMID) failed\n");
		exit(EXIT_FAILURE);
	}

  ```

	// If we need to use semaphores on shared memory we can either put the semaphore on in shared memory or share named POSIX semaphores.
		1. share named POSIX semaphores
      ```
			//Choose a name for your semaphore
			#define SNAME "/mysem"

			//Use sem_open with O_CREAT in the process that creates them
			sem_t *sem = sem_open(SNAME, O_CREAT, 0644, 3); /* Initial value is 3. */
			errno=0;  /* <---- This is an important thing I learned when using errno. */
			if ((sem_t *semaphore = sem_open("/sem1", O_CREAT | O_EXCL, 0644, 0)) == SEM_FAILED)
			   {
			   fprintf(stderr, "sem_open() failed.  errno:%d\n", errno);
			   ...

		// then in the other process open the semaphore so it can use it.
		sem_t *sem = sem_open(SEM_NAME, 0); /* Open a preexisting semaphore. */
		```

		2. Shared

		```
		#include        <stdio.h>
		#include        <limits.h>
		#include        <stdlib.h>
		#include        <sys/time.h>
		#include        <semaphore.h>
		#include        <unistd.h>
		#include        <sys/mman.h>
		#include        <sys/stat.h>
		#include        <fcntl.h>

		shm();
		int fd;
		void *sem_id;
		int num = 1;
		int err;
		size_t large = sizeof(sem_t);

		if ((fd = shm_open("SHARE_MEMORY", O_CREAT | O_TRUNC | O_RDWR, 0666)) < 0) {
			perror("shm_open error ");
			exit(EXIT_FAILURE);
		}

		if (ftruncate(fd, large) < 0) {
			perror("ftruncate error ");
			exit(EXIT_FAILURE);
		}

		if ((sem_id = mmap(0, large, PROT_READ | PROT_WRITE , MAP_SHARED, fd, 0)) < 0) {
			perror("mmap error ");
			exit(EXIT_FAILURE);
		}

		close(fd);

		if ( sem_init(sem_id, 1, 0) < 0 ) {
			perror("sem_init error");
			exit(1);
		}
		```

	shm_open() allows multiple un-related processes to access
	the same shared memory - since it can be accessed by a well
	know name.

	shmget() requires some way for the creating process to
	give the 'key' used to create the memory to other processes
	so they can access it. sometimes the creating process
	writes the 'key' to a well known file name so that other
	un-related processes can read the key.

	if the creating process only needs to share the memory with
	child processes created via fork(), then shmget() is ok;
	otherwise, shm_open() is often used.

	3. Message Queues

In Java:
  - Synchronization
  Use 'synchronized' keyword to only allow one thread to access a method or data structure / object at one time.

  - Multithreading
  1. public void run(); // So when we do thread.start() it executes this method.
  2. Thread(Runnable threadObj, String threadName); // Create the thread with the object that has a runnable interface.
  3. thread.start(); // to call the run() method.

  - Rate monotonic scheduling
  - Cyclic Executive


###**Network programming**
  - Sockets? packets?

###**Testing**
- Application Under Test (AUT)
- Unit testing, white box testing (data coverage, code coverage), black box testing (input testing)

###**Projects:**
RPI: Touch screen
Arduino: maze robot: Based on sensor data from detecting the line in a line maze or walls in a wall maze the motor behaviour changed to navigate the robot.
	LED globe: Persistance of vision illusion. Spin the 2D array of LEDs fast enough, 30 frames per second, it creates the illusion of a solid image when the LEDs and motor are synced.

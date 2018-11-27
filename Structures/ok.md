Conservatives####**Leonardo DRS**
C / Java
  - Differences
    - Object Oriented


experience in software projects involving embedded software design and integration
- Touch screen
- Robot maze
- LED globe

Multitasking/multithreading (Processes and threads), synchronization concepts (semaphores, mutexes, inter-processor communications), ISR, Interrupt handle
  - Hand write producer/cons and reader/writer.

VoIP:
  Use IP to carry voice for telephone calls. I just some overall elements it needs to operate like:
    1. Signaling: capability to generate and exchange control information that will be used to establish, monitor, and release connections between two end-points. including H.323, Session Initiation Protocol (SIP), H.248, Media Gateway Control Protocol (MGCP), and Skinny Client Control Protocol (SCCP)
    2. Database services for extra services like caller ID.
    3. Codecs: coding and decoding translation between analog and digital facilities
    4. Bearer control: Bearer channels are the channels that carry voice calls. Proper supervision of these channels requires that appropriate call connect and call disconnect signaling be passed between end devices. Correct signaling ensures that the channel is allocated to the current voice call and that a channel is properly deallocated when either side terminates the call.

    Benefits:
      - Dynamic call routing
      - Long distance calls by pass
      - Security encryption and availability.
      - User portability

    Cons: technical challenges.
      - Delays degrade voice quality, high ping is noticeable
      - Network jitter, packet arrival gaps
      - Security of network. Different issues that traditional phone system
      - Existing NAT (network address translation) may not translate to the correct private IP.

TCP/IP, UDP
  Transmission Control Protocol: Connection-oriented (Handshaking), point to point, reliable (in order), flow and congestion control, full duplex.

  The Model
  4. The application layer provides applications with standardized data exchange. Its protocols include the Hypertext Transfer Protocol (HTTP), File Transfer Protocol (FTP), Post Office Protocol 3 (POP3), Simple Mail Transfer Protocol (SMTP) and Simple Network Management Protocol (SNMP).

  3. The transport layer is responsible for maintaining end-to-end communications across the network. TCP handles communications between hosts and provides flow control, multiplexing and reliability. The transport protocols include TCP and User Datagram Protocol (UDP), which is sometimes used instead of TCP for special purposes.

  2. The network layer, also called the internet layer, deals with packets and connects independent networks to transport the packets across network boundaries. The network layer protocols are the IP and the Internet Control Message Protocol (ICMP), which is used for error reporting.

  1. The physical layer consists of protocols that operate only on a link -- the network component that interconnects nodes or hosts in the network. The protocols in this layer include Ethernet for local area networks (LANs) and the Address Resolution Protocol (ARP).

  - User Datagram protocol (UDP): Connectionless data transfer, has error checking with checksum, etc.
  java

    ```
    byte[] sendBuf;
    int sendLen;

    InetAddress remoteIpAddress;
    int remotePort;

    DatagramPacket packet = null;

    //DatagramPacket(byte[] buf, int length, InetAddress address, int port)
    packet = new DatagramPacket(sendBuf, sendLen + 4, remoteIpAddress, remotePort);
    rcvHanlder.transferSocket.send(packet);
    ```

    **Summary**
    I took an elective in computer communications that taught the concepts and functions of each layer. I know that TCP/IP is a communication model used to connect devices to the internet. The layers are Application, Transport, Network, and data link.

    TCP (Transmission Control Protocol), is responsible for Connection-oriented Handshaking, point to point connection, reliable in order transfer, flow and congestion control, and being full duplex. **Transport layer.**
    IP (internet protocol), is responsible for routing and forwarding datagrams across network boundaries. Its routing function enables internetworking, and essentially establishes the Internet. It requires hosts to have an IP address to uniquely identify it to public networks. **Network layer.**

      An Internet Protocol address (IP address) is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication.[1][2] An IP address serves two principal functions: host or network interface identification and location addressing.

    I also had experience using UDP datagrams in a project to implement TFTP (Trivial File transfer protocol). (used for reliable transferring of files; Handshaking)

    3. transport layer. It provides host to host communication services (end to end), management of error correction, providing quality and reliability to the end user, and it also allows multiplexing (many users share a medium bursty data, requires mux/demux).
      - TCP (Transmission Control Protocol), is responsible for Connection-oriented (Handshaking), point to point connection, reliable in order transfer, flow and congestion control, and being full duplex.
        - Flow control is traffic at the receiver buffer
        - Congestion control is traffic in the network, detected with packets dropped.
      - User Datagram protocol (UDP): Connectionless data transfer, has error checking with checksum

      multiplexing is a method by which multiple analog or digital signals are combined into one signal over a shared medium.

      Transport layer gathers chunks of data it receives from different sockets and encapsulate them with transport headers. Passing these resulting segments to the network layer is called multiplexing.

      The reverse process which is delivering data to the correct socket by the transport layer is called demultiplexing. But this still doesn’t explain how the transport layer identifies the correct socket. Port numbers are the ones that do the trick.s

    2. Network layer/ Internet layer in every host and router, it has 2 key functions:
      - Packet forwarding to the correct output at each router.
      - Determining the route taken by the packet from the source to destination.
        Distance Vector:
          - Nodes have information for neighbors, local info globally
          - Good for large networks since exchange is to neighbors. In link state flooding could be expensive.
        Link state:
          - Routers have complete topology, global info locally.
          - Supports multiple paths to Destination
          - Fast reaction to a failure on a link.

        Failure in link:
          Solution:
            - Split horizon: do not report route to destination to the node it learned it from
            - Poisoned reverse: report infinite to the node it learned the route from.

      Can provide connectionless Datagram networks, (packets may take different paths) which doesn’t require an end to end connection (uses look up table to determine the next hop), or Connection oriented networks (signaling protocols for setup, maintain, and tear down virtual circuit) like Multiprotocol label switching.

    1. Data link layer: Has the responsibility of transferring datagrams from one node to an adjacent node in the network. It provides framing, link access, reliable delivery, flow control, error detection, error correction, and duplexing. Ethernet or ppp.
      (Parity check, Checksum, cyclic redundancy check)

        Includes:
        - Address resolution protocol (ARP): Maps IP and MAC addresses to be able to send the datagram to the correct destination. Every host has an ARP table and is self learning if doesn't know.

        - Medium access control layer (MAC): controls access to the medium through CSMA/CD or CA for wireless. Also determines where one frame of data ends and the next one starts – frame synchronization. There are four means of frame synchronization: time based, character counting, byte stuffing and bit stuffing.

          MAC addresses are also known as hardware addresses or physical addresses. They uniquely identify an adapter on a LAN. They allow computers to uniquely identify themselves on a network at this relatively low level. IP changes if device moves, but MAC stays the same.
          DHCP also usually relies on MAC addresses to manage the unique assignment of IP addresses to devices.


      Still needed but not specified
      PHY layer: The physical layer deals with bit-level transmission between different devices, it connects different interfaces (electrical and/ mechanical) to the physical medium to support synchronized communication.
        Physical media:
          Coaxial cable, Fiber optic
        Multiplexing:
          Time Division multiplexing
          OFDM: Orthogonal
          Frequency Division Multiplexing
          Wavelength Division multiplexing
          Code Division Multiplexing.

computer architecture
  **ARM**
    Intro to ARM processor (Advanced RISC (Reduced instruction set computer) Machine) where the chip is smaller, lower power consumption, and higher speed due to better pipelining by adding stages and trying to have them take equal duration (fetch and execution).

      - Fetch instruction (FI)
      - Decode instruction (DI)
      - Calculate operand (CO)
      - Fetch operand (FO)
      - Execute instruction (EI)
      - Write operand (WO)

        Hazards: Non identical duration means waiting for other stages, branching and interrupts invalidate fetching, memory conflicts
    ARM Features:
    1. fixed instruction lengths (usually 4 bytes);
    2. simple addressing modes (no indirect);
    3. register/register operations (load and store); and
    4. simple instruction format.

    - A load-store architecture: load data into registers, process data, store results.
    - Fixed-length 32-bit instructions, or 16-bit Thumb
    instructions
    - 3-address instruction formats.

      ARM uses a load-store model for memory access which means that only load/store (LDR and STR) instructions can access memory. While on x86 most instructions are allowed to directly operate on data in memory, on ARM data must be moved from memory into registers before being operated on. This means that incrementing a 32-bit value at a particular memory address on ARM would require three types of instructions (load, increment, and store) to first load the value at a particular address into a register, increment it within the register, and store it back to the memory from the register.

        - Use load/store to minimize the architecture since only operating on registers and The instructions should be simple enough to only require 1 execute cycle in the pipeline to be effective

    - I/O
      - Memory-mapped IO devices: Devices appear as
      addressable locations in ARM memory map.
      - Reading and writing to devices use load-store
      instructions.
      - Peripherals attract processor’s attention by normal
      interrupt requests, normal (IRQ) or fast (FIQ).
      - Most interrupt sources connect to IRQ input, one or two
      time-critical sources connect to high-priority FIQ.
      - Interrupts comprise a special form of exceptions.


    - Processor Modes

        ARM supports 7 modes of operation.
        • User (unprivileged) Mode: Used by most applications.
        While processor in this mode, program being executed
        does not have access to protected system resources.

        • Exception (privileged) Modes: Used to run system
        software. Have full access to system resources. Modes
        can be exchanged freely.
          1. Supervisor Mode: Used by operating system.
          2. Abort Mode: Entered in response to memory fault.
          3. Undefined Mode: Entered when processor attempts an
          supported instructions.
          4. Fast Interrupt Mode: Entered when processor receives
          signal from fast interrupt source. Fast interrupt cannot
          be interrupted but can interrupt a normal interrupt.
          5. Interrupt Mode: Entered when processor receives
          signal from interrupt source.
          6. System Mode: Used for running certain privileged
          operating system tasks.

  **Intel x86 CISC machine**, below
    Taught Intel x86 Microprocessor systems like Registers, Addressing Modes, I/O systems, Interrupts

data structures
  - technical doc

standard programming practices
  - Clear definition, High cohesion (class has clear goal.)
  - Low coupling between modules.
    - Use setters and getters.
    - Provide interfaces instead of linking methods in other classes directly.
  - Encapsulation: The module has data and the functions it contains only deal with that data.
  - Simple to use
  - Readability
  - Testability

testing
  **Summary**
  I took an elective on software verification and validation that taught methods for black box, white box, and integration testing.
  - Questions doc

  - Functional requirements: Defines what the system behaviour is with certain inputs described in its specifications.
	Unit testing (test individual methods), integration testing (big bang, top down, bottom up, sandwich) After unit tests determine which modules to do integration testing order. System testing, acceptance testing.

  - Non-functional requirements: How the system operates like the quality of the system
	Examples are Usability, security, performance (execution speed). (- testing)

  - Black box testing: Concerned with what the output is with a certain inputs to test functionality. Can be used to confirm functional and non-functional requirements, but you don’t know how much of the system was tested.

  	Functionality-Based Input Domain Modeling with pairwise testing and all combinations.
  	Boundary value analysis
  	For GUI, record/ playback

  - White box testing: Testing the paths within the code to achieve code coverage, but doesn’t reveal missing functionality. Still checking expected output in the end, may be hard due to many branches and loops. Cons quite complex and expensive.

  	Control flow, data flow, logic coverage

  - integration testing methodologies:
	First the modules have to be ordered by dependencies, then there are 4 methods that determine the order that the modules are tested.

		1. There is Big Bang Integration, where after all the modules are tested, they are all put together and the whole system is tested at once. This makes it difficult to find the root cause of any error.

		2. There is Bottom-Up integration, where the modules with no dependencies are tested first then you connect upwards. This requires drivers with no stubs. The problem is that the lower level is more general routines and error in design at the top level may affect it.

		3. There is Top down integration, where all the top controlling modules are tested first. Less drivers are needed, but need more stubs which are more error prone and complex.

		4. Last is Sandwich integration, where there is a target middle layer and the bottom and top are tested. Tests both the controlling and general purpose routines, but the middle layer modules may not be sufficiently tested.



agile scrum
  Scrum sprints ~ 2 weeks**
  Daily meetings and stating:
    1. What's been done
    2. What to do
    3. Issues

  It is meant to be adaptive to customers changing their requirements

  **Summary**
  I've only heard of scrum sprints, but never been a part of a formal one. A sprint usually lasts 2 weeks and it includes daily meetings that state 'what's been done', 'What needs to be done', and 'current Issues'. The sprint is meant to be adaptive to customers that have changing requirements.

end \\\\\\\\\\\\\\\\


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

####**misc**

- Python lists behind the scenes are dynamic arrays. This means lists allow elements to be added or removed and they will automatically adjust the backing store that holds these elements by allocating or releasing memory. Python lists can hold arbitrary elements—“everything” is an object in Python, including functions. Therefore you can mix and match different kinds of data types and store them all in a single list.

- Java
  - Array.
    int[] data; // create the reference
    data = new int[] {10,20,30,40,50,60,71,80,90,91}; // alias, link the reference to the object

  - ArrayList
    ArrayList is a collection framework used in java that serves as dynamic data structure incorporating the traits of an array

      ArrayList<Integer> array = new ArrayList<Intger>(); // create reference = to object

      //Add elements you wish
      array.add(1);

- C arrays must declare size since it needs to allocate memory on the stack.

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

###**ARM**
13 general purpose registers.

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

####**Modes**
- Protected mode:
  - The Windows operating system domain.
  - 4G of memory with 2G for the system and 2 G for the application
  - Protected mode still uses segment and offset addresses, but the offset address is 32-bits
  - Protection is provided by restricting access through priority levels and access rights
    - When accessing this memory the descriptor describes the base address (starting address) and limit (offset to the ending address) of a segment and the privilege level.

  - Real Mode: the 8086/8088/186 can only operate in this mode. These are microprocessors, 8086 no internal memory but registers to store immediate and final results. Connected to ROM and RAM. 20-bit external address bus provides a 1 MB physical address space (220 = 1,048,576).

    A microprocessor is a computer processor that incorporates the functions of a central processing unit on a single integrated circuit (IC),[1] or at most a few integrated circuits.[2] The microprocessor is a multipurpose, clock driven, register based, digital-integrated circuit that accepts binary data as input, processes it according to instructions stored in its memory, and provides results as output.

####**Paging**
 - paging is a memory management scheme by which a computer stores and retrieves data from secondary storage for use in main memory. In this scheme, the operating system retrieves data from secondary storage in same-size blocks called pages (so in RAM u only need the page table and each there will be references to its pages in secondary memory). Paging is an important part of virtual memory implementations in modern operating systems, using secondary storage to let programs exceed the size of available physical memory.

 - For simplicity, main memory is called "RAM" (an acronym of "random-access memory") and secondary storage is called "disk" (a shorthand for "hard disk drive"), but the concepts do not depend on whether these terms apply literally to a specific computer system.

####**Registers:**
  - Execution Unit (execution of program instructions) 8 multipurpose registers:
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

    - The Instruction Pointer (IP) is updated by theBIU. (or called PC - program counter)
        - EIP (32 bits) in 80386 and up
    - IP contains the offset of the next instruction to be
    fetched from the beginning of the code segment.

    1. controls the address, data, and control busses.
    2. handles instruction fetch and data read/write functions
      Segment registers.
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
      - Lower priority than NMI
    - NMI – non-maskable interrupt
      - edge triggered.
      - must be logic zero for two clock periods before positive edge.
      - must remain held by external device at logic 1 until INTA goes low.
      - Often used for parity errors, power failures and other major faults.

  - A software interrupt is caused either by an exceptional condition or a special instruction in the instruction set which causes an interrupt when it is executed by the processor.
    - INT n – specify interrupt type (32-255), special instruction
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
      1. Push flag register onto stack. (saving state of current process)
      2. Clear IF and TF (interrupt enable and trap flags). Interrupts are now disabled. (So an interrupt cannot be interrupted)
      3. Push CS then IP on stack. (pointer to code of process)
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

###**Multithreading**
####**Process vs Threads**
  **Process**
A process is an instance of a program running in a computer.
  Two essential elements of a process are:
  	1. Program code, which may be shared with other processes that are executing the same program
  	2. A set of data associated with that code, when the processor begins to execute the program code we refer to this executing entity as a process

    PCB (Process control block is managed by the OS and when started it allocates main memory for its code and its associated data):
      PID: process identifier
      State
      Priority
      Program counter, for its code
      Memory pointers, for its data*
      Context data
      I/O status information
      Accounting information

      OS manages a Table of PCBs

    Since PCB contains the critical information for the process, it must be kept in an area of memory protected from normal user access. In some operating systems the PCB is placed in the beginning of the kernel stack of the process since that is a convenient protected location.

Creating a Process is slower due to the child being a duplicate of the parent and has its own allocated memory and stack (Each has its own PCB (process control block)). Takes time to copy. Almost 2 times slower than thread creation.
States: Running, Ready, Blocked. Additional Ready/Suspend, Blocked/Suspend

  N CPUs, processes in running state is maximum N.
  Benefits
  - No risk of data corruption between processes, kept in an area of memory protected from normal user access
  - A crash in one process may not affect others
  - Process states and it is dispatched and scheduled by the OS.

  Cons
  - Need to Mode switch (changes privilege levels) to kernel to be able to Context switch (suspend one process and then retrieving the next process)
    Switching processes need full context switch, can have negative impact on performance since need to load process elements and update the process control blocks.

(When a process needs to access hardware, the kernel takes over and returns a response to the process.)

Suspending a process also suspends all the threads that belong to that process, also with termination.

  **Threads**
Threads share the same memory addresses, that’s why we need synchronization to avoid problems
States: Running, Ready, Blocked
  Benefits
  - Faster creation and termination
  - switching is faster due to no Mode switch
  - Single process can have multiple threads

  cons
  - A crash in a thread may crash the entire process.
  - Have to synchronize

    **User Level threads**
    Pro
    - Scheduling can be application specific
    - Thread switching does not require kernel mode privileges

    Cons
    - A system call from one thread may block all the threads in the process
      a system call is the programmatic way in which a computer program requests a service from the kernel of the operating system it is executed on. A system call is a way for programs to interact with the operating system.

      Services Provided by System Calls :
        Process creation and management
        Main memory management
        File Access, Directory and File system management
        Device handling(I/O)
        Protection
        Networking, etc.

    **Kernel Level threads**
    Pros
    - Management and scheduling done by kernel
    - Threads can be run on multiple processors

    Cons
    - Need mode switch to control another thread.

  Is there speed up by adding more cores?
  	Depending on the application, the overhead of mode and context switching AND needed coordination for the parallel program AND some code needs to be sequential (some not parallelizable algorithm some cores idle) causes the relative speed up to actually not be 1 to 1

  	For databases, there is super linear scaling due to the added cache with added CPUs and multiple instances that require no coordination. Majority of requests are reads so many requests can be handled in parallel.

    Multi instance applications can act in parallel.
      - Like java applications.


####**Creating a new or duplicate process:**
	- In Linux, use
		pid_t pid;
		pid = fork(); // create child process.

####**Creating a thread:**

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

####**C semaphore:**
A semaphore is simply a variable that stores an integer value. This integer can be accessed by two operations: wait() and signal() to coordinate A critical section execution

1. For one whole program
**Init:**

```
	int res;
  sem_t sync_bin_sem;
	// int sem_init(sem_t *sem, int pshared, unsigned int value); if 0 it is shared among threads, if pshared is non-zero means shared with multiple processes so need a shared memory location.
	res = sem_init(&bin_sem, 0, 0);	// 2nd arg is scope
	if (res != 0){
		perror("Semaphore initialization failed.\n");
		exit(EXIT_FAILURE);
	}
 ```

**decrement (wait):**

```
	sem_wait(&bin_sem);// decrement by 1, if sem is <= 0 then it is blocked here
```

**increment (signal):**

```
	sem_post(&bin_sem); // increment by 1, if > 0 it may unblock another thread or process
```

2. If across multiple files, but still same process (program). Include the file and use 'extern sem_t semaphore'

  c ++
  Main file:
   // Declare sem_t
   sem_t sync_emit_and_sensor;

   // and initilze there
   sem_init(&sync_emit_and_sensor, 0, 0);

   sem_destroy(&sync_emit_and_sensor);


   Other file:
   // Make sure the file that creates the semaphore is executed first
   // Must declare that it is in another file
   extern sem_t sync_emit_and_sensor;

   // Now can use in the file
   sem_post(&sync_emit_and_sensor);


3. If multiple programs with same semaphore (Like two processes using shared memory), then need to use:
  Refer to IPC 1.

###**Synchronization** is needed for threads and processes that share a resource.
Need to:
1. Coordinate processes/threads that use shared data. - The OS can block the process/thread instead of doing a busy waiting in a loop for a shared resource, that wastes CPU time on their processor.

2. Use critical sections for sections of code that accesses shared data, we can use semaphores , - A critical section is a segment of code that can be accessed by only one signal process at a certain instance in time. This section consists of shared data resources that need to be accessed by other processes.

  To coordinate access to critical sections we Use semaphores. A semaphore is simply a variable that stores an integer value. This integer can be accessed by two operations: wait() and signal().

\\
Concurrency is the concept of several running tasks that happen within the a time frame without the final outcome being affected, this can mean time sharing a single processor between the tasks or a truly parallel tasks on multiple CPUs.

Parallel means several calculations or programs running simultaneously. 2 processes on 2 CPU running independently.

Concurrency refers to the ability of different parts or units of a program, algorithm, or problem to be executed out-of-order or in partial order, without affecting the final outcome. This can allow for parallel execution of the concurrent units, which can significantly improve overall speed of the execution in multi-processor and multi-core systems.
  - Difficulties:
    - Sharing global resources
    - Hard to locate programming errors as results are not deterministic and reproducible.
    - Hard for OS to manage the allocation of resources optimally.

Hardware support:
  - Interrupt disabling, but only works in uniprocessor and performance is noticeably degraded.

  When Interrupt are disabled then no other process is allowed to perform Context Switch operation that would allow only one process to enter into the Critical State.
\\
critical sections Try to satisfy:
  - Mutual exclusion: only one thread is in its critical section at a time.
	- Progress: If no process is in the critical section, then no other process from outside can block it from entering the critical section. So eventually all processes will progress.
	- Bounded wait: a process will eventually gain control of the processor and not starved/deadlocked. Scheduler should be able to tell a process has been waiting more than a certain amount of time will get access. Picked from blocked queue / Time limit on run for threads/processes.
    For priority based Scheduling:
      - Priority Inversion: high priority task is indirectly preempted by a lower priority task
        Solution: Priority Inheritance: Say L executing its critical section, and H arrives and is blocked for it, so then L inherits H's priority to ensure M cannot preempt H and L.
	- Fairness: If only one process needs to enter the critical section then it should be able to do it immediately.

  **mechanisms provided by OS**
  - Binary Semaphore: only 1 or 0.
    - After arithmetic:
      wait: <= 0, ex sem = 1;
                    sem = sem - 1;
                    if (sem <= 0) wait(sem);

      signal: > 0; ex sem = 0;
                      sem = sem + 1;
                      if (sem > 0) signal(sem);

  - General Semaphores: An integer used for signaling for processes and there are only 3 operations; initialize, decrement (may block a process, wait()), and increment (may unblock a process, signal()).
    they can have any value you want. The max value X they take allows X process/threads to access the shared resource simultaneously.

    - Strong: The process blocked the longest is released from the queue first (FIFO). Guarantees no starvation.
    - Weak: order removed from blocked queue not specified.
          http://cs.pnw.edu/~rlkraft/cs52500-2012/Dijkstra%20(strong)%20vs%20Posix%20(weak)%20semaphores.html
            A "strong semaphore" is one in which an unblocked thread is guaranteed
        to get possession of the semaphore. In a "weak semaphore", an unblocked
        thread must recheck the value of the semaphore variable before it can
        take possession of the semaphore. A weak semaphore can allow one thread
        to starve another tread.


        First, here are "implementations" of strong and weak semaphores that
        can take on negative values. -1, 0, 1

           STRONG                               WEAK
           ------                               ----
        // for this the values are < 0 for wait and >= 0 for post after arithmetic
        P(s)                                  P(s)
        {                                     {
         s = s - 1;                            s = s - 1;
         if (s < 0)                            while (s < 0)  // notice it has to check, during the cycle to check it may be blocked again
         {                                     {
            wait(s);                              wait(s);
         }                                     }
        }                                     }



        V(s)                                  V(s)
        {                                     {
         s = s + 1;                            s = s + 1;
         if (s >= 0)                           if (s >= 0)
         {                                     {
            unblockOneThread(s);                  unblockOneThread(s);
         }                                     }
        }                                     }


  - Mutex: is a lock and the processes that locked the mutex must be the one to unlock it.

  - Condition Variable: Data type used to block

  - Monitor: Ensure mutual exclusion since only one process actively accesses a monitor at one time, it encapsulates procedures for the critical section that .

  - Mail Boxes/Messages: Processes exchange data that may be used for synchronization.

  - Inter-process communications (IPC) facilities:
  	1. Sharing common semaphore, use POSIX, put a sem on shared mem, or Linux facilities below

     defn: POSIX is a family of standards, specified by the IEEE, to clarify and make uniform the application programming interfaces (and ancillary issues, such as commandline shell utilities) provided by Unix-y operating systems. If use linux API that is not standardized porting to other unix systems may be difficult.

    Must implement:
      set inital sem value with semctl
      delete sem with semctl
      wait function with semop
      signal function with semop

    ```
      #include <sys/sem.h> // The header file sys/sem.h usually relies on two other header files, sys/types.h and sys/ipc.h.

    	int semctl(int sem_id, int sem_num, int command, ...); // The semctl function allows direct control of semaphore information

        The first parameter, sem_id, is a semaphore identifier, obtained from semget. The sem_num parameter
        is the semaphore number. You use this when you’re working with arrays of semaphores. Usually, this is
        0, the first and only semaphore. The command parameter is the action to take, and a fourth parameter, if
        present, is a union semun, which according to the X/OPEN specification must have at least the following
        members:
          union semun {
            int val;
            struct semid_ds *buf;
            unsigned short *array;
          }

        Most versions of Linux have a definition of the semun union in a header file (usually sem.h), though
        X/Open does say that you have to declare your own. If you do find that you need to declare your own,
        check the manual pages for semctl to see if there is a definition given. If there is, we suggest you use
        exactly the definition given in your manual, even if it differs from that given here.

        There are many different possible values of command allowed for semctl. Only the two that we describe
        here are commonly used. For full details of the semctl function, you should consult the manual page.
        The two common values of command are:
          ❑ SETVAL: Used for initializing a semaphore to a known value. The value required is passed as the
          val member of the union semun. This is required to set the semaphore up before it’s used for
          the first time.
          ❑ IPC_RMID: Used for deleting a semaphore identifier when it’s no longer required.

        The semctl function returns different values depending on the command parameter. For SETVAL and
        IPC_RMID it returns 0 for success and –1 on error.

      // --

    	int semget(key_t key, int num_sems, int sem_flags);  // The semget function creates a new semaphore or obtains the semaphore key of an existing semaphore

        The first parameter, key, is an integral value used to allow unrelated processes to access the same semaphore.
        All semaphores are accessed indirectly by the program supplying a key, for which the system then
        generates a semaphore identifier. The semaphore key is used only with semget. All other semaphore
        functions use the semaphore identifier returned from semget.

        There is a special semaphore key value, IPC_PRIVATE, that is intended to create a semaphore that only
        the creating process could access, but this rarely has any useful purpose. You should provide a unique,
        non-zero integer value for key when you want to create a new semaphore.

        The num_sems parameter is the number of semaphores required. This is almost always 1.

        The sem_flags parameter is a set of flags, very much like the flags to the open function. The lower nine
        bits are the permissions for the semaphore, which behave like file permissions. In addition, these can be bitwise
        ORed with the value IPC_CREAT to create a new semaphore. It’s not an error to have the IPC_CREAT
        flag set and give the key of an existing semaphore. The IPC_CREAT flag is silently ignored if it is not
        required. You can use IPC_CREAT and IPC_EXCL together to ensure that you obtain a new, unique semaphore.
        It will return an error if the semaphore already exists.

        The semget function returns a positive (nonzero) value on success; this is the semaphore identifier used
        in the other semaphore functions. On error, it returns –1.

      // --
    	int semop(int sem_id, struct sembuf *sem_ops, size_t num_sem_ops); // The function semop is used for changing the value of the semaphore; num_sem_ops is number of semaphores

        The first parameter, sem_id, is the semaphore identifier, as returned from semget.

        The second parameter,
        sem_ops, is a pointer to an array of structures, each of which will have at least the following members:
          struct sembuf {
            short sem_num;
            short sem_op;
            short sem_flg;
          }
        The first member, sem_num, is the semaphore number, usually 0 unless you’re working with an array
        of semaphores.

        The sem_op member is the value by which the semaphore should be changed. (You can
        change a semaphore by amounts other than 1.) In general, only two values are used, –1, which is your P
        operation to wait for a semaphore to become available, and +1, which is your V operation to signal that a
        semaphore is now available.

        The final member, sem_flg, is usually set to SEM_UNDO. This causes the operating system to track the
        changes made to the semaphore by the current process and, if the process terminates without releasing
        the semaphore, allows the operating system to automatically release the semaphore if it was held by this process. It’s good practice to set sem_flg to SEM_UNDO, unless you specifically require different behavior.

        If you do decide you need a value other than SEM_UNDO, it’s important to be consistent, or you can get very
        confused as to whether the kernel is attempting to “tidy up” your semaphores when your process exits.

        All actions called for by semop are taken together to avoid a race condition implied by the use of multiple
        semaphores. You can find full details of the processing of semop in the manual pages.

    ```

	  2. Shared memory: It allows two unrelated processes to access the
same logical memory. Shared memory is a very efficient way of transferring data between two running
processes. A special range of addresses that is created by IPC for one process and appears in the
address space of that process. Other processes can then “attach” the same shared memory segment into
their own address space. All processes can access the memory locations just as if the memory had been
allocated by malloc . If one process writes to the shared memory, the changes immediately become visible
to any other process that has access to the same shared memory.

```
	#include <sys/shm.h>

	void *shmat(int shm_id, const void *shm_addr, int shmflg); // When you first create a shared memory segment, it’s not accessible by any process. To enable access to the
shared memory, you must attach it to the address space of a process. You do this with the shmat function.

    The first parameter, shm_id, is the shared memory identifier returned from shmget.

    The second parameter, shm_addr, is the address at which the shared memory is to be attached to the
    current process. This should almost always be a null pointer, which allows the system to choose the
    address at which the memory appears.

    The third parameter, shmflg, is a set of bitwise flags. The two possible values are SHM_RND, which, in conjunction
    with shm_addr, controls the address at which the shared memory is attached, and SHM_RDONLY,
    which makes the attached memory read-only. It’s very rare to need to control the address at which shared
    memory is attached; you should normally allow the system to choose an address for you, because doing
    otherwise will make the application highly hardware-dependent.

    If the shmat call is successful, it returns a pointer to the first byte of shared memory. On failure –1
    is returned.
  // --

	int shmctl(int shm_id, int cmd, struct shmid_ds *buf);

    The shmid_ds structure has at least the following members:
      struct shmid_ds {
        uid_t shm_perm.uid;
        uid_t shm_perm.gid;
        mode_t shm_perm.mode;
      }

    The first parameter, shm_id, is the identifier returned from shmget.

    The second parameter, command, is the action to take. It can take three values, shown in the following table.

    The third parameter, buf, is a pointer to the structure containing the modes and permissions for the
    shared memory.

    On success, it returns 0, on failure, –1.

  // --

	int shmdt(const void *shm_addr); // The control functions for shared memory

    The shmdt function detaches the shared memory from the current process. It takes a pointer to the address
    returned by shmat. On success, it returns 0, on error –1. Note that detaching the shared memory doesn’t
    delete it; it just makes that memory unavailable to the current process.
    // --

  int shmget(key_t key, size_t size, int shmflg); // You create shared memory using the shmget function

    // As with semaphores, the program provides key, which effectively names the shared memory segment,
    and the shmget function returns a shared memory identifier that is used in subsequent shared memory
    functions. There’s a special key value, IPC_PRIVATE, that creates shared memory private to the process.
    You wouldn’t normally use this value, and you may find the private shared memory is not actually private
    on some Linux systems.

    The second parameter, size, specifies the amount of memory required in bytes.

    The third parameter, shmflg, consists of nine permission flags that are used in the same way as the mode
    flags for creating files. A special bit defined by IPC_CREAT must be bitwise ORed with the permissions to
    create a new shared memory segment. It’s not an error to have the IPC_CREAT flag set and pass the key of
    an existing shared memory segment. The IPC_CREAT flag is silently ignored if it is not required.

    The permission flags are very useful with shared memory because they allow a process to create shared
    memory that can be written by processes owned by the creator of the shared memory, but only read by
    processes that other users have created. You can use this to provide efficient read-only access to data
    by placing it in shared memory without the risk of its being changed by other users.

    If the shared memory is successfully created, shmget returns a nonnegative integer, the shared memory
    identifier. On failure, it returns –1.
 ```
---
	Ex. (same process as creating a shared semaphore in [1])
	#include "shm_com.h"	// shared memory structure for both consumer and producer to use, has a flag within to indicate which process will continue. int written_by_you;

  Producer
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


	printf("Memory attached at %X\n", (int)shared_memory);

	// assign shared_memory to shared stuff. USE IT
	shared_stuff = (struct shared_use_st *)shared_memory;	//point to first byte
	shared_stuff->written_by_you = 0;
	strncpy(shared_stuff->some_text, buffer, TEXT_SZ); // buffer to some_text



	// after finished, detach from shared memory
	if (shmdt(shared_memory) == -1){
		fprintf(stderr, "shmdt failed\n");
		exit(EXIT_FAILURE);
	}

	// only one of the users of the shared memory must delete it.
	if(shmctl(shmid, IPC_RMID, 0) == -1){
		fprintf(stderr,"shmctl(IPC_RMID) failed\n");
		exit(EXIT_FAILURE);
	}

  ```
  consumer
  ```
  // Still create with same key, if existing OK.
  shmid = shmget((key_t)1234, sizeof(struct shared_use_st), 0666 | IPC_CREAT);

  // attach
  shared_memory = shmat(shmid, (void *)0, 0);
  if (shared_memory == (void*)-1){
    fprintf(stderr, "shmat failed\n");
    exit(EXIT_FAILURE);
  }

  shared_stuff = (struct shared_use_st *)shared_memory;

  // unlink
  if (shmdt(shared_memory) == -1){
    fprintf(stderr, "shmdt(shared_memory) failed\n");
    exit(EXIT_FAILURE);
  }

  ```

	// If we need to use semaphores on shared memory we can either put the semaphore on in shared memory or share named POSIX semaphores.
		1. share named POSIX semaphores

      Consumer
      ```

    #include <sys/shm.h>
    #include <semaphore.h>  // for POSIX semaphore
    #include <fcntl.h>      // this also needed

    #include <errno.h>

    #include "sh_arrayStruct.h" // The shared structure

		//Choose a name for your semaphore
		#define SNAME "/mysem" ~~

    //main
			//Use sem_open with O_CREAT in the process that creates them
			sem_t *sem = sem_open(SNAME, O_CREAT, 0644, 3); /* Initial value is 3. */
			errno=0;  /* <---- This is an important thing I learned when using errno. */
			if (sem == SEM_FAILED)
			   {
			   fprintf(stderr, "sem_open() failed.  errno:%d\n", errno);
			   ...

      sem_wait(sem);
      sem_post(sem);


      // The sem_unlink() function removes the semaphore identified by name and marks the semaphore to be destroyed once all processes cease using it (this may mean immediately, if all processes that had the semaphore open have already closed it).
      sem_close(sem);
      sem_unlink(SEM_NAME);
      ```

      Producer
      ```
      // name semaphore and is same name of existing semaphore ~~
      #define SEM_NAME "/mysem"

  		// open the existing semaphore so it can use it.
  		sem_t *sem = sem_open(SEM_NAME, 0); /* Open a preexisting semaphore. */

      // close the semaphore for this process, the semaphore remains in the system
      sem_close(sem);
  		```
    ---
		2. Putting a sem in shared memory.
---
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
---
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

  Message queues provide a reasonably easy and efficient way of passing data between two unrelated
  processes. They have the advantage over named pipes that the message queue exists independently of
  both the sending and receiving processes, which removes some of the difficulties that occur in synchronizing
  the opening and closing of named pipes.

  Unlike in the pipes example, there’s no need for the processes to provide their own synchronization
  method. This is a significant advantage of messages over pipes.

  // msg2 write strings with terminating /0 into buffer, then msg1 is ran and it reads from the queue.

  ```

  #include <sys/msg.h>

  int msgctl(int msqid, int cmd, struct msqid_ds *buf); // The final message queue function is msgctl, which is very similar to that of the control function for
shared memory. ex IPC_RMID

  int msgget(key_t key, int msgflg); // You create and access a message queue using the msgget function

  int msgrcv(int msqid, void *msg_ptr, size_t msg_sz, long int msgtype, int msgflg); // The msgrcv function retrieves messages from a message queue

  int msgsnd(int msqid, const void *msg_ptr, size_t msg_sz, int msgflg); // The msgsnd function allows you to add a message to a message queue
  ```

In Java:
  - Synchronization
  Use 'synchronized' keyword to only allow one thread to access a method or data structure / object at one time.

  - Multithreading
  1. public void run(); // So when we do thread.start() it executes this method.
  2. Thread(Runnable threadObj, String threadName); // Create the thread with the object that has a runnable interface.
  3. thread.start(); // to call the run() method.

  process/thread completion on time checks.
  - Rate monotonic scheduling
  - Cyclic Executive


###**Network programming**
  - TCP / IP:
    Transmission Control Protocol: Connection-oriented (Handshaking), point to point, reliable (in order), flow and congestion control, full duplex.

    The Model
    1. The application layer provides applications with standardized data exchange. Its protocols include the Hypertext Transfer Protocol (HTTP), File Transfer Protocol (FTP), Post Office Protocol 3 (POP3), Simple Mail Transfer Protocol (SMTP) and Simple Network Management Protocol (SNMP).

    2. The transport layer is responsible for maintaining end-to-end communications across the network. TCP handles communications between hosts and provides flow control, multiplexing and reliability. The transport protocols include TCP and User Datagram Protocol (UDP), which is sometimes used instead of TCP for special purposes.

    3. The network layer, also called the internet layer, deals with packets and connects independent networks to transport the packets across network boundaries. The network layer protocols are the IP and the Internet Control Message Protocol (ICMP), which is used for error reporting.

    4. The physical layer consists of protocols that operate only on a link -- the network component that interconnects nodes or hosts in the network. The protocols in this layer include Ethernet for local area networks (LANs) and the Address Resolution Protocol (ARP).

  - User Datagram protocol (UDP): Connectionless data transfer, has error checking with checksum, etc.
    java

      ```
      byte[] sendBuf;
      int sendLen;

      InetAddress remoteIpAddress;
	    int remotePort;

      DatagramPacket packet = null;

      //DatagramPacket(byte[] buf, int length, InetAddress address, int port)
      packet = new DatagramPacket(sendBuf, sendLen + 4, remoteIpAddress, remotePort);
			rcvHanlder.transferSocket.send(packet);
      ```
###**Deadlocks**
####**Definition**
Is a permanent blocking of a set of processes that compete for a system resource or communicate with each other.
A set of processes are deadlocked when each process in the blocked set are waiting for an event that can only be triggered by another processes that is also blocked.

It is permanent and there is no efficient solution.

####**notes**

Many OS let the user deal with deadlocks.
An OS can do avoidance by checking if a deadlock is possible and being conservative when allocating resources.
Can also deal with it when a deadlock occurs, it may be easy to solve.

2 resource categories
- Reusable: Can be safely used by only one process at a time and is not depleted by that use. Examples are:
  Processors, main and secondary memory, data structures.
- Consumable: Can be created(produced) and destroyed(consumed). Examples are:
  interrupts, signals, messages, I/O buffers.

Approaches that an OS can take for deadlocks:
1. Prevention:
  - Resource Allocation policy: Conservative, it under commits resources.
  - Different schemes: Requesting all the resources it needs at once, Preemption(forcibly remove resources), and Resource ordering.
2. Avoidance: Dynamic choices based on current resource allocation state. Must know future process requests.
  - Resource Allocation policy: Midway between detection and prevention
  - Scheme: Manipulate to find a safe path for allocation
    - Needs to know future resource requirements for all processes.
  - Approaches:
    1. Resource Allocation Denial: Do not grant an incremental resource request to process if this allocation might lead to deadlock.
    2. Process Initialization Denial: Do not start a process if its demands might lead to deadlock.
  - Algorithms:
    - Banker Algorithm:
      :State: reflects the current allocation of resources to processes
      :Safe State: There is at least one sequence of resource allocations to processes that does not result in a deadlock.
      :Unsafe state: Not safe, deadlock.
3. Detection:
  - Liberal, Requested resources are granted whenever possible.
  - Scheme: Invoke periodically to test if there is a deadlock.

Some conditions for a deadlock:
1. Mutual Exclusion: Only one process may use a resource at a time
2. Hold and wait: A process holds allocated resources while awaiting something.
  - Prevention: Have a process request all of its required resources at one time and block it until all the requests can be granted simultaneously.
3. No Pre-emption: no resource can be forcibly removed from a process holding it.
  - Prevention: if a process holding certain resources is denied a further request, that process must release its original resources and request them again.
    - Also define a linear ordering of resource types.
4. Circular wait: closed chain of processes where each process holds at least one resource needed by the next process in the chain.

####**Recovery Strategies**
1. Abort all deadlocked Processes
2. Back up each deadlocked process to some previously defined checkpoint and restart all processes.
3. One by one abort deadlocked processes until deadlock no longer exists.
4. One by one abort preempt (remove from processes) until deadlock no longer exists.

Dining Philosophers problem:
  Definition:
    - 5 Philosophers and 5 forks.
    - No two Philosophers can use the same fork at the same time (mutual exclusion)
    - No starvation of Philosophers (avoid deadlock and starvation)

  Solutions:
    - If a philosopher cannot get both forks then they are put in the waiting queue. Monitor is good for this since entering a monitor guarantees both forks.
    - If using semaphores only allow max 4 philosophers for the 5 forks.


###**Databases**
####**Relational DB**
A relational database at its simplest is a set of tables used for storing data. Each table has a unique name and may relate to one or more other tables in the database through common values.

Tables:
A table in a database is a collection of rows and columns. Tables are also known as entities or relations.

Rows:
A row contains data pertaining to a single item or record in a table. Rows are also known as records or tuples.

Columns:
A column contains data representing a specific characteristic of the records in the table. Columns are also known as fields or attributes.

Relationships:
A relationship is a link between two tables (i.e, relations). Relationships make it possible to find data in one table that pertains to a specific record in another table.

Datatypes:
Each of a table's columns has a defined datatype that specifies the type of data that can exist in that column. For example, the FirstName column might be defined as varchar(20), indicating that it can contain a string of up to 20 characters. Unfortunately, datatypes vary widely between databases.

Primary Keys:
Most tables have a column or group of columns that can be used to identify records. For example, an Employees table might have a column called EmployeeID that is unique for every row. This makes it easy to keep track of a record over time and to associate a record with records in other tables.

Foreign Keys:
Foreign key columns are columns that link to primary key columns in other tables, thereby creating a relationship. For example, the Customers table might have a foreign key column called SalesRep that links to EmployeeID, the primary key in the Employees table.

Relational Database Management System:
A Relational Database Management System (RDBMS), commonly (but incorrectly) called a database, is software for creating, manipulating, and administering a database. For simplicity, we will often refer to RDBMSs as databases.

#####**Commercial DB**
Oracle:
Oracle is the most popular relational database. It runs on both Unix and Windows. It used to be many times more expensive than SQL Server and DB2, but it has come down a lot in price.

SQL Server:
SQL Server is Microsoft's database and, not surprisingly, only runs on Windows. It has only a slightly higher market share than Oracle on Windows machines. Many people find it easier to use than Oracle.

#####**Open Source DB**
MySQL:
Because of its small size, its speediness, and its very good documentation, MySQL has quickly become the most popular open source database. MySQL is available on both Windows and Unix, but it lacks some key features such as support for stored procedures.

####**Non Relational DB**
https://www.jamesserra.com/archive/2015/08/relational-databases-vs-non-relational-databases/
Also called NoSQL databases, the most popular being MongoDB, DocumentDB

most non-relational databases that are in the categories Document stores and Column stores can also be used for OLTP, adding to the confusion.  OLTP databases can be thought of as “Operational” databases, characterized by frequent, short transactions that include updates and that touch a small amount of data and where concurrency of thousands of transactions is very important (examples including banking applications and online reservations).  Integrity of data is very important so they support ACID transactions (Atomicity, Consistency, Isolation, Durability).  This is opposed to data warehouses, which are considered “Analytical” databases characterized by long, complex queries that touch a large amount of data and require a lot of resources.  Updates are infrequent.  An example is analysis of sales over the past year.

###**Testing**
- Application Under Test (AUT)
- Unit testing, white box testing (data coverage, code coverage), black box testing (input testing)

###**Standard Programming Practices**
  - Clear definition, High cohesion (class does has clear goal.)
  - Low coupling between modules.
  - Encapsulation: The module has data and the functions it contains only deal with that data.
  - Simple to use
  - Readability
  - Testability

###**GUI design**


###**Agile**
####**Scrum sprints ~ 2 weeks**
Daily meetings and stating:
  1. What's been done
  2. What to do
  3. Issues

It is meant to be adaptive to customers changing their requirements

###**Projects:**

A Single Board Computer(SBC) is a printed circuit board (PCB) with a microcontroller and all components needed to make it function as a small computer

####**RPI: Touch screen**
  The project was a system that helped tourist find locations of interest in a city, and my part was to create a touch screen kiosk that hosted the application so people without internet access could use it. I used a raspberry pi and PiFace to control the circuits that enabled an infrared touch screen surface. The main idea is to have 1 column of 8 infrared emitters on one side of the screen and a column of 8 infrared transistors on the other to create a touch screen area in between. The general operation is to have a single emitter on at a time and all the sensors would check if they can detect the ON emitter. If it doesn’t it means something was in the way. After cycling through the emitters, it will check if an intercept can be calculated.
  To test and visualize if the correct location was touched on the screen, I wrote an (visual studio (c sharp)) application that received the touch location and showed which lines were being blocked to cause the intercept.

  **RPI experience summary**
  Most of the Raspberry pi experience is from my 4th year project where I used a raspberry pi and PiFace to control the circuits that enabled an infrared touch screen surface. It was fairly simple, mainly synchronizing the turning on of an infrared LED and then reading the sensors.
    - The main idea is to have 1 column of 8 infrared emitters on one side of the screen and a column of 8 infrared transistors on the other to create a touch screen area in between. The general operation is to have a single emitter on at a time and all the sensors would check if they can detect the ON emitter. If it doesn’t it means something was in the way. After cycling through the emitters, it will check if an intercept can be calculated.

####**Arduino: maze robot:**
  Using an Arduino nano connected to an H bridge (4 pins to control direction of the 2 motors (2 pins for each)) to control the motors and to infrared and sonar sensors, the project was to have a maze robot self navigate a line and a wall maze by combining multiple sensor's data and changing motor behaviour accordingly.

	Using an Arduino uno and Raspberry PI, the project was a LED globe to attempt the Persistance of vision illusion, the idea is to spin a single vertical array of LEDs on a 2D ring fast enough, 30 frames per second, that it creates the illusion of a solid image when the LEDs and motor are synced. The pi just controlled the motor speed and the arduino was attached onto the spinning ring.

####**TFTP**

  The server was multithreaded to handle multiple requests in parallel, it handled read and write requests and had error handling for incorrect packets, like wrong block number (for ack and data) or wrong transfer ID and network errors. TFTP used UDP datagrams and added reliability like handshaking and in order transfers. (Testing was with microsoft’s TFTP client to test the server, to test the whole system with the group’s client was using an error simulator in the middle that would simulate packet and network errors like (duplicate, drops).

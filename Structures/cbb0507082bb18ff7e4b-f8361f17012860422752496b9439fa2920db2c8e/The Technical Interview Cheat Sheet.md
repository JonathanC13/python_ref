## Studying for a Tech Interview Sucks, so Here's a Cheat Sheet to Help

This list is meant to be a both a quick guide and reference for further research into these topics.  It's basically a summary of that comp sci course you never took or forgot about, so there's no way it can cover everything in depth.  It also will be available as a [gist](https://gist.github.com/TSiege/cbb0507082bb18ff7e4b) on Github for everyone to edit and add to.

## Data Structure Basics

###**Array**
####Definition:
- Stores data elements based on an sequential, most commonly 0 based, index.
- Based on [tuples](http://en.wikipedia.org/wiki/Tuple) from set theory.
- They are one of the oldest, most commonly used data structures.  

####What you need to know:
- Optimal for indexing (direct access to indices); bad at searching, inserting, and deleting (except at the end).
- **Linear arrays**, or one dimensional arrays, are the most basic.
  - Are static in size, meaning that they are declared with a fixed size.
- **Dynamic arrays** are like one dimensional arrays, but have reserved space for additional elements.
  - If a dynamic array is full, it copies it's contents to a larger array. (larger memory space)
- **Two dimensional arrays** have x and y indices like a grid or nested arrays.  

####Big O efficiency:
- Indexing:         Linear array: O(1),      Dynamic array: O(1)
- Search:           Linear array: O(n),      Dynamic array: O(n)
- Optimized Search: Linear array: O(log n), Dynamic array: O(log n)
- Insertion:        Linear array: n/a        Dynamic array: O(n)

####**summary**
**Linear array**
- It is a data structure that stores data elements sequentially and it has to be declared with a fixed size. It is optimal for indexing since you have direct access to the indices, Big O of O of 1, but it is bad for inserting and deleting, Big O of O of n, except at the very end, since you have to shift the elements if it takes place within the array.

**Dynamic Arrays**
- Are like linear arrays where it stores data elements sequentially and is optimized for indexing,
- Is a data structure that will attempt to grow if you want to do an insertion when it is full, either it will grow in the same memory location if there is space or into a larger memory space elsewhere. (copying in larger array)

**Two dimensional arrays**
- Built to have x and y indices like a grid or nested arrays to represent something like a matrix or r,g,b values for an image.

####

###**Linked List**
####Definition:
- Stores data with **nodes** that point to other nodes.
  - Nodes, at its most basic it has one datum and one reference (another node).
  - A linked list _chains_ nodes together by pointing one node's reference towards another node.  
  - in C, declare a struct for a node that has a variable for the element and a variable to point to the next node.

####What you need to know:
- Designed to optimize insertion and deletion, slow at indexing and searching (follow the chain).
- **Doubly linked list** has nodes that reference the previous node (enables backward traversal, quicker insertion and deletion if not always reseting the to the head). (w/o you would need two pointers traversing)
- **Circularly linked list** is simple linked list whose **tail**, the last node, references the **head**, the first node.
- **Stack**, commonly implemented with linked lists but can be made from arrays too.
  - Stacks are **last in, first out** (LIFO) data structures.
  - Made with a linked list by having the head be the only place for insertion and removal.
- **Queues**, too can be implemented with a linked list or an array.
  - Queues are a **first in, first out** (FIFO) data structure.
  - Made with a doubly linked list that only removes from head and adds to tail.  

####Big O efficiency:
- Indexing:         Linked Lists: O(n)
- Search:           Linked Lists: O(n)
- Optimized Search: Linked Lists: O(n)
- Insertion:        Linked Lists: O(1)  ; operation itself is O(1), still need to traverse

###**Linked List searches**
- Only linear with iterative or recursion since you don't have direct access to elements of linked lists. Would need to traverse more than simply doing a linear search.

###**Linked List sort**
- Merge sort is often preferred for sorting a linked list. The slow random-access performance of a linked list makes some other algorithms (such as quicksort) perform poorly, and others (such as heapsort) completely impossible.
- Steps: (need the size)
  1. Divide the list into the smallest unit, which is one element. 2 halves represented as a and b.
  2. Compare each half and order and merge them. Update the head reference to the smallest value element.

####**summary**
**linked lists**
- A linked list contains nodes, which have space for the data and a reference, and it chains these nodes together by pointing a node's reference to another node. It is designed to optimize insertion and deletion, Big O of O of 1, but it is slow at indexing and searching, Big O of O of n, since you have to follow the links (can be very scattered memory locations).

**Doubly Linked list**
- In a Doubly linked list, each node has an additional reference that points to the previous node to enable backward traversal, this makes insertion and deletion quicker since you don't need traverse with additional pointers to perform the operations.

**Linked List searches**
- A linear search for a linked list is effective since you don't have direct access to elements of linked lists with indices.

**Linked List sort**
- Merge sort is often preferred for sorting a linked list. The slow random-access performance of a linked list makes some other algorithms (such as quicksort) perform poorly. It starts by continuously halving the dataset until the smallest unit of 1 element, then it orders the elements by pairs as it merges back into one complete set. Average Time complexity Big O of O of n log n.

**Circularly linked list**
- It is a simple linked list whose **tail** references the **head** of the linked list.

**Stack**
- Stacks are Last In, First out (LIFO) data structures and is commonly implemented with linked lists where the head is the only place for insertion and removal.

**Queues**
- Queues are First in, First Out (FIFO) data structures and can be implemented with a linked lists where removal happens at the head and insertion at the tail.

####

##Search for Arrays. http://bigocheatsheet.com/
###**Linear Search**
####Definition:
- Start from the beginning (leftmost) and iterate until the element matches.
- Sorted or Non Sorted arrays

####Big O efficiency:
- Best:   O(1) ; O(1) means first element found? I think so
- Worst:  O(n)

####**summary**
- Works for a sorted or unsorted array, starting at the leftmost index we iterate one by one until the target is found or the end of the array. Worst time complexity Big O of O of n.

###**Binary Search**
####Definition:
- Given a SORTED array, divide the array in half and compare that pivot to the search value and which half to divide next if still looking

####Big O efficiency:
- Best:   O(1)
- Worst:  O(log n)

####**summary**
- Given a sorted array, we divide the array in half and compare that pivot to the target then if the target is lower than the pivot we divide into the left side, if it is greater we divide into the right side. It continues until the pivot is equal to the target or not found. Worst complexity of O of log n.

###**Jump Search**
####Definition:
- For SORTED array, check fewer elements by firstly jumping ahead a set amount until found or the array value is greater than searched for value, then jump back until the array value is lower. Finally do a linear search within the min and max for the searched for value.
- This approach is better than Binary if it is costly to jump backward in the array, since Jump search may only jump back once.

####Big O efficiency
- Best:   (1)
- Worst:  O(sqrt(N))

####**summary**
- Given a sorted array, starting from the base it iterates by jumping a fixed number of steps until the element is greater than the target to set the max, then it does one jump back to set the min. From the range min to max it conducts a linear search to find the target. Worst Time complexity of O of square root n. (larger than log n)

###**Sublist Search (Search a linked list in another list)**
####Definition:
- If the first list is present in the second list.

####Methods:
#####**Linear**:
- Start matching the pattern at the leftmost index and if there is a mismatch, increment the index by 1. It is brute force method to check all alignments. The time complexity is O of m times n, where m is the size of the list and n is the size of the pattern.

- O(m*n), m is number of nodes in the first list and n in second.

####**Knuth–Morris–Pratt_algorithm**
- Instead of just incrementing the index by 1 when a mismatch occurs, since you know where the mismatch happened the new index for the search can be at that position (just in case to match head of pattern), unless there is a partial match you may need to backtrack from the new index (build a look up table to check how much to backtrack). The time complexity is O of n, where n is the length of the string.

- Θ(n), n is the length of the String.

####**Boyer–Moore string-search algorithm**
- Skips ahead and matches on the tail of a pattern instead of the head.
- Hard to understand atm


###**Hash Table or Hash Map**
####Definition:
- Stores data with key value pairs.
- **Hash functions** accept a key and return an output unique only to that specific key.
  - This is known as **hashing**, which is the concept that an input and an output have a one-to-one correspondence to map information.
  - Hash functions return a unique address in memory for that data.

####What you need to know:
- Designed to optimize searching, insertion, and deletion.
- **Hash collisions** are when a hash function returns the same output for two distinct inputs. Solutions are open addressing (find next available spot) or chaining (existing at same hash location but they link together).
  - All hash functions have this problem.
  - This is often accommodated for by having the hash tables be very large.
- Hashes are important for associative arrays and database indexing.

####Big O efficiency:
- Indexing:         Hash Tables: O(1)
- Search:           Hash Tables: O(1)
- Insertion:        Hash Tables: O(1)

####**summary**
- Hash tables/maps store data with key value pairs and has the concept of hashing where the input and output have a one-to-one correspondence to map information. It is optimized for searching, insertion, and deletion, Big O of O of 1.

- Internally Hash Map contains an array of Nodes and a nodes is represented as a class which contains 4 fields: int hash, key, value, reference next. The Nodes are stored in an array, if a hash collision occurs, the reference will of the first node will connect to the second, so they both are stored at the same index.


###**Binary Tree**
####Definition:
- Is a tree like data structure where every node has at most two children.
  - There is one left and right child node. Top node is the root.

####What you need to know:
- Designed to optimize searching (When sorted very simple traversal to find value) and sorting (Easy reference changes).
- A **degenerate tree** is an unbalanced tree, which if entirely one-sided is a essentially a linked list.
- They are comparably simple to implement than other data structures.
- Used to make **binary search trees**.
  - A binary tree that uses comparable keys to assign which direction a child is.
  - Left child has a key smaller than it's parent node.
  - Right child has a key greater than it's parent node.
  - There can be no duplicate node.
  - Because of the above it is more likely to be used as a data structure than a binary tree.

####Big O efficiency:
- Indexing:  Binary Search Tree: O(log n)
- Search:    Binary Search Tree: O(log n)
- Insertion: Binary Search Tree: O(log n)

####**summary**
**binary tree**
- Is a  data structure where every node has at most two children, left and right child. It is optimized for (searching - only search tree?), insertion, and deletion if the tree remains balanced.

**binary search tree**
- Is a sorted tree with no duplicates that uses the node as a comparable key to its children, the left child is less than the parent and the right node is greater than the parent. Optimized for searching and sorting, assuming it is balanced. Search Big O of O of log n.

####

####**Creating the binary search tree**
#####**Tree Sort**
- If given a binary tree must copy into an array first (Breadth or Depth depending on the tree). If already in an array, ok.

- Unsorted array
  - Start with the first element as the root node and insert based on left child is less and right child is greater value. This most likely creates a sorted but unbalanced binary search tree.

- Sorted Linked List. Balanced Binary search tree https://www.geeksforgeeks.org/?p=17063
  - Method 1: Time complexity: O(n Log n).
    - 1. Make the middle element of the linked list the root.
    - 2. Recursively get the middle element from the left and make it the left child of the root.
    - 3. Repeat step 2 but with the right side of root.
  - Method 2; O(n).
  - In this method, we construct from leaves to root. The idea is to insert nodes in BST in the same order as the appear in Linked List, so that the tree can be constructed in O(n) time complexity.
    - After counting nodes, we take left n/2 nodes and recursively construct the left subtree. After left subtree is constructed, we allocate memory for root and link the left subtree with root. Finally, we recursively construct the right subtree and link it with root.
    While constructing the BST, we also keep moving the list head pointer to next so that we have the appropriate pointer in each recursive call.

- Sorted Array: O(n) easier than linked list due to direct access to the middle in O(1)
  - 1. Make the middle element of the linked list the root.
  - 2. Recursively get the middle element from the left and make it the left child of the root.
  - 3. Repeat step 2 but with the right side of root.

#####**Balancing**
- Must keep track of the height of the left and right sub tree. The balance factor of a balanced tree can be -1, 0, or +1. balance_factor := height(right_subtree) - height(left_subtree)
  - During insertion and deletion, compare at what height the operation is happening and if at a leaf, adjust the height values.
- When an imbalance happens then the rotations (single or double) and/or element link changes are needed.

###****
- AVL tree or height balanced binary tree
  - it is a variation of the Binary tree where height difference between left and right sub tree can be at most 1. If at any time they differ by more than one, rebalancing is done to restore this property. Lookup, insertion, and deletion all take O(log n) time in both the average and worst cases, where n is the number of nodes in the tree prior to the operation.

- Red-Black tree:
  - Another variant of binary tree similar to AVL tree it is a self balancing binary search tree. In this tree nodes are either colored red or black. the number of black nodes from the root to a node is the node's black depth; the uniform number of black nodes in all paths from root to the leaves is called the black-height of the red–black tree.



## Search Basics
###**Breadth First Search**
####Definition:
- An algorithm that searches a tree (or graph) by searching levels of the tree first, starting at the root.
  - It finds every node on the same level, most often moving left to right.
  - While doing this it tracks the children nodes of the nodes on the current level.
  - When finished examining a level it moves to the left most node on the next level.
  - The bottom-right most node is evaluated last (the node that is deepest and is farthest right of it's level).

####What you need to know:
- Optimal for searching a tree that is wider than it is deep.
- Uses a queue to store information about the tree while it traverses a tree.
  - Because it uses a queue it is more memory intensive than **depth first search**.
  - The queue uses more memory because it needs to stores pointers

####Big O efficiency:
- Search: Breadth First Search: O(|E| + |V|)
- E is number of edges
- V is number of vertices (parent with 2 children)

####**summary**
- An algorithm that searches a tree by searching levels first starting at the root. It searches each level from left to right, so it is optimized for a tree that is wider than it is deep. Searching Big O is O of Edges + parents that have 2 children.
- The tree node information can be stored using a queue since after searching through one level, it returns to the head and starts checking the next level from that node.

###**Depth First Search**
####Definition:
- An algorithm that searches a tree (or graph) by searching depth of the tree first, starting at the root.
  - It traverses left down a tree until it cannot go further.
  - Once it reaches the end of a branch it traverses back up trying the right child of nodes on that branch, and if possible left from the right children.
  - When finished examining a branch it moves to the node right of the root then tries to go left on all it's children until it reaches the bottom.
  - The right most node is evaluated last (the node that is right of all it's ancestors).

####What you need to know:
- Optimal for searching a tree that is deeper than it is wide.
- Uses a stack to push nodes onto.
  - Because a stack is LIFO it does not need to keep track of the nodes pointers and is therefore less memory intensive than breadth first search.
  - Once it cannot go further left it begins evaluating the stack.

####Big O efficiency:
- Search: Depth First Search: O(|E| + |V|)
- E is number of edges
- V is number of vertices

####**summary**
- An algorithm that searches a tree by searching the depth first starting at the root. It always to traverse the leftmost branch first, so the it starts by traversing the leftmost until the end, then it backtracks and tries the right child. It is optimized for a tree that is deeper than wide, search Big O of O of Edges + parents that have 2 children.
- It can use a stack to keep track of the nodes it traverses. When it reaches the end of the leftmost side, it evaluates the stack to determine which nodes it should try to explore.


####Breadth First Search Vs. Depth First Search
- The simple answer to this question is that it depends on the size and shape of the tree.
  - For wide, shallow trees use Breadth First Search
  - For deep, narrow trees use Depth First Search

####Nuances:
  - Because BFS uses queues to store information about the nodes and its children, it could use more memory than is available on your computer.  (But you probably won't have to worry about this.)
  - If using a DFS on a tree that is very deep you might go unnecessarily deep in the search. See [xkcd](http://xkcd.com/761/) for more information.
  - Breadth First Search tends to be a looping algorithm.
  - Depth First Search tends to be a recursive algorithm.


## Efficient Sorting Basics
###**Merge Sort** https://en.wikipedia.org/wiki/Merge_sort
####Definition:
- A comparison based sorting algorithm
  - Divides entire dataset into groups of at most two.
  - Compares each number one at a time, moving the smallest number to left of the pair.
  - (After you compare 2 groups together by starting with the leftmost value and sort them, in the end you have a group of 4. This continues until there is only one set).
  - ----
  - Once all pairs sorted it then compares left most elements of the two leftmost pairs creating a sorted group of four with the smallest numbers on the left and the largest ones on the right.
  - This process is repeated until there is only one set.

####What you need to know:
- This is one of the most basic sorting algorithms.
- Know that it divides all the data into as small possible sets then compares them.

####Big O efficiency:
- Best Case Sort: Merge Sort: O(n)
- Average Case Sort: Merge Sort: O(n log n)
- Worst Case Sort: Merge Sort: O(n log n)

####**summary**
- It is a comparison based soring algorithm, where is starts by continuously halving the dataset until the smallest unit of 1 element, then it orders the elements by pairing groups as it merges back into one complete set. Average Time complexity is O of n log n. (bad, have to divide the array set close to linear increase)

###**Quicksort** https://www.geeksforgeeks.org/quick-sort/
####Definition:
- A comparison based sorting algorithm
  - Where you choose a pivot element (could be a chosen element like the most right) and putting all elements smaller than the pivot on the left side of the array.
  - It repeats this process, until it reaches the pivot element, then places the pivot in the correct place where all the elements to the left are lesser and elements to the right are greater; ;;at which point the left side is sorted.
  - When the left side is finished sorting it performs the same operation on the right side.
- Computer architecture favors the quicksort process. Uses swaps, since shifting is costly.

####What you need to know:
- While it has the same Big O as (or worse in some cases) many other sorting algorithms it is often faster in practice than many other sorting algorithms, such as merge sort.
- Know that it halves the data set by the average continuously until all the information is sorted.

####Big O efficiency:
- Best Case Sort: Merge Sort: O(n)
- Average Case Sort: Merge Sort: O(n log n)
- Worst Case Sort: Merge Sort: O(n^2)

####**summary**
- It is a comparison based sorting algorithm where a pivot element is chosen, could be the most right element, and a wall index is tracked to divide the values less and greater than the pivot. Each time an element is less than the pivot it swaps it to put it behind the wall and when it reaches the pivot the pivot is swapped to the wall index. Average time complexity is O of n log n

###**Bubble Sort**
####Definition:
- A comparison based sorting algorithm
  - It iterates left to right comparing every couplet, moving the smaller element to the left.
  - It repeats this process until it no longer moves and element to the left.

####What you need to know:
- While it is very simple to implement, it is the least efficient of these three sorting methods.
- Know that it moves one space to the right comparing two elements at a time and moving the smaller on to left.

####Big O efficiency:
- Best Case Sort: Merge Sort: O(n)
- Average Case Sort: Merge Sort: O(n^2)
- Worst Case Sort: Merge Sort: O(n^2)

####Merge Sort Vs. Quicksort
- Quicksort is likely faster in practice.
- Merge Sort divides the set into the smallest possible groups immediately then reconstructs the incrementally as it sorts the groupings.
- Quicksort continually divides the set by the average, until the set is recursively sorted.

###**Insertion Sort**
####Definition:
-  It is a comparison based sorting algorithm where the pivot is chosen starting from the left and compares the elements on the left of the pivot. If the pivot is less than an element, it is inserted to the left of it. An analogy is systematically sorting a hand of cards.

####Big O efficiency:
- O(n*n)

## Basic Types of Algorithms
###**Recursive Algorithms**
####Definition:
- An algorithm that calls itself in its definition.
  - **Recursive case** a conditional statement that is used to trigger the recursion.
  - **Base case** a conditional statement that is used to break the recursion.

####What you need to know:
- **Stack level too deep** and **stack overflow**.
  - If you've seen either of these from a recursive algorithm, you messed up.
  - It means that your base case was never triggered because it was faulty or the problem was so massive you ran out of RAM before reaching it.
  - Knowing whether or not you will reach a base case is integral to correctly using recursion.
  - Often used in Depth First Search


###**Iterative Algorithms**
####Definition:
- An algorithm that is called repeatedly but for a finite number of times, each time being a single iteration.
  - Often used to move incrementally through a data set.

####What you need to know:
- Generally you will see iteration as loops, for, while, and until statements.
- Think of iteration as moving one at a time through a set.
- Often used to move through an array.

####Recursion Vs. Iteration
- The differences between recursion and iteration can be confusing to distinguish since both can be used to implement the other. But know that,
  - Recursion is, usually, more expressive and easier to implement.
  - Iteration uses less memory.
- **Functional languages** tend to use recursion. (i.e. Haskell)
- **Imperative languages** tend to use iteration. (i.e. Ruby)
- Check out this [Stack Overflow post](http://stackoverflow.com/questions/19794739/what-is-the-difference-between-iteration-and-recursion) for more info.

####Pseudo Code of Moving Through an Array (this is why iteration is used for this)
```
Recursion                         | Iteration
----------------------------------|----------------------------------
recursive method (array, n)       | iterative method (array)
  if array[n] is not nil          |   for n from 0 to size of array
    print array[n]                |     print(array[n])
    recursive method(array, n+1)  |
  else                            |
    exit loop                     |
```
###**Greedy Algorithm**
####Definition:
- An algorithm that, while executing, selects only the information that meets a certain criteria.
- The general five components, taken from [Wikipedia](http://en.wikipedia.org/wiki/Greedy_algorithm#Specifics):
  - A candidate set, from which a solution is created.
  - A selection function, which chooses the best candidate to be added to the solution.
  - A feasibility function, that is used to determine if a candidate can be used to contribute to a solution.
  - An objective function, which assigns a value to a solution, or a partial solution.
  - A solution function, which will indicate when we have discovered a complete solution.

####What you need to know:
- Used to find the optimal solution for a given problem.
- Generally used on sets of data where only a small proportion of the information evaluated meets the desired result.
- Often a greedy algorithm can help reduce the Big O of an algorithm.

####Pseudo Code of a Greedy Algorithm to Find Largest Difference of any Two Numbers in an Array.
```
greedy algorithm (array)
  var largest difference = 0
  var new difference = find next difference (array[n], array[n+1])
  largest difference = new difference if new difference is > largest difference
  repeat above two steps until all differences have been found
  return largest difference
```

This algorithm never needed to compare all the differences to one another, saving it an entire iteration.

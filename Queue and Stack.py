# CS331 Assignment 5, 10/27/2022

# In this assignment, you're asked to implement methods in several classes:
# 1. A Linked-Queue using a Singly LinkedList.
# 2. A Stack that's implemented using one or more Queues.
# 3. A Linked-Stack using a Singly LinkedList.
# You're also asked to implement a method valid_parentheses that uses Linked-Stack.

####################    DO NOT CHANGE THIS CLASS   ####################
class Node:
    # The Node class for a Singly LinkedList is implemented. Do not change anything in this class.

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self)


# This is the class StackUsingQueue.
# You need to use Queue methods to simulate each method in a Stack.
class StackUsingQueue:
    # This is the class Queue, it is implemented using a Singly LinkedList.
    class Queue:

        # Please implement each of the following methods in class Queue following the guide.
        # Here, I've only implemented the construction method and the dunder __repr__ method. Do not change them.

        def __init__(self):
            # A new Queue contains two pointers head and tail both pointing to None.
            # Note that, the head is NOT a sentinel head.
            ####################    DO NOT CHANGE THIS   ####################
            self.head = self.tail = None

        def empty(self):
            # Return whether the Queue is empty or not.
            if self.head is None and self.tail is None:
                return False
            else:
                return True

        def enqueue(self, item):
            # Enqueue item to the tail of the Queue.
            # Note that, while enqueuing item to an empty Queue, both head and tail pointers need to be updated.
            # Do not return anything in the method.
            if self.head is None and self.tail is None:
                a = Node(item)
                self.head = a
                self.tail = a
                self.head.next = self.tail
            else:
                a = Node(item)
                self.tail.next = a
                self.tail = a
                self.tail.next = None

        def dequeue(self):
            # assert not self.empty()
            # Dequeue the item at the head of the Queue.
            # Note that, after dequeuing the last item, both head and tail pointers need to be updated.
            # Return the dequeued item.
            if self.__sizeof__() == 1:
                self.head = None
                self.tail = None

            else:
                self.head = self.head.next
                if self.head is None:
                    self.tail = None

        def __iter__(self):
            # This implements "for item in Queue"
            # Yield each node from head to tail.
            # (We don't need to yield node.val since when implemented __repr__(Node) already.)
            n = self.head
            while n:
                yield n.val
                n = n.next

        def __repr__(self):
            # This method implements "print(Queue)"
            ####################    DO NOT CHANGE THIS  ####################
            return "[" + ",".join(repr(n) for n in self) + "]"

    # Please implement each of the following methods in class StackUsingQueue following the guide.
    # Remind that, you may use ONLY Queue methods to implement each Stack method in this class.
    # Here, our design is that the "head" of self.data (which is a Queue) is the "top" of self (which is a Stack).
    # I've only implemented the construction method, peek(), and the dunder __repr__ method. Do not change them.

    def __init__(self):
        # A new StackUsingQueue contains a Queue as its data.
        ####################    DO NOT CHANGE THIS  ####################

        self.data = StackUsingQueue.Queue()

    def empty(self):
        # Return whether self.data is empty or not.
        # Note that, use methods in the Queue class only.
        if self.data is None:
            return False
        else:
            return True
        pass

    def peek(self):
        # This implementation shows that we consider the "head" of self.data (which is a Queue)
        # as the "top" of self (which is a Stack).

        ####################    DO NOT CHANGE THIS  ####################
        assert not self.empty()
        return self.data.head

    def push(self, item):
        # Push item to the "head" of self.data.
        # Remind that, you may only use methods in the Queue class to implement this method.
        # Note that, we cannot insert item directly to the head of a queue.
        # Do not return anything in this method.
        if self.data.__sizeof__() == 0:
            self.data.head = item
        else:
            self.data.enqueue(item)

    def pop(self):
        # assert not self.empty()
        # Pop out the "top" of self (aka, the "head" of self.data).
        # Remind that, you may only use methods in Queue class to implement this method.
        # Note that, we can dequeue item directly from the head of a queue.
        # Return the popped out item.
        item = self.data.head
        self.data.dequeue()
        return item

    def __iter__(self):
        # This implements "for item in StackUsingQueue"
        # You can yield each node from "top" to "bottom" of self (aka, head to tail of self.data).
        # Or you can simply use the iterator of self.data that you implemented for the Queue class.
        # (We don't need to yield node.val since when implemented __repr__(Node) already.)
        n = self.data.head
        while n:
            yield n.val
            n = n.next
        pass

    def __repr__(self):
        # This method implements "print(StackUsingQueue)"

        ####################    DO NOT CHANGE THIS  ####################
        return "[" + ",".join(repr(n) for n in self) + "]"


# This is the class Stack, it is implemented using a Singly LinkedList.
# We have implemented this class together in Lecture 12.
class Stack:
    # Please implement each of the following methods in class Stack following the guide.
    # Here, I've only implemented the construction method and the dunder __repr__ method. Do not change them.

    def __init__(self):
        # A new Stack contains a pointer called "top" points to None.
        ####################    DO NOT CHANGE THIS  ####################
        self.top = None

    def empty(self):
        # Return whether Stack is empty or not
        if self.top is None:
            return True
        else:
            return False

    def push(self, item):
        # Push item to the top of the Stack.
        self.top = Node(item, next=self.top)

    def pop(self):
        assert not self.empty()
        # Pop out the top item from Stack.
        # Return the popped out item.
        temp = self.top.val
        self.top = self.top.next
        return temp

    def peek(self):
        assert not self.empty()
        # Return the item on the top of the Stack.
        return self.top

    def __iter__(self):
        # This implements "for item in Stack"
        # Yield each node from "top" to "bottom" of the Stack.
        # (We don't need to yield node.val since when implemented __repr__(Node) already.)
        n = self.top
        while n:
            yield n
            n = n.next

    def __repr__(self):
        # This implements "print Stack"
        ####################    DO NOT CHANGE THIS  ####################
        return "[" + ",".join(repr(n) for n in self) + "]"


# This is Question 20. Valid Parentheses on LeetCode.com that we did in a lab.
# The input of this method is a string that contains "{}", "[]" and "()".
# Return whether the parentheses in the input string is valid or not.
# Note that, use the Stack class instead of StackUsingQueue class for better running time.
def valid_parentheses(expr: str):
    if len(expr) % 2 != 0:
        return False
    par = {'(': ')', '[': ']', '{': '}'}
    stack = Stack()
    for i in expr:
        if i in par.keys():
            stack.push(i)
        else:
            if stack.empty():
                return False
            a = stack.pop()
            if i != par[a]:
                return False
    return stack.empty()


########################################################################################################################
######################################                                      ############################################
######################################     DO NOT CHANGE ANYTHING BELOW     ############################################
######################################                                      ############################################
########################################################################################################################
print("First, let's test whether the Linked Queue is correctly implemented.")
q1 = StackUsingQueue.Queue()
for x in range(6):
    q1.enqueue(x)
print("Let q1 be an empty Linked Queue. After enqueuing numbers 0 ~ 5 to q1, q1 =", q1, ".")

for _ in range(2):
    q1.dequeue()
print("After calling dequeue twice, then q1 =", q1, ".")

print("Then, let's test both Stack classes.")
s1 = StackUsingQueue()
for x in range(6):
    s1.push(x)
print("Let s1 be an empty Stack implemented with a Queue. After pushing numbers 0 ~ 5 to s1, s1 =", s1, ".")
s2 = Stack()
for x in range(6):
    s2.push(x)
print("Let s2 be an empty Linked Stack. After pushing numbers 0 ~ 5 to s2, s2 =", s2, ".")

for _ in range(2):
    s1.pop()
    s2.pop()
print("Pop out two elements from each Stack, then s1 =", s1, "; and s2 =", s2, ".")

print("In the end, let's test method \"valid_parentheses()\".")
str1 = "{[()](())(){}}{}[]"
print("Let string str1 = " + str1 + ", which is a series of valid parentheses. "
                                    "Our method returns", valid_parentheses(str1), ".")
str2 = "([])}"
print("Let string str1 = " + str2 + ", which is a series of invalid parentheses. "
                                    "Our method returns", valid_parentheses(str2), ".")

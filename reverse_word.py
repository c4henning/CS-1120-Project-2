class Stack:
    """
    Creates a basic stack object

    This class provides a simple implementation of a stack data structure
    using a Python list. The stack supports push and pop operations.
    """
    def __init__(self, size: int):
        """
        Initialize an empty list to hold elements.

        The stack is initialized with a maximum size and sets all placeholder elements to None.

        :parameter size: Maximum size of the stack
        :type size: int
        """
        self.__stack = [None] * size
        self.top = -1

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.

        This method compares against the maximum stack index.
        If the maximum stack index is at least 0 there are elements in the stack.

        :returns: True if stack is empty, False otherwise.
        :rtype: bool
        """
        return self.top < 0

    def is_full(self) -> bool:
        """
        Check if the stack is empty.

        This method compares against the maximum stack index.
        If the maximum stack index is at least 0 there are elements in the stack.

        :returns: True if stack is empty, False otherwise.
        :rtype: bool
        """
        return self.top >= len(self.__stack) - 1

    def push(self, item: any) -> None:
        """
        Adds an item to the top of the stack and increments pointer.

        :parameter item: The item to be pushed onto the stack.
        :returns: None
        """
        if self.is_full():
            print("Cannot insert stack is full")
        else:
            self.top += 1
            self.__stack[self.top] = item

    def pop(self) -> any:
        """
        Removes and returns an item at the top of the stack. Decrements the pointer.

        :returns: The item removed from the top of the stack. If the stack is empty, will return None.
        :rtype: any
        """
        if self.is_empty():
            return None
        else:
            item = self.__stack[self.top]
            self.top -= 1
            return item


if __name__ == "__main__":
    # A program to reverse the letters of a word
    stack = Stack(100)                                  # Create a stack to hold letters
    word = input("Word to reverse: ")
    for letter in word:                                 # Loop over letters in word
        stack.push(letter)                              # and push to stack

    reverse = ''                                        # Build the reversed version
    while not stack.is_empty():                         # by popping the stack until empty
        reverse += stack.pop()

    print('The reverse of', word, 'is', reverse)

class Stack:
    """
    Creates a basic stack object

    This class provides a simple implementation of a stack data structure
    using a Python list. The stack supports push and pop operations.
    """
    def __init__(self):
        """
        Initialize an empty list to hold elements.
        """
        self.__stack = []

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.

        :returns: True if stack is empty, False otherwise.
        :rtype: bool
        """
        return len(self.__stack) == 0

    def push(self, item: any) -> None:
        """
        Adds an item to the top of the stack

        :parameter item: The item to be pushed onto the stack.
        :returns: None
        """
        self.__stack.append(item)

    def pop(self) -> any:
        """
        Removes and returns an item at the top of the stack

        :returns: The item removed from the top of the stack. If the stack is empty, will return None.
        :rtype: any
        """
        if self.is_empty():
            return None
        else:
            item = self.__stack.pop()
            return item


if __name__ == "__main__":
    # A program to reverse the letters of a word
    stack = Stack()                                     # Create a stack to hold letters
    word = input("Word to reverse: ")
    for letter in word:                                 # Loop over letters in word
        stack.push(letter)                              # and push to stack

    reverse = ''                                        # Build the reversed version
    while not stack.is_empty():                         # by popping the stack until empty
        reverse += stack.pop()

    print('The reverse of', word, 'is', reverse)

#!/usr/bin/python3
class MyList(list):
    """
    MyList class that inherits from the built-in list class.

    This class adds a public instance method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))

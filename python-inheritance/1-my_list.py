#!/usr/bin/python3
class MyList(list):
    """
    MyList is a subclass of the built-in list.
    It provides an additional method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Print the list in ascending sorted order.
        The original list is not modified.
        """
        print(sorted(self))

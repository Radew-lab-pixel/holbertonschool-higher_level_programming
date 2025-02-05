#!/usr/bin/python3
"""class VerboseList inherits from list"""
from sympy.codegen.ast import continue_


class VerboseList(list):
    """VerboseList class inherit from list"""
    # def __init__(self, iterable):
    #    super().__init__((item) for item in iterable)

    def append(self, item):
        """child method named append"""
        super().append(item)
        # print(f"Added [{item}] to the list.")
        print(f"Added [{item}] to the list.")

    def extend(self, other):
        """child method named extend"""
        if isinstance(other, type(self)):
            super().extend(other)
        else:
            super().extend(item for item in other)
        print(f"Extended the list with [{len(other)}] items.")

    def remove(self, item):
        """child method named remove"""
        print(f"Removed [{item}] from the list.")
        try:
            super().remove(item)
        except ValueError:
            print("", end="")


    # def pop(self):
    #    print(f"Popped [item] from the list.")
    #    super().pop()

    # def pop(self, item):
        # """child method named pop"""
        # print(f"Popped [item] from the list.")
        # super().pop(item)

    def pop(self, index=-1):
        """child method named pop"""
        result = super().pop(index)
        print(f"Popped {result} from the list.")
        return result
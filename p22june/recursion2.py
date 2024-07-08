import sys
print(sys.getrecursionlimit())  # This will print the current recursion limit, which is 1000 by default.

sys.setrecursionlimit(3000)  # This sets the recursion limit to 3000.
print(sys.getrecursionlimit())  # This will print the new recursion limit, which should be 3000.

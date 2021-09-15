def bowling_pins(arr):
    s = [' ' if i in arr else 'I' for i in range(1, 11)]
    return "{6} {7} {8} {9}\n {3} {4} {5} \n  {1} {2}  \n   {0}   ".format(*s)
# python3
# Kristaps Arnolds Kaidalovs 16.grupa 201RDK001

import sys
import threading

def compute_height(count, nodes):
    visited_nodes = [0] * count
    max_height = 0
    cur_height = 0
    next_node = 0

    for i, node in enumerate(nodes):
        next_node = node
        cur_height = 1

        while next_node != -1:
            next_node = nodes[next_node]
            cur_height = cur_height + 1

            if (visited_nodes[next_node] != 0):
                cur_height = cur_height + visited_nodes[next_node]
                break
                
        visited_nodes[i] = cur_height
        if cur_height > max_height:
            max_height = cur_height

    return max_height

def main():
    # implement input form keyboard and from files
    count = 0
    nodes = 0

    # account for github input inprecision
    input_type = input().strip()
    if (input_type.upper() == "F"):
        # let user input file name to use, append "test/" to account for github inaccuracy
        file = open("test/" + input())
        count = int(file.readline())
        nodes = list(map(lambda i: int(i), file.readline().split()))
    elif (input_type.upper() == "I"):
        # input number of elements
        count = int(input())
        # input values in one variable, separate with space, split these values in an array
        nodes = list(map(lambda i: int(i), input().split()))
    else:
        print("Invalid input type: ", input_type)
        return

    if (count != len(nodes)):
        print("Invalid input length: ", count)
        return

    # call the function and output it's result
    print(compute_height(count, nodes))
    
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

# ************************** Question 1 *************************************

# The BFS function takes a single argument TREE that represents a tree, and returns a tuple of leaf nodes in the order they are visited by left-to-right breadth-first search.
def BFS(TREE):
    # Solution: It uses a list (`tree_list`) as a queue to keep track of nodes to visit. At each step, it removes the front element from the queue:
    # If the element is a string (a leaf node), it adds it to the result list.
    # If the element is a tuple (a subtree), it appends its children to the end of the queue.This process continues until all nodes have been visited, resulting in a left-to-right BFS traversal. 

    # tree_list acts like a queue
    tree_list = [TREE]
    BFS_result = []

    while tree_list != []:
        curr = tree_list.pop(0) 
        # we have a leaf node, so we can append to our final result
        if type(curr) is str:
            BFS_result.append(curr)
        # add items in tuple to the end of queue
        elif type(curr) is tuple:
            for item in curr:
                tree_list.append(item)
         
    # result is a list but we want a tuple      
    return tuple(BFS_result)

# ************************** Question 2 *************************************

# DFS takes a single argument TREE that represents a tree, and returns a tuple of leaf nodes in the order they are visited by left-to-right depth-first search.
def DFS(TREE):
    # Solution: Traverse each subtree from left to right. If a string (leaf node) is encountered, add it to the dfs_result tuple. If the element is a subtree (a tuple), recursively dive deeper into it.
    if type(TREE) is str:
        # return a tuple 
       return (TREE, )
    else:
        DFS_result = ()
        for subtree in TREE:
            DFS_result += DFS(subtree)
         
    return DFS_result

# ************************** Question 3 *************************************

# DLS_RIGHT_TO_LEFT Searches the tree from right-to-left, only up to a certain depth. Takes two arguments, a tuple TREE representing a tree and an integer DEPTH representing the depth of TREE, and returns a tuple of leaf nodes in the order they are visited by a right-to-left depth limited search.
def DLS_RIGHT_TO_LEFT(TREE, DEPTH):
    # Solution: This function does a depth-limited search on a tree, going from right to left. It's similar to my DFS function, but it only returns leaf nodes (strings) that are exactly at the given depth. If the current node is a string and depth >= 0, we return it. If it's a tuple, we go deeper into each subtree (starting from the right), reducing the depth each time. We stop searching once the depth goes below 0.
    
    # when we go into a negative depth, we want to stop
    if DEPTH < 0:
        return ()
    # encountered a leaf node
    elif type(TREE) is str:
            return (TREE, )
    else:
        DLS_result = ()
        # reverse the tree to get that desired right-to-left iteration
        for subtree in reversed(TREE):
            DLS_result += DLS_RIGHT_TO_LEFT(subtree, DEPTH - 1)
    
    return DLS_result

# top-level function, called DFID, takes two arguments, a tuple TREE representing a tree and an integer D representing the depth of TREE, and returns a tuple of leaf nodes in the order they are visited by a right-to-left depth-first iterative-deepening search.
def DFID(TREE, D):
    # Solution: This function runs depth-limited search multiple times, from depth 0 up to depth D. Each time, it calls DLS_RIGHT_TO_LEFT to collect the leaf nodes at that depth. It adds together all the results from each depth level. This allows for the tree to be explored step by step, getting deeper each time.
    DFID_result = ()
    # only perform DLS_RIGHT_TO_LEFT D (depth) times
    for current_depth in range(D + 1):
        DFID_result += DLS_RIGHT_TO_LEFT(TREE, current_depth)
    return DFID_result

# **************************** Question 4 *************************************

# These functions implement a depth-first solver for the homer-baby-dog-poison
# problem. In this implementation, a state is represented by a single tuple
# (homer, baby, dog, poison), where each variable is True if the respective entity is
# on the west side of the river, and False if it is on the east side.
# Thus, the initial state for this problem is (False False False False) (everybody
# is on the east side) and the goal state is (True True True True).

# The main entry point for this solver is the function DFS_SOL, which is called
# with (a) the state to search from and (b) the path to this state. It returns
# the complete path from the initial state to the goal state: this path is a
# list of intermediate problem states. The first element of the path is the
# initial state and the last element is the goal state. Each intermediate state
# is the state that results from applying the appropriate operator to the
# preceding state. If there is no solution, DFS_SOL returns [].
# To call DFS_SOL to solve the original problem, one would call
# DFS_SOL((False, False, False, False), [])
# However, it should be possible to call DFS_SOL with any intermediate state (S)
# and the path from the initial state to S (PATH).

# First, we define the helper functions of DFS_SOL.

# FINAL_STATE takes a single argument S, the current state, and returns True if it is the goal state (True, True, True, True) and False otherwise.
def FINAL_STATE(S):
    # Solution: We simply return true if the current state is the goal state which is (True, True, True, True)
    if S == (True, True, True, True):
        return True
    else:
        return False

# NEXT_STATE returns the state that results from applying an operator to the
# current state. It takes two arguments: the current state (S), and which entity
# to move (A, equal to "h" for homer only, "b" for homer with baby, "d" for homer with dog, and "p" for homer with poison).
# It returns a list containing the state that results from that move.
# If applying this operator results in an invalid state (because the dog and baby, or poison and baby are left unsupervised on one side of the river), or when the action is impossible (homer is not on the same side as the entity) it returns [].
# NOTE that NEXT_STATE returns a list containing the successor state (which is
# itself a tuple)
# the return should look something like [(False, False, True, True)].
def NEXT_STATE(S, A):
    # Solution: We unwrap the state and check what action we are given to perform. We update our state based on this action and verify we have no illegal moves or that are updated state is not illegal.
    
    # unwrap the state
    homer, baby, dog, poison = S
    
    # we have an invalid move
    if A != "h" and A != "b" and A != "d" and A != "p":
        return []
    else:
        # "h" for homer only moves
        if A == "h":
            updated_state = (not(homer), baby, dog, poison)
        # "b" for homer with baby moves
        if A == "b":
            updated_state = (not(homer), not(baby), dog, poison)
        # "d" for homer with dog moves
        if A == "d":
            updated_state = (not(homer), baby, not(dog), poison)
        # "p" for homer with poison moves
        if A == "p":
            updated_state = (not(homer), baby, dog, not(poison))
    
    updated_homer, updated_baby, updated_dog, updated_poison = updated_state
    # baby and poison can't be left together (unless homer is with them)
    if (updated_poison == updated_baby):
        if (updated_poison != updated_homer):
            return []
    # dog and baby can't be left together (unless homer is with them)
    if (updated_dog == updated_baby):
        if (updated_dog != updated_homer):
            return []
    return [updated_state]

# SUCC_FN returns all of the possible legal successor states to the current
# state. It takes a single argument (S), which encodes the current state, and
# returns a list of each state that can be reached by applying legal operators
# to the current state.
def SUCC_FN(S):
   # Solution: We perform every legal action ("h", "b", "d", "p") on our given state using our NEXT_STATE funcion, if the updated_state is legal we add it to a list of sucessor_states. At the end we return this list of successor_states.
    succesor_states = []
    for legal_action in ["h", "b", "d", "p"]:
        updated_state = NEXT_STATE(S, legal_action)
        # verify action returns a valid updated_state
        if updated_state != []:
            # remember NEXT_STATE returns a list inside a tuple
            new_updated_state = updated_state[0]
            succesor_states.append(new_updated_state)
            
    return succesor_states

# ON_PATH checks whether the current state is on the stack of states visited by
# this depth-first search. It takes two arguments: the current state (S) and the
# stack of states visited by DFS (STATES). It returns True if S is a member of
# STATES and False otherwise.
def ON_PATH(S, STATES):
    # Solution: We iterate through STATES and check if the current state matches any of the states in STATES
    for state in STATES:
        if S == state:
            return True
    return False

# MULT_DFS is a helper function for DFS_SOL. It takes two arguments: a list of
# states from the initial state to the current state (PATH), and the legal
# successor states to the last, current state in the PATH (STATES). PATH is a
# first-in first-out list of states
# that is, the first element is the initial
# state for the current search and the last element is the most recent state
# explored. MULT_DFS does a depth-first search on each element of STATES in
# turn. If any of those searches reaches the final state, MULT_DFS returns the
# complete path from the initial state to the goal state. Otherwise, it returns
# [].
def MULT_DFS(STATES, PATH):
    # Solution: Try each of the next possible states using our other function DFS_SOL. If any of these possible paths we take lead to a goal we return this complete path. 
    for state in STATES:
        possible_path = DFS_SOL(state,PATH)
        # a path to the goal has been found (Returns the first path we found that reaches the goal)
        if possible_path != []:
            return possible_path
    return []

# DFS_SOL does a depth first search from a given state to the goal state. It
# takes two arguments: a state (S) and the path from the initial state to S
# (PATH). If S is the initial state in our search, PATH is set to []. DFS_SOL
# performs a depth-first search starting at the given state. It returns the path
# from the initial state to the goal state, if any, or [] otherwise. DFS_SOL is
# responsible for checking if S is already the goal state, as well as for
# ensuring that the depth-first search does not revisit a node already on the
# search path (i.e., S is not on PATH).
def DFS_SOL(S, PATH):
    # Solution: We use a stack to keep track of the S (state) and Path we are using. We check if the current state is the goal, if it is, we have found a path to the goal. We also prevent visiting states already on the path. If we are not at the goal, we find the next succesor_states and keep exploring these paths using the MULT_DFS function.
    
    # store current state and path to that state in the stack
    stack = [(S, PATH)]
    while stack != []:
        current_state, current_path = stack.pop()
        # Check if we are at goal already 
        if FINAL_STATE(current_state) == True:
            return current_path + [current_state]
        
        # check if we have already visited this state before
        if ON_PATH(current_state, current_path) == True:
            continue
        
        # update the path with the current state
        new_path = PATH + [current_state]
        # get the successor states from the given state
        successor_states = SUCC_FN(S)
        # now we want to explore all successors 
        return MULT_DFS(successor_states, new_path)
    
    return []
        
        
        
    
    
    
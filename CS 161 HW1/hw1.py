# The PAD function takes a single numeric argument N, returns the Nth Padovan number
def PAD(N):
    # Solution: There is a base case that returns 1 when N equals 0, 1, or 2. For any N>=3, The Nth padovan number is calculated using the sum of the two non-adjacent previous numbers.
    if (N == 0 or N == 1 or N == 2):
        return 1
    else:
        return PAD(N - 2) + PAD(N - 3)
        
        
# The SUMS function takes a single numeric argument N and returns the number of additions required by the PAD function to compute the Nth Padovan number
def SUMS(N):
    # Solution: The base case returns 0 as no additions are required when N equals 0, 1, or 2. For any N>=3, the function makes the same recursive call as the PAD function but adds 1 to account for the addition. 
    if (N == 0 or N == 1 or N == 2):
        return 0
    else:
        return SUMS(N - 2) + SUMS(N - 3) + 1
    

# The function ANON takes a single argument TREE that represents a tree. It returns an anonymized tree with the same structure, but where every leaf in the tree is replaced by a question mark
def ANON(TREE):
    # Solution: The function first checks if TREE is a leaf node. If it is, it replaces it with a '?'. Otherwise, it recursively processes each subtree, keeping the structure the same but replacing all leaves with '?'.
    if type(TREE) is not tuple:
        return "?"
    else:
        anonymized_tree = []
        for subtree in TREE:
            anonymized_tree.append(ANON(subtree))
        return tuple(anonymized_tree)
    


# The function TREE_HEIGHT takes a tree TREE in tuples, and returns the height of TREE.
def TREE_HEIGHT(TREE):
    # Solution: The base case returns 0 if it encounters a leaf node.  If the tree has subtrees, it calculates the height of each subtree, adds 1 for the current level, and returns the maximum height from all the subtree heights.
    if type(TREE) is not tuple:
        return 0
    else:
        subtree_heights = []
        for subtree in TREE:
            subtree_heights.append(TREE_HEIGHT(subtree) + 1)
        return max(subtree_heights)
    

# The TREE_ORDER function takes one argument TREE that represents an ordered tree, and returns a tuple that represents the postorder traversal of the numbers in TREE.
def TREE_ORDER(TREE):
    # Solution: If the tree is a single number (leaf), return it in a tuple. If the tree is not a leaf, split it into the left subtree (L), root (m), and right subtree (R). Then, recursively get the postorder traversal for the left and right subtrees, and combine them with the root at the end. Note: `extend` is used to merge the results from the left and right subtrees into a single list before adding the root.
    if type(TREE) is not tuple:
        return (TREE,)
    else:
        postorder_traversal = []
        (L, m, R) = TREE
        postorder_traversal.extend(TREE_ORDER(L))
        postorder_traversal.extend(TREE_ORDER(R))
        postorder_traversal.append(m)
        return tuple(postorder_traversal)
    
    
    
    

    
    
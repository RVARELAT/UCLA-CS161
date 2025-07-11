##############
# Homework 4 #
##############

# Exercise: Fill this function.
# Returns the index of the variable that corresponds to the fact that
# "Node n gets color c" when there are k possible colors
def node2var(n, c, k):
    # Solution: The following conversion convention was provided in the spec. Returns a unique variable index for the assignment: node n is color c.
    variable_index =  (n - 1) * k + c
    return variable_index

# Exercise: Fill this function
# Returns *a clause* for the constraint:
# "Node n gets at least one color from the set {1, 2, ..., k}"
def at_least_one_color(n, k):
    # Solution:  This function makes a rule that says a node must have at least one color. It creates a list of variable numbers, one for each color the node could be. The list is returned as a single clause.
    variable_index_list = []
    for color in range(1, k + 1):
        variable_index_list.append(node2var(n, color, k))
    return variable_index_list

# Exercise: Fill this function
# Returns *a list of clauses* for the constraint:
# "Node n gets at most one color from the set {1, 2, ..., k}"
def at_most_one_color(n, k):
    # Solution: We makes rules to stop a node from having more than one color. For every two different colors, it adds a rule that says the node can't have both. We return this list of rules
    clauses_list = []
    # Check every color with all the colors on its right side of the list
    for color_1 in range (1, k + 1):
        for color_2 in range(color_1 + 1, k + 1):
            variable_index_1 = node2var(n, color_1, k)
            variable_index_2 = node2var(n, color_2, k)
            clauses_list.append([-variable_index_1, -variable_index_2])
    return clauses_list

# Exercise: Fill this function
# Returns *a list of clauses* for the constraint:
# "Node n gets exactly one color from the set {1, 2, ..., k}"
def generate_node_clauses(n, k):
    # Solution: This function makes all the rules needed for one node.
    # It combines the rule that the node must have at least one color
    # with the rules that stop it from having more than one color.
    
    # Combine the node clauses from the previous two functions
    combined_node_clause = [at_least_one_color(n, k)] + at_most_one_color(n, k)
    return combined_node_clause

# Exercise: Fill this function
# Returns *a list of clauses* for the constraint:
# "Nodes connected by an edge e cannot have the same color"
# The edge e is represented by a tuple
def generate_edge_clauses(e, k):
    # Solution: This function makes rules to stop two connected nodes from having the same color. For each color, it adds a rule that blocks both nodes from being that color together.
    
    # An (undirected) edge e is simply a tuple of two node indices m, n.
    m, n = e
    # generate rules for each of the nodes
    edge_clauses = []
    for color in range(1, k + 1):
        node_m_color_index = node2var(m, color, k)
        node_n_color_index = node2var(n, color, k)
        edge_clauses.append([-node_m_color_index, -node_n_color_index])
    return edge_clauses

# The function below converts a graph coloring problem to SAT
# Return CNF as a list of clauses
# DO NOT MODIFY
def graph_coloring_to_sat(graph_fl, sat_fl, k):
    clauses = []
    # Open the graph file
    with open(graph_fl) as graph_fp:
        # Read the first line: it tells how many nodes and edges the graph has.
        node_count, edge_count = tuple(map(int, graph_fp.readline().split()))
        # For each node, add the rules that make sure it gets exactly one color
        for n in range(1, node_count + 1):
            clauses += generate_node_clauses(n, k)
        # For each edge, add the rules to stop the two connected nodes from sharing the same color
        for _ in range(edge_count):
            e = tuple(map(int, graph_fp.readline().split()))
            clauses += generate_edge_clauses(e, k)
    # Count how many total variables (one per node-color combo), and how many rules you have in total.
    var_count = node_count * k
    clause_count = len(clauses)
    # Open the .cnf output file, and write the header line in SAT format:
    with open(sat_fl, 'w') as sat_fp:
        # For each clause (list of variable numbers), write it to the file with a 0 at the end. SAT solvers expect each clause like: 1 -4 5 0
        sat_fp.write("p cnf %d %d\n" % (var_count, clause_count))
        for clause in clauses:
            sat_fp.write(" ".join(map(str, clause)) + " 0\n")
    return clauses, var_count


# Example function call
if __name__ == "__main__":
   graph_coloring_to_sat("graph1.txt", "graph1_3.cnf", 3)
   graph_coloring_to_sat("graph1.txt", "graph1_4.cnf", 4)
   
   
   
   graph_coloring_to_sat("graph2.txt", "graph2_3.cnf", 3)
   graph_coloring_to_sat("graph2.txt", "graph2_4.cnf", 4)
   graph_coloring_to_sat("graph2.txt", "graph2_5.cnf", 5)
   graph_coloring_to_sat("graph2.txt", "graph2_6.cnf", 6)
   graph_coloring_to_sat("graph2.txt", "graph2_7.cnf", 7)
   graph_coloring_to_sat("graph2.txt", "graph2_8.cnf", 8)
   graph_coloring_to_sat("graph2.txt", "graph2_9.cnf", 9)
   graph_coloring_to_sat("graph2.txt", "graph2_10.cnf", 10)

from hw3 import sokoban, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, h0, h1, h2

test_cases = [
    ("s1", s1, [80, 7]),
    ("s2", s2, [110, 10]),
    ("s3", s3, [211, 12]),
    ("s4", s4, [300, 13]),
    ("s5", s5, [551, 10]),
    ("s6", s6, [722, 12]),
    ("s7", s7, [1738, 50]),
    ("s8", s8, [1763, 22]),
    ("s9", s9, [1806, 41]),
    ("s10", s10, [10082, 51]),
    ("s11", s11, [16517, 48]),
    ("s12", s12, [22035, 38]),
    ("s13", s13, [26905, 28]),
    ("s14", s14, [41715, 53]),
    ("s15", s15, [48695, 44]),
    ("s16", s16, [91344, 111]),
    # ("s17", s17, [3301278, 76]),
    ("s18", s18, [None, 25]),
    ("s19", s19, [None, 21]),
]

# print("=== TESTING HEURISTIC h0 ===\n")
# for name, state, expected in test_cases:
#     print(f"Running {name}, expected {expected}:")
#     sokoban(state, h0)
#     print("-" * 30)

# print("\n=== TESTING HEURISTIC h1 ===\n")
# for name, state, expected in test_cases:
#     print(f"Running {name}, expected {expected}:")
#     sokoban(state, h1)
#     print("-" * 30)

print("\n=== TESTING HEURISTIC h2 ===\n")
for name, state, expected in test_cases:
    print(f"Running {name}, expected {expected}:")
    sokoban(state, h2)
    print("-" * 30)
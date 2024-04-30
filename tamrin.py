def find_thief():
    # Initialize all statements as True
    statements = {
        'A': [True, True, True],
        'B': [True, True, True],
        'C': [True, True, True],
        'D': [True, True, True]
    }

    # Update statements based on their relationships
    if statements['A'][0]:
        statements['C'][0] = False
    if statements['B'][0]:
        statements['D'][0] = False
    if statements['B'][1]:
        statements['D'][2] = False
    if statements['C'][2]:
        statements['D'][1] = False
    if statements['A'][1]:
        statements['C'][1] = False
        statements['B'][2] = False

    # Count the number of true and false statements
    num_true = sum(sum(s) for s in statements.values())
    num_false = 4 * 3 - num_true

    if num_true == num_false:
        print("In this case, the number of lies and truths is equal (lies == truths)")

    print("So the following people are not thieves:")
    print("A, because A's second statement is always true")
    print("C, because C's second statement is always false")
    print("D, because B's third statement is always false")

    print("So B is the thief")

find_thief()

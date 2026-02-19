import itertools
# Crypto-Arithmetic Solver for SEND + MORE = MONEY
def solve_cryptarithm():
    letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')
    digits = range(10)

    for perm in itertools.permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))

        # Leading zeros not allowed
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue

        SEND = (1000 * mapping['S'] +
                100 * mapping['E'] +
                10 * mapping['N'] +
                mapping['D'])

        MORE = (1000 * mapping['M'] +
                100 * mapping['O'] +
                10 * mapping['R'] +
                mapping['E'])

        MONEY = (10000 * mapping['M'] +
                 1000 * mapping['O'] +
                 100 * mapping['N'] +
                 10 * mapping['E'] +
                 mapping['Y'])

        if SEND + MORE == MONEY:
            print("Solution Found!")
            print(f"SEND  = {SEND}")
            print(f"MORE  = {MORE}")
            print(f"MONEY = {MONEY}")
            print("\nLetter Mapping:", mapping)
            return
    print("No solution found.")
solve_cryptarithm()
 

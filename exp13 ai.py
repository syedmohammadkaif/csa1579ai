def solve_cryptarithmetic(puzzle):
"""
Solves the cryptarithmetic puzzle.
puzzle: a string containing the puzzle in the form of "WORD + WORD = RESULT"
Returns a dictionary mapping letters to digits, or None if no solution is found.
"""
words = puzzle.split()
letters = set(''.join(words))
if len(letters) > 10:
return None # More than 10 letters, no solution is possible
for perm in permutations(range(10), len(letters)):
mapping = dict(zip(letters, perm))
if all(mapping[word[0]] != 0 for word in words): # Check for leading zeros

SAVEETHA SCHOOL OF ENGINEERING

SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES

26

a = sum(mapping[c] * (10 ** (len(word) - i - 1)) for word in words for i, c in
enumerate(word[::-1]))
b = a // 10
a %= 10
c = sum(mapping[c] * (10 ** (len(words[2]) - i - 1)) for i, c in enumerate(words[2][::-
1]))
if a == mapping[words[2][-1]] and b + c == sum(mapping[c] * (10 ** (len(word) - i -
1)) for word in words[:-1]):
return mapping
return None
# Example usage
puzzle = "SEND + MORE = MONEY"
mapping = solve_cryptarithmetic(puzzle)
if mapping:
print(mapping)
print(puzzle.translate(str.maketrans(mapping)))
else:
print('No solution found.')

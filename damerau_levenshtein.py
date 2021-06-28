# Damerau-Levenshtein edit distane implementation
# Based on pseudocode from Wikipedia: https://en.wikipedia.org/wiki/Damerau-Levenshtein_distance

# Copyright © 2013 James Jensen
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Possible improvement by treating 1 addition + 1 deletion = 1 substitution
# between transposed characters:
#
# Damerau-Levenshtein distance for "abcdef" and "abcfad" = 3:
#   1. substitute "d" for "f"
#   2. substitute "e" for "a"
#   3. substitute "f" for "d"
#
# Or alternatively:
#   1. transpose "d" and "f"
#   2. delete "a"
#   3. insert "e"
#
# It's obvious that (2) and (3) in the second analysis are really just one
# substitution:
#   1. transpose "d" and "f"
#   2. substitute "e" for "a"
#
# With this variant, the distance between "abcdef" and "abcfad" is in fact 2.

def damerau_levenshtein_distance_improved(a, b):
    # "Infinity" -- greater than maximum possible edit distance
    # Used to prevent transpositions for first characters
    INF = len(a) + len(b)

    # Matrix: (M + 2) x (N + 2)
    matrix  = [[INF for n in xrange(len(b) + 2)]]
    matrix += [[INF] + range(len(b) + 1)]
    matrix += [[INF, m] + [0] * len(b) for m in xrange(1, len(a) + 1)]

    # Holds last row each element was encountered: DA in the Wikipedia pseudocode
    last_row = {}

    # Fill in costs
    for row in xrange(1, len(a) + 1):
        # Current character in a
        ch_a = a[row-1]

        # Column of last match on this row: DB in pseudocode
        last_match_col = 0

        for col in xrange(1, len(b) + 1):
            # Current character in b
            ch_b = b[col-1]

            # Last row with matching character
            last_matching_row = last_row.get(ch_b, 0)

            # Cost of substitution
            cost = 0 if ch_a == ch_b else 1

            # Compute substring distance
            matrix[row+1][col+1] = min(
                matrix[row][col] + cost, # Substitution
                matrix[row+1][col] + 1,  # Addition
                matrix[row][col+1] + 1,  # Deletion

                # Transposition
                # Start by reverting to cost before transposition
                matrix[last_matching_row][last_match_col]
                    # Cost of letters between transposed letters
                    # 1 addition + 1 deletion = 1 substitution
                    + max((row - last_matching_row - 1),
                          (col - last_match_col - 1))
                    # Cost of the transposition itself
                    + 1)

            # If there was a match, update last_match_col
            if cost == 0:
                last_match_col = col

        # Update last row for current character
        last_row[ch_a] = row

    # Return last element
    return matrix[-1][-1]
"""
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, 
you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply 
to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

T: O(n)
S: O(n)
    - n is the number of elements in operations
"""
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        def evaluate_op(operation):
            if operation == "+":
                self.stack_results.append(
                    self.stack_results[-1] + self.stack_results[-2])
            elif operation == "D":
                self.stack_results.append(self.stack_results[-1] * 2)
            elif operation == "C":
                self.stack_results.pop()
            else:
                self.stack_results.append(int(operation))

        self.stack_results = []

        for op in operations:
            evaluate_op(op)

        return sum(self.stack_results)


def test_calPoints():
    s = Solution()
    assert s.calPoints(["5", "2", "C", "D", "+"]) == 30
    assert s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27
    assert s.calPoints([]) == 0

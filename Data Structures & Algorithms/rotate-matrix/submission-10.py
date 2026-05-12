import copy

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        result = copy.deepcopy(matrix)
        e = len(matrix)
        for row_idx, row in enumerate(matrix):
            for col_idx, i in enumerate(row):
                result[col_idx][e - row_idx - 1] = i
        
        matrix[:] = result

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        B = [ [] for _ in range(len(A[0])) ]

        for row in A:
            for index, item in enumerate(row):
                B[index].append(item)
                
        return B

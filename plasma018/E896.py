class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        B = sorted(A)
        return B == A or B[::-1] == A
        

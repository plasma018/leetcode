class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        B = sorted(A)
        return B == A or B[::-1] == A
    
 
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        def isUper(A):
            dummy = A[0]
            for item in A:
                if dummy > item:
                    return False
                dummy = item
            return True
        
        def isLower(A):
            dummy = A[0]
            for item in A:
                if dummy < item:
                    return False
                dummy = item
            return True
        return isUper(A) or isLower(A)   
    
        

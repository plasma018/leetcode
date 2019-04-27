class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:

        if len(A) != len(B) or len(A) == 0:
            return False
        
        times = 0
        temp_a, temp_b = None, None
        
        for i in range(len(A)):
            if A[i] is not B[i]:
                times += 1
                if temp_a is None:
                    temp_a = A[i]
                    temp_b = B[i]
                elif temp_a != B[i] or temp_b != A[i]:
                    return False
                    
        
        if times == 0 and len(A) != len(set(A)):
            return True
        
        if times != 2:
            return False
        
        return True
         
            
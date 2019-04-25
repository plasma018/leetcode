class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        K = str(K)
        remain = 0
        
        if len(A) < len(K):
            size = len(K)-len(A)
            A = [0]*size + A
        
        for i in range(-1, -len(K)-1,-1):
            remain, A[i] = divmod(A[i]+int(K[i])+remain,10)
        
        for i in range(-len(K)-1, -len(A)-1, -1):
            if remain == 0:
                break
            remain, A[i] = divmod(A[i]+remain,10)
            
        if remain is 1:
            A.insert(0,1)
            
        return A

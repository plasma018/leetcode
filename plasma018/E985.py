class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
      B = [0]*len(A)
      ans = 0
      for i in A:
        if i % 2 == 0: ans += i
      
      i = 0
      for val, index in queries:
        
        if A[index] % 2 == 0: ans -= A[index]
          
        A[index] += val
        
        if A[index] % 2 == 0: ans += A[index]
        
        B[i] = ans
        i += 1
        
        
      return B

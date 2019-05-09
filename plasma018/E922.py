class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
      j = -1
      for i in range(0,len(A),2):
        if A[i] % 2 == 0:
          continue
        while j < len(A):
          j += 2
          if A[j] % 2 == 0:
            temp = A[j]
            A[j], A[i] =  A[i], temp
            break
      return A  
             
            

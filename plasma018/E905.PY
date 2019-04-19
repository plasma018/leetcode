class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
      A.sort(key=lambda x: x % 2 is 1)
      return A

    def sortArrayByParity(self, A: List[int]) -> List[int]:
      size = len(A)
      B = [None]*size
      start = 0
      end = size - 1 
      for val in A:
        if val % 2 == 0:
            B[start] = val
            start += 1
        else
            B[end] = val
            end -= 1
      return A
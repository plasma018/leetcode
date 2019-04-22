class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
      _sum = 0
      answer = [0]*len(A)
      for i in range(len(A)):
        _sum = (_sum << 1 | A[i])
        answer[i] = True if _sum  % 5 == 0 else False
      return answer

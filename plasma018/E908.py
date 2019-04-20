class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
      _max = A[0]
      _min = A[0]
      for i in A:
        if _max < i:
          _max = i
          continue
        if _min > i:
          _min = i
      d = _max - _min
      return max(0, d - K - K)

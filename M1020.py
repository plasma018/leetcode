class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
      row = len(A) - 1
      column = len(A[0]) - 1
      _sum = 0

      def help(A, i, j):
        if i >= 0 and i < len(A) and j >= 0 and j < len(A[i]) and A[i][j] == 1: 
          A[i][j] = 0
          help(A , i-1, j)
          help(A , i+1, j)
          help(A , i, j+1)
          help(A , i, j-1)

      for i in range(len(A)):
        help(A, i, 0)
        help(A, i, column)

      for j in range(len(A[0])):
        help(A, 0, j)
        help(A, row, j)

      for i in range(1, row):
        for j in range(1, column):
          if A[i][j] == 1:
            _sum += 1

      return _sum
    
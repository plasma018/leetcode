class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
      answer = 0
      pos_x, pos_y = 0, 0
      for i, row in enumerate(board):
        for j, item in enumerate(row):
          if item is 'R':
            pos_x, pos_y = i, j
            break
      i = pos_x - 1
      
      while i != 0:
        if board[i][pos_y] != '.':
          answer += 1 if board[i][pos_y] is 'p' else 0
          break
        i -= 1
        
      i = pos_x + 1
      
      while i != len(board):
        if board[i][pos_y] != '.':
          answer += 1 if board[i][pos_y] is 'p' else 0
          break
        i += 1
        
      j = pos_y - 1
      
      while j != 0:
        if board[pos_x][j] != '.':
          answer += 1 if board[pos_x][j] is 'p' else 0
          break
        j -= 1
        
      j = pos_y + 1
      
      while j != len(board[0]):
        if board[pos_x][j] != '.':
          answer += 1 if board[pos_x][j] is 'p' else 0
          break
        j += 1
      
      return answer

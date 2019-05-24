class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        S = list(S)
        lenght = len(S)
        index = 0
        count = 999
        while index < lenght:
          if S[index] != C:
            count += 1
            S[index] = count
            index += 1
            continue
          
          S[index] = 0
          count = 0
          
          c, i = 1, index - 1
          index += 1
          while i > -1:
            if S[i] <= c:
              break
            S[i] = c
            c += 1
            i -= 1
        return S  

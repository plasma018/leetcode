class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
      answer = [1, 0]
      for char in S:
        index = ord(char) - 97
        if answer[1] + widths[index] > 100:
          answer[0] += 1
          answer[1] = widths[index]
          continue
        answer[1] += widths[index]
      return answer 

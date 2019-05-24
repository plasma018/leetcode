class Solution:
    def convertToBase7(self, num: int) -> str:
      minus = '' if num >= 0 else '-'
      num = abs(num)
      answer = ''
      while num > 6:
        num, q = divmod(num, 7)
        answer = str(q) + answer
      return minus + str(num) + answer

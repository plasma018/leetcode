class Solution:
    def removeDuplicates(self, S: str) -> str:
      i, length = 1, len(S)
      answer = list(S)
      flag = 0
      remain = []
      while i < length:
        if S[flag] == S[i]:
          answer[flag] = ''
          answer[i] = ''
          if len(remain):
            flag = remain.pop()
          else:
            i += 1
            flag = i
        else:
          remain.append(flag)
          flag = i
        i += 1
      return ''.join(answer)

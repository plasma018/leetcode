class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
      size = len(quiet)
      lists = [[] for i in range(size)]
      status = [False]*size
      answer = list(range(size))
      
      for person, index in richer:
        lists[index].append(person)
      
      for i in range(size):
        self.looker(i, status, lists, answer, quiet)
      
      return answer
    
    def looker(self, index, status, lists, answer, quiet):
      if status[index]:
        return answer[index]
      
      for i in lists[index]:
        j = self.looker(i, status, lists, answer, quiet)
        answer[index] = answer[index] if quiet[answer[index]] < quiet[j] else j 
      status[index] = True
      
      return answer[index]

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
      from itertools import product
      answer = list(map(list, product(range(R), range(C))))
      answer.sort(key=lambda x: abs(x[0]-r0) + abs(x[1] - c0))
      return answer 

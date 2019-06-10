class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
      minutes = 0
      for index, minute in enumerate(customers):
        if grumpy[index] is 0:
          minutes += minute

      _max = 0
      
      for index in range(X):
        if grumpy[index] is 1:
          _max += customers[index]
          
      _temp = _max
      
      for index in range(len(grumpy) - X): 
        if grumpy[index] is 1: 
          _temp -= customers[index]
        if grumpy[index+X] is 1: 
          _temp += customers[index+X]
        _max = max(_temp, _max)
      return _max + minutes

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        _set = set()
        for i in A :
            if i in _set:
                return i
            _set.add(i)

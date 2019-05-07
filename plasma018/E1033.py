class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        [a,b,c] = sorted([a,b,c])
        right = c - b - 1
        left = b - a - 1
        _max = right + left
        return [ 0 if _max is 0 else 1 if right < 2 or left < 2 else 2, _max]

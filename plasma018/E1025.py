class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: -abs(x[0]-x[1]))
        A = len(costs) // 2
        B = A
        _sum = 0
        for item in costs:
            if A == 0:
                _sum += item[1]
            if B == 0:
                _sum += item[0]
            if item[0] < item[1]:
                _sum += item[0]
                A -= 1
            else:
                _sum += item[1]
                B -= 1
        return _sum
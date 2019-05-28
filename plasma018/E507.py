class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 2: return False
        _sum = 0
        sqrt= int(math.sqrt(num)) + 1
        return sum((i+num//i for i in range(1,sqrt) if num % i is 0)) == (num + num)

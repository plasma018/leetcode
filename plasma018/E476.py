class Solution:
    def findComplement(self, num: int) -> int:
        return ((1 << len(bin(num)[2:])) - 1)^ num
    
    
class Solution:
    def findComplement(self, num: int) -> int:
        _str = ''
        for i in bin(num)[2:]:
            _str += '0' if i is '1' else '1'
        return int(_str, 2)

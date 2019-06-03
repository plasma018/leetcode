class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
      length1, length2 = len(str1), len(str2)
      import math
      gcd = math.gcd(length1, length2)
      lcm = length1*length2 // gcd
      times1 = lcm // length1
      times2 = lcm // length2
      if str1*times1 == str2*times2:
        return str1[0:gcd]
      return ''

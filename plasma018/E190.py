class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        number = bin(n)[:1:-1]
        return int(number + ('0'*(32-len(number))),2)

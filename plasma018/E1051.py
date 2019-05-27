class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        correct = sorted(heights)
        count = 0
        for index in range(len(heights)):
            if correct[index] != heights[index]:
                count += 1
        return count

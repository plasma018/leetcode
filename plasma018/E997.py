class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        
        people = [0]*(N+1)
        for i in trust:
            people[i[0]] = -1
            if people[i[1]] != -1:
                people[i[1]] += 1

        judge = -1
        
        for i in range(len(people)):
            if people[i] == N-1:
                judge = i

        return  judge
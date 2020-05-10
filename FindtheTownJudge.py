#https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3325/
#10May2020

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        town=list(range(1,N+1))
        for li in trust:
            if li[0] in town:
                town.remove(li[0])
        if len(town) is 1:
            guess=town[0]
            new_town=list(range(1,N+1))
            new_town.remove(guess)
            for i in new_town:
                if [i,guess] not in trust:
                    return -1
            return guess
        else:
            return -1

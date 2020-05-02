#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/
#02May2020

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count=0
        for stone in S:
        	if stone in J:
        		count=count+1
        return count
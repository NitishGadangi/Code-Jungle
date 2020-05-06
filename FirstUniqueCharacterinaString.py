#https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3320/
#05May2020

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts=Counter(s)
        res=-1
        for a in s:
        	if counts[a]==1:
        		res=s.index(a)
        		break
        return res
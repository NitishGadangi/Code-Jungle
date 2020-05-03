#https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/
#03May2020

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dummy=magazine
        for x in ransomNote:
        	if x in dummy:
        		dummy=dummy[:dummy.find(x)] + dummy[dummy.find(x) + 1:]
        	else:
        		return False
        return True
        
#https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/
#04May2020

from math import log
class Solution:
    def findComplement(self, num: int) -> int:
    	return ((2**(int(log(num,2))+1)-1)-num)


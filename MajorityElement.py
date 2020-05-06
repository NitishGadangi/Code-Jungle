#https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321/
#06May2020

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    	return Counter(nums).most_common(1)[0][0]
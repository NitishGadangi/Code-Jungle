#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3316/
#01May2020


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left=1
        right=n
        while True:
        	mid=int((left+right)/2)
        	if isBadVersion(mid):
        		right=mid
        	else:
        		left=mid+1
        	if left == right:
        		break
        return left
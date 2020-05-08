#https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3323/
#08May2020

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)==2:
        	return True
        x1=coordinates[0][0]
        y1=coordinates[0][1]
        x2=coordinates[1][0]
        y2=coordinates[1][1]
        

        res=True

        for i in range(2,len(coordinates)):
        	x=coordinates[i][0]
        	y=coordinates[i][1]
        	
        	if (y-y1)*(x2-x1)!=(y2-y1)*(x-x1):
        		res=False
        		break
        return res
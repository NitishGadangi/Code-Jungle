#https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3322/
#07May2020


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution(object):
	xparent=None
	yparent=None
	xdepth=-1
	ydepth=-1
    
	def isCousins(self, root, x, y):
		self.setParentandDepth(self,root,x,y,-1,None)
		return (xdepth==ydepth) and (xparent!=yparent)

	def setParentandDepth(root,x,y,depth,pare):
		if root==None:
			return
		if root.val==x:
			xdepth=depth
			xparent=pare
			return
		if root.val==y:
			ydepth=depth
			yparent=pare
			return
		setParentandDepth(root.left,x,y,depth+1,root)
		setParentandDepth(root.right,x,y,depth+1,root)
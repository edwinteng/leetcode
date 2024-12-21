# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        
        def helper(topRight,bottomLeft):
            x1,y1 = bottomLeft.x,bottomLeft.y
            x2,y2 = topRight.x,topRight.y
        
            if x1 >x2 or y1>y2 or not sea.hasShips(topRight,bottomLeft) :
                return 0
            if x1==x2 and y1==y2:
                return 1
            xm,ym = x1+(x2-x1)//2,y1+(y2-y1)//2
            return helper(Point(xm,ym),Point(x1,y1))+helper(Point(x2,ym),Point(xm+1,y1))+helper(Point(x2,y2),Point(xm+1,ym+1))+helper(Point(xm,y2),Point(x1,ym+1))
        return helper(topRight,bottomLeft)


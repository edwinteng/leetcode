class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0]+flowerbed+[0]
        count = 0
        for i in range(1,len(flowerbed)-1):
            if sum(flowerbed[i-1:i+2])==0:
                count+=1
                flowerbed[i]=1
        return True if count>=n else False
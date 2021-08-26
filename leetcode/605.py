class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.append(0)
        flowerbed.insert(0,0)
        
        for i in range(1,len(flowerbed)-1):
            if(flowerbed[i-1] + flowerbed[i] +flowerbed[i+1] == 0 and n>0):
                flowerbed[i] = 1
                n -= 1
                
            if(n==0):
                return True
            
        return False
class Solution:
    """
    @param flowerbed: an array
    @param n: an Integer
    @return: if n new flowers can be planted in it without violating the no-adjacent-flowers rule
    """
    '''
    def canPlaceFlowers(self, flowerbed, n):
        # Write your code here
        count_0 = 0
        start = 0
        while start < len(flowerbed) - 2:
            if flowerbed[start] != 1 or (start ==0 and flowerbed[start] == 0):
                end = start + 1
                while end < len(flowerbed):
                    if end != len(flowerbed) - 1 and flowerbed[end] == 0:
                        end += 1
                        continue
                    elif flowerbed == 0 and end == len(flowerbed) - 1:
                        count_0 += (end - start)/2
                        break
                    else :
                        count_0 += (end - start - 1)/2
                        start = end + 1
                        break
                if count_0 >= n:
                    return True
            else:
                start += 1
        return False
    '''
    def canPlaceFlowers(self,flowerbed,n):
        count = 0
        for i in range(0,len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            left = flowerbed[i-1] if i>0 else 0
            right = flowerbed[i+1] if i<len(flowerbed)-1 else 0
            if left==0 and right==0:
                count+=1
                flowerbed[i] = 1
            if count == n:
                return True
        return False
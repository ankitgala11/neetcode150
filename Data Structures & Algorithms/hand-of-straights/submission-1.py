class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        
        hand.sort()

        if n%groupSize!=0:
            return False

        i = 0
        ele = -1

        while i<n:
            
            while i<n :
                
                ele = hand[i]
                if ele !=-1:break
                i+=1
            
            if i==n:
                return True

            hand[i]=-1
            # print(i, hand)
            cnt = 1

            j=i+1
            while cnt!=groupSize and j<n:
                # print(hand[j], ele)
                if hand[j]==ele+1:
                    ele = hand[j]
                    hand[j]=-1
                    cnt +=1
                
                j+=1
            # print("cnt" ,cnt, groupSize, hand)
            if cnt!=groupSize:
                return False
            else:
                i=0
        
        return True
            
        
        
        


 


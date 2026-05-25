class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        x = target[0]
        y = target[1]
        z = target[2]

        a = -1
        b = -1
        c = -1
        for p,q,r in triplets:
            if p<=x and q<=y and r<=z:
                a = p
                b = q
                c = r

            
        if a==-1:
            return False
        
        

        

        for i in range(n):
        
            
            temp1 = max(triplets[i][0] , a )
            temp2 = max(triplets[i][1] , b )
            temp3 = max(triplets[i][2] , c )
            print(temp1, temp2, temp3)
        
            if temp1==x and temp2==y and temp3==z:
                return True
            
            elif temp1<=x and temp2<=y and temp3<=z:
                a = temp1
                b = temp2
                c = temp3
        
        return False



class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        n = len(position)
        fleets = 0
        temp = list(zip(position, speed))
        last=0
        temp.sort(key = lambda x : -x[0] )

        for p , s in temp:

            time = (target - p)/s

            if last < time:
                fleets += 1
                last = time

        return fleets


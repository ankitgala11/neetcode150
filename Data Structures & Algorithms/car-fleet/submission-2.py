class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        n = len(position)
        seen = []
        temp = list(zip(position, speed))
        last=0
        temp.sort(key = lambda x : -x[0] )

        for p , s in temp:

            time = (target - p)/s

            if last < time:
                seen.append(time)
                last = time

        return len(seen)


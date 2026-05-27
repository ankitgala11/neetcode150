class CountSquares:

    def __init__(self):
        self.mp = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.mp[tuple(point)] += 1
  
        

    def count(self, point: List[int]) -> int:

        qx ,qy = point
        res=0

        for x,y in list(self.mp.keys()):

            if abs(qx-x) == abs(qy-y) and qx!=x and qy!=y:
                res+= self.mp[(x, y)]* self.mp[(qx,y)] * self.mp[(x, qy)]
        
        return res



        

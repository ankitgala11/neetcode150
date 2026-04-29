class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = None
        

    def push(self, val: int) -> None:

        if not self.stack:
            self.stack.append(val)
            self.mini = val
        
        else:
            if val < self.mini:
                self.stack.append(2 * val - self.mini)
                self.mini = val
            else:
                self.stack.append(val)
        # print(self.stack, self.mini)

        

    def pop(self) -> None:
        if not self.stack:
            return -1
        
        if self.mini > self.stack[-1]:
            temp = self.mini
            val = self.stack.pop()
            self.mini = 2 * self.mini - val
            # print(self.stack, self.mini)
            return temp
        else:
            temp = self.stack.pop()
            print(self.stack, self.mini)
            return temp

    def top(self) -> int:
        if self.stack:
            if self.mini>self.stack[-1]:
                return self.mini 
            else:
                return self.stack[-1]
        return -1
        

    def getMin(self) -> int:
        return self.mini
        

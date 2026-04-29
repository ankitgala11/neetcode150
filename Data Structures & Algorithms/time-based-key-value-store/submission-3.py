class TimeMap:

    def __init__(self):
        self.mp = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mp:
            self.mp[key].append((value, timestamp))
        else:
            self.mp[key] = [(value,timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.mp:
            return ""

        ans = ""
        for val, time in self.mp[key]:
            if time<=timestamp:
                ans = val
            else:
                break

        return ans

        

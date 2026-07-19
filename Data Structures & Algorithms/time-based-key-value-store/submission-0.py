class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        arr = self.dic[key]
        l = 0
        r = len(arr) - 1
        res = ""
        while l <= r:
            mid = (l+r)//2
            time , value = arr[mid]
            if time <= timestamp:
                res = value
                l = mid + 1
            else:
                r = mid - 1    
        return res
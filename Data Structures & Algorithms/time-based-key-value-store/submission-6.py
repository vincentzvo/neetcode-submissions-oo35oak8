class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.hashmap.get(key, [])
        l = 0
        r = len(self.hashmap[key]) - 1
        while l <= r:
            m = (l + r) // 2
            if timestamp >= values[m][1]:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
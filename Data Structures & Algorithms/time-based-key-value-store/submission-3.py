class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append(tuple((value, timestamp)))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        l = 0
        r = len(self.hashmap[key]) - 1
        while l <= r:
            m = (l + r) // 2
            if timestamp > self.hashmap[key][m][1]:
                res = self.hashmap[key][m][0]
                l = m + 1
            elif timestamp < self.hashmap[key][m][1]:
                r = m - 1
            else:
                res = self.hashmap[key][m][0]
                break
        return res
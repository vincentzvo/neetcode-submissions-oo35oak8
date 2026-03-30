class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append(tuple((value, timestamp)))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        for v in self.hashmap[key]:
            if v[1] <= timestamp:
                res = v[0]

        return res
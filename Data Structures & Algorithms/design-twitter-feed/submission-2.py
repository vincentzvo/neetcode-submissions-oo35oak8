class Twitter:
    def __init__(self):
        self.count = 0 # count that will go negative to keep track of most recent tweets
        self.tweetMap = defaultdict(list) # hash with list vals for mult tweets by same user
        self.followMap = defaultdict(set) # hash with set vals for followers and followees (no dupes)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId]) # key = userId, val = [recency, tweetId]
        self.count -= 1 # decrement count because minHeap will prioratize smaller values as more recent

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId) # add self to followers so that own tweets appear
        for followeeId in self.followMap[userId]: # traverse all people user follows
            if followeeId in self.tweetMap: # if person has posted a tweet
                index = len(self.tweetMap[followeeId]) - 1 # how many tweets the user has posted
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId) # adds followee to followers set

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId) # rms followee from followers set

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)

        hashmap = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                pattern = word[:i] + "*" + word[i + 1:]
                hashmap[pattern].append(word)
        
        q = deque([beginWord])
        visit = set([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(beginWord)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for adjWord in hashmap[pattern]:
                        if adjWord not in visit:
                            visit.add(adjWord)
                            q.append(adjWord)
            res += 1
        return 0
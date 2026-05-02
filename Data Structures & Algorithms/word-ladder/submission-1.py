class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:                             # if endWord isnt in word list:
            return 0                                                # return 0
        
        adjList = defaultdict(list)                             # init adjlist with list vals
        wordList.append(beginWord)                              # append beginword to wordlist
        for word in wordList:                                   # for each word:
            for i in range(len(word)):                              # for each index:
                pattern = word[:i] + "*" + word[i + 1:]                 # set pattern to word with * replacing letter at cur idx
                adjList[pattern].append(word)                           # append cur word to adjlist at cur pattern

        visit = set([beginWord])                                # init visit set with beginWord in it
        q = deque([beginWord])                                  # init q with beginWord in it
        res = 1                                                 # init res to 1
        while q:                                                # while q isnt empty
            for i in range(len(q)):                                 # for each word cur in q
                word = q.popleft()                                      # set word to left pop q
                if word == endWord:                                     # if popped word is endword:
                    return res                                              # return res
                for j in range(len(word)):                              # for each idx:
                    pattern = word[:j] + "*" + word[j + 1:]                 # set pattern again
                    for adjWord in adjList[pattern]:                        # for word in adjlist at cur pattern
                        if adjWord not in visit:                                # if cur word not visited:
                            visit.add(adjWord)                                      # add cur word to visit
                            q.append(adjWord)                                       # append cur word to q
            res += 1                                                # increm res
        return 0                                                # return 0 if popped word never equals endword
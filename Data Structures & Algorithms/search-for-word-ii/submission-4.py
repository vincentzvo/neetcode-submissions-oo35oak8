class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()                               # init root trienode
        for w in words:                                 # populate trie
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])          # init row, cols
        res, path = set(), set()                        # init res and path sets

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or                       # return if:
                r >= ROWS or c >= COLS or               # r or c out of bounds
                board[r][c] not in node.children or     # word not in trie
                (r, c) in path):                        # letter already used
                return
            
            path.add((r, c))                            # add row col to path
            node = node.children[board[r][c]]           # move down trie
            word += board[r][c]                         # append letter to word 
            if node.isWord:                             # if is word, add to res
                res.add(word)

            dfs(r + 1, c, node, word)                   # run dfs on all surrounding
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word) 
            dfs(r, c - 1, node, word)

            path.remove((r, c))                         # remove row, col from path
        
        for r in range(ROWS):                           # traverse every row
            for c in range(COLS):                       # traverse every col
                dfs(r, c, root, "")                     # cal dfs on every letter
        return list(res)                                # return res cast as list
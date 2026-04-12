class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        p, a = set(), set()
        pQ, aQ = deque(), deque()
        
        def addP(r, c, h):
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                (r, c) in p or
                heights[r][c] < h):
                return
            
            pQ.append([r, c])
            p.add((r, c))

        def addA(r, c, h):
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                (r, c) in a or
                heights[r][c] < h):
                return
            
            aQ.append([r, c])
            a.add((r, c))


        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    p.add((r, c))
                    pQ.append([r, c])
                if r == ROWS - 1 or c == COLS - 1:
                    a.add((r, c))
                    aQ.append([r, c])

        while pQ:
            for i in range(len(pQ)):
                r, c = pQ.popleft()
                h = heights[r][c]
                addP(r - 1, c, h)
                addP(r + 1, c, h)
                addP(r, c - 1, h)
                addP(r, c + 1, h)

        while aQ:
            for i in range(len(aQ)):
                r, c = aQ.popleft()
                h = heights[r][c]
                addA(r - 1, c, h)
                addA(r + 1, c, h)
                addA(r, c - 1, h)
                addA(r, c + 1, h)

        res = []
        for r, c in p:
            if (r, c) in a:
                res.append([r, c])

        return res


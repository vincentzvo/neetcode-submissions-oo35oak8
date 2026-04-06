"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}                               # init hashmap to map given node to new clone

        def clone(node):                            # recursive dfs func
            if node in oldToNew:                        # if node already cloned:
                return oldToNew[node]                       # return already existing clone
            
            copy = Node(node.val)                       # create copy with matching val
            oldToNew[node] = copy                       # place old, clone node pair in hashmap

            for n in node.neighbors:                    # for each of the cur nodes neighbors:
                copy.neighbors.append(clone(n))             # clone them and add them to curs clone neighbors

            return copy                                 # return last clone
        
        return clone(node) if node else None        # return call on clone(node) if node not null else return null
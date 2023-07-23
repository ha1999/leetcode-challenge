from typing import Optional, Dict
from pprint import pprint


class TreeNode:
    def __init__(self, value: Optional[int] = None, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, N, memos={1: [TreeNode(0)]}):
        if N not in memos:
            ret = []
            for l in range(1, N - 1, 2):
                for left in self.allPossibleFBT(l):
                    for right in self.allPossibleFBT(N - l - 1):
                        root = TreeNode(0, left, right)
                        ret += [root]
            memos[N] = ret
        return memos[N]


sl = Solution()

pprint(sl.allPossibleFBT(13))

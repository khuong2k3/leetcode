from typing import Self

class TreeNode:
    def __init__(self, val: int=0, left: Self | None=None, right: Self | None=None):
        self.val: int = val
        self.left: Self | None = left
        self.right: Self | None = right
        

class Node:
    def __init__(self, val: int | None = None, children: list[Self] | None = None):
        self.val: int | None = val
        self.children: list[Self] | None = children


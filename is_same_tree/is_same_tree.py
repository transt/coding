from typing import List


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, a: TreeNode, b: TreeNode) -> bool:
        if a is None and b is None:
            return True
        if a is None and b is not None: 
            return False
        if a is not None and b is None:
            return False
        if a.val == b.val and self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right): 
            return True
        else:
            return False

def build_tree(values: List[int]) -> TreeNode:
    if not values:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in values]
    n = len(values)

    for i in range(n):
        node = nodes[i]
        if node is not None:
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            if left_index < n:
                node.left = nodes[left_index]
            if right_index < n:
                node.right = nodes[right_index]
    return nodes[0]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 3], [1, 2, 3], True),
        ([], [], True),
        ([1, 2, 3], [1, 3, 2], False)
    ]

    for idx, (tree_list1, tree_list2, expected) in enumerate(tests, 1):
        tree1 = build_tree(tree_list1)
        tree2 = build_tree(tree_list2)
        result = sol.isSameTree(tree1, tree2)
        print(f"Test {idx}: isSameTree({tree_list1}, {tree_list2}) => result={result}, expected={expected}")
        assert result == expected, f"Test {idx} failed! Expected={expected}, Got={result}"
        print("All tests passed!")

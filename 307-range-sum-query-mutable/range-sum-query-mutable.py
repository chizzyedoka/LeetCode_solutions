class Node:
    def __init__(self, startInterval, endInterval):
        self.startInterval = startInterval
        self.endInterval = endInterval
        self.data = 0 # the range sum of intervals
        self.left = None
        self.right = None


class NumArray:

    def __init__(self, nums: List[int]):
        # build the segment tree
        self.root = self._construct_tree(nums, 0, len(nums)-1)

    def _construct_tree(self, arr, start, end):
        if start == end:
            leaf = Node(start, end)
            leaf.data = arr[start]
            return leaf
        
        node = Node(start, end)
        mid = (start + end) // 2

        node.left = self._construct_tree(arr, start, mid)
        node.right = self._construct_tree(arr, mid+1, end)

        node.data = node.left.data + node.right.data
        return node

    def update(self, index: int, val: int) -> None:
        self._update(self.root, index, val)

    def _update(self, node, index, val):
        # if node covers the target inde
        if node.startInterval <= index <= node.endInterval:
            if node.startInterval == node.endInterval:
                node.data = val # update the leaf
                return node.data

            # recursively update children
            left_sum = self._update(node.left, index, val)
            right_sum = self._update(node.right, index, val)

            node.data = left_sum + right_sum
        return node.data
        

    def sumRange(self, left: int, right: int) -> int:
        return self._query(self.root, left, right)

    def _query(self, node, left, right):
        # completely inside query range
        if node.startInterval >= left and node.endInterval <= right:
            return node.data

        # completely outside query range
        if (node.endInterval < left) or (node.startInterval > right):
            return 0

        # partial overlap
        return self._query(node.left, left, right) + self._query(node.right, left, right)

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def widthOfBinaryTree(tree):
    t = TreeNode()
    start = 0
    for i in range (len(tree)):
        t.val = tree[i]
        t.left = tree[i+1]
        t.right = tree[i+2]
        print(t.left, t.val, t.right)


widthOfBinaryTree([1,2,3,5])

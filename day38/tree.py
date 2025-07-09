from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


def preOrder(root):
    if root==None:
        return
    print(root.val,end=" ")
    preOrder(root.left)
    preOrder(root.right)



def inOrder(root):
    if root==None:
        return
    inOrder(root.left)
    print(root.val,end=" ")
    inOrder(root.right)


def postOrder(root):
    if root==None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val,end=" ")


def levelOrder(root):
    queue=deque([root])
    while queue:
        current=queue.popleft()
        print(current.val,end=" ")
        if current.left!=None:
            queue.append(current.left)

        if current.right!=None:
            queue.append(current.right)


root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.right=TreeNode(6)
root.left.left.left=TreeNode(9)
root.left.left.right=TreeNode(10)
root.left.right.right=TreeNode(11)
root.right.right.left=TreeNode(7)
root.right.right.right=TreeNode(8)

print("\n preOrder:")
preOrder(root)
print("\n inOrder:")
inOrder(root)
print("\n postOrder:")
postOrder(root)
print("\n levelOrder:")
levelOrder(root)
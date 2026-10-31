# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # -> "1,2,3,null,null,4,5"
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        tokens = []

        def preorder(root):
            if not root:
                return tokens.append("N")

            tokens.append(str(root.val))
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return ",".join(tokens)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = iter(data.split(","))
        def build():
            token = next(tokens)

            if token == "N":
                return None

            node = TreeNode(int(token))
            node.left = build()
            node.right = build()

            return node

        return build()

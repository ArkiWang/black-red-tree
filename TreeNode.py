class TreeNode(object):
    # 0:red 1:black
    def __init__(self, value, color=0, left=None, right=None):
         self.value = value
         self.left = left
         self.right = right
         self.color = color

    def changeColor(self, color):
        self.color = color
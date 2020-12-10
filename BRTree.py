from TreeNode import TreeNode

class BRTree(object):
    def __init__(self, root=None):
        self.root = root

    #unique tree
    def insert(self, v: int)->None:
        if self.root == None:
            self.root = TreeNode(value=v, color=1)
            return
        z = TreeNode(v)
        x = self.root
        while x != None:
            y = x
            if z.value < x.value:
                x = x.left
            else:x = x.right
        z.parent = y
        if z.value < y.value:
            y.left = z
        else:
            y.right = z
        if y == None:
            self.root = z
        elif z.value < y.value:
            y.left = z
        else:
            y.right = z
        z.left = None
        z.right = None
        z.color = 0
        self.insert_fix_up(z)

    def insert_fix_up(self, z: TreeNode):
        while  z.parent!= None and z.parent.color == 0:#red
            if z.parent != None and z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 0:
                    z.parent.color = 1
                    y.color = 1
                    z.parent.parent.color = 0
                    z = z.parent.parent
                elif z == z.parent.right:
                    z = z.parent
                    self.left_rotate(z)
                    z.parent.color = 1
                    z.parent.parent.color = 0
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y != None and y.color == 0:
                    z.parent.color = 1
                    y.color = 1
                    z.parent.parent.color = 0
                    z = z.parent.parent
                elif z == z.parent.left:
                    z = z.parent
                    self.right_rotate(z)
                    z.parent.color = 1
                    z.parent.parent.color = 0
                    self.left_rotate(z.parent.parent)
        self.root.color = 1



    def left_rotate(self, x: TreeNode):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y


    def right_rotate(self, x:TreeNode):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y


    def get_node(self, x: int):
        p = self.root
        while p != None and p.value != x:
            if x < p.value: p = p.left
            else: p = p.right
        return p

    def rb_transplant(self, u: TreeNode, v: TreeNode):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent

    def tree_minimum(self, x: TreeNode):
        while x.left != None:
            x = x.left
        return x

    def rb_delete(self, z: TreeNode):
        y = z
        y_oc = y.color
        if z.left == None:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == None:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            y_oc = y.color
            x = y.right
            if x != None and y.parent == z:
                x.parent = y
            elif y.right != None:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_oc == 1:
            self.rb_delete_fixup(x)

    def rb_delete_fixup(self, x: TreeNode):
        while x != self.root and x != None and x.color == 1:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 0:
                    w.color = 1
                    x.parent.color = 0
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 1 and w.right.color == 1:
                    w.color = 0
                    x = x.p
                elif w.right.color == 1:
                    w.left.color = 1
                    w.color = 1
                    self.right_rotate(w)
                    w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 1
                    w.right.color = 1
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 0:
                    w.color = 1
                    x.parent.color = 0
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.left.color == 1 and w.right.color == 1:
                    w.color = 0
                    x = x.p
                elif w.left.color == 1:
                    w.right.color = 1
                    w.color = 1
                    self.left_rotate(w)
                    w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 1
                    w.left.color = 1
                    self.right_rotate(x.parent)
                    x = self.root
        if x != None:x.color = 1

    def delete(self, x: int):
        nx = self.get_node(x)
        self.rb_delete(nx)





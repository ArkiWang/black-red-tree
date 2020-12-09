from TreeNode import TreeNode

class BRTree(object):
    def __init__(self, root=None):
        self.root = root

    #unique tree
    def insert_node(self, x: int)->None:
        if self.root == None:
            self.root = TreeNode(value=x, color=1)
            return
        p = self.insert_to(x)
        z = TreeNode(x)
        if p.color == 1:#black
            if x < p.value:
                p.left = z
            else:
                p.right = z
        else:#red
            if x < p.value:
                p.left = z
            else:
                p.right = z
            self.insert_fix_up(z)

    def insert_fix_up(self, z: TreeNode):
        zp = self.get_parent(z)
        while  zp!= None and zp.color == 0:#red
            zpp = self.get_parent(zp)
            if zp == zpp.left:
                y = zpp.right
                if y != None and y.color == 0:
                    zp.color = 1
                    y.color = 1
                    zpp.color = 0
                    z = zpp
            elif zp == zp.right:
                z = zp
                self.left_rotate(z)
                zp.color = 1
                zpp.color = 0
                self.right_rotate(zpp)
            else:
                z = zp
                self.right_rotate(z)
                zp.color = 1
                zpp.color = 0
                self.left_rotate(zpp)
        self.root.color = 1



    def left_rotate(self, x: TreeNode):
        p = self.get_parent(x)
        y = x.right
        yl = y.left
        p.right = y
        y.left = x
        x.right = yl

    def right_rotate(self, x:TreeNode):
        p = self.get_parent(x)
        y = x.left
        yr = y.right
        p.left = y
        y.right = x
        x.left = yr

    def insert_to(self, x: int) -> TreeNode:
        p = self.root
        while p != None:
            if x < p.value:
                if p.left == None: return p
                p = p.left
            else:
                if p.right == None: return p
                p = p.right
        return p

    def get_parent(self, n: TreeNode) -> TreeNode:
        p = self.root
        while p != None and p.left != n and p.right != n:
            if n.value < p.value:p = p.left
            else: p = p.right
        return p

    def get_node(self, x: int):
        p = self.root
        while p != None and p.value != x:
            if x < p.value: p = p.left
            else: p = p.right
        return p

    def rb_transplant(self, u: TreeNode, v: TreeNode):
        up = self.get_parent(u)
        vp = self.get_parent(v)
        if up == None:
            self.root = v
        elif u == up.left:
            up.left = v
        else:
            up.right = v
        vp = up

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
            xp = self.get_parent(x)
            yp = self.get_parent(y)
            if yp == z:
                xp = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                yrp = self.get_parent(y.right)
                yrp = y
                self.rb_transplant(z, y)
                y.left = z.left
                ylp = self.get_parent(y.left)
                ylp = y
                y.color = z.color
        if y_oc == 1:
            self.rb_delete_fixup(x)

    def rb_delete_fixup(self, x: TreeNode):
        while x != self.root and x.color == 1:
            xp = self.get_parent(x)
            if x == xp.left:
                w = xp.right
                if w.color == 0:
                    w.color = 1
                    xp.color = 0
                    self.left_rotate(xp)
                    w = xp.right
                if w.right.color == 1:
                    w.left.color = 1
                    w.color = 1
                    self.right_rotate(w)
                    w = xp.right
                    w.color = xp.color
                    xp.color = 1
                    w.right.color = 1
                    self.left_rotate(xp)
                    x = self.root
            else:
                w = xp.left
                if w.color == 0:
                    w.color = 1
                    xp.color = 0
                    self.right_rotate(xp)
                    w = xp.left
                if w.left.color == 1:
                    w.right.color = 1
                    w.color = 1
                    self.left_rotate(w)
                    w = xp.left
                    w.color = xp.color
                    xp.color = 1
                    w.left.color = 1
                    self.right_rotate(xp)
                    x = self.root
        x.color = 1

    def delete(self, x :int):
        nx = self.get_node(x)
        self.rb_delete(nx)





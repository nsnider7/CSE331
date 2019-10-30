if root.left.left is None:
    parent_side = None
    # determine which side the parent is on
    parent_side = parentSide(root)
    # rotate the new root to position
    if parent_side is not None:
        if root.parent.left == root:
            AVLTreeSetChild(root.parent, "left", root.left.right)
        elif root.parent.right == root:
            AVLTreeSetChild(root.parent, "right", root.left.right)
        AVLTreeSetChild(root.left.right, "right", root)
        AVLTreeSetChild(root.left.right, "left", root.left)
        root.left = None ##########
        leftRightChild.left.right = None ########
    else:
        self.root = root.left.right
        root.left.right = None
        self.root.parent = None
        AVLTreeSetChild(self.root, "right", root)
        AVLTreeSetChild(self.root, "left", root.left)
        root.left = None
    AVLTreeUpdateHeight(leftRightChild.left) ############# ADDED
    AVLTreeUpdateHeight(leftRightChild.right) ########### ADDED
    AVLTreeUpdateHeight(leftRightChild)

    # set new roots values in rotation

elif root.left.right is None: # then do left left rotation
    # determine which side the parent is on
    parent_side = parentSide(root)
    if parent_side is not None:
        if root.parent.left == root:
            AVLTreeSetChild(root.parent, "left", root.left)
        elif root.parent.right == root:
            AVLTreeSetChild(root.parent, "right", root.left)
    else:
        self.root = root.left
        self.root.parent = None
    # rotate the new root to position
    AVLTreeSetChild(root.left, "right", root)
    AVLTreeSetChild(root, "left", None)
    AVLTreeUpdateHeight(root.parent)

AVLTreeUpdateHeight(self.root)
return self.root  # return new root